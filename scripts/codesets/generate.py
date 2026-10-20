#!/usr/bin/env python3
"""Generate dist/openapi files from source/openapi masters with codeset-aligned enums.

Every node in a master carrying ``x-codeset-ref: <List>/<CodeSet>`` has its
``enum`` / ``x-namespaced-enum`` values replaced with the ``Code Value`` column
of the pinned codeset CSV (in CSV order), after applying any approved
exceptions from ``source/codeset-config.yaml``. Everything else in the master
is copied to dist byte-for-byte. JSON files are regenerated from the YAML.

Usage:
  generate.py                 regenerate dist files
  generate.py --check         exit 1 if dist files are out of date (no writes)
  generate.py --codesets-dir  read CSVs from a local checkout instead of GitHub
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import fnmatch
import io
import json
import os
import re
import sys
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from openapi_spec_validator import validate as validate_openapi
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "source" / "codeset-config.yaml"
SOURCE_DIR = ROOT / "source" / "openapi"
DIST_DIR = ROOT / "dist" / "openapi"
ENUM_KEYS = ("enum", "x-namespaced-enum")
TAG_RE = re.compile(r"^( *)x-codeset-ref:\s*(\S.*?)\s*$")
ITEM_RE = re.compile(r"^( *)- (.*)$")

_yaml12 = YAML(typ="safe", pure=True)


class GenerationError(Exception):
    pass


@dataclass
class TaggedNode:
    file: str
    pointer: str
    ref: str
    enum_key: str
    master_values: list
    new_values: list = field(default_factory=list)
    dist_values: list | None = None
    exceptions: list = field(default_factory=list)


@dataclass
class Report:
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    nodes: list = field(default_factory=list)
    ignored: list = field(default_factory=list)
    unclassified: list = field(default_factory=list)
    files: dict = field(default_factory=dict)
    referenced: set = field(default_factory=set)
    codesets: dict = field(default_factory=dict)
    meta: dict = field(default_factory=dict)


# --------------------------------------------------------------------------- helpers

def escape(token: str) -> str:
    return token.replace("~", "~0").replace("/", "~1")


def walk(node, pointer=""):
    """Yield (pointer, mapping) for every mapping in document order."""
    if isinstance(node, dict):
        yield pointer, node
        for k, v in node.items():
            yield from walk(v, f"{pointer}/{escape(str(k))}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, f"{pointer}/{i}")


def resolve(doc, pointer):
    node = doc
    for raw in pointer.split("/")[1:]:
        token = raw.replace("~1", "/").replace("~0", "~")
        node = node[int(token)] if isinstance(node, list) else node[token]
    return node


def roundtrips(item_text: str, value: str) -> bool:
    """True if `- item_text` loads as `value` under both YAML 1.1 and YAML 1.2."""
    text = f"- {item_text}\n"
    try:
        return yaml.safe_load(text) == [value] and _yaml12.load(text) == [value]
    except Exception:
        return False


def render_scalar(value: str) -> str:
    if roundtrips(value, value):
        return value
    return "'" + value.replace("'", "''") + "'"


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def gh(kind: str, message: str):
    if os.environ.get("GITHUB_ACTIONS"):
        print(f"::{kind}::{message.replace(chr(10), '%0A')}")


# --------------------------------------------------------------------------- inputs

def load_codesets(cfg, codesets_dir: str | None, report: Report) -> dict:
    src = cfg["codesetSource"]
    out = {}
    for list_name, filename in src["lists"].items():
        if codesets_dir:
            data = (Path(codesets_dir) / filename).read_bytes()
        else:
            url = f"https://raw.githubusercontent.com/{src['repository']}/{src['commit']}/{filename}"
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = resp.read()
        reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig")))
        for row in reader:
            name = (row.get("Code Set") or "").strip()
            value = row.get("Code Value") or ""
            if not name:
                continue
            if value != value.strip():
                report.warnings.append(f"{list_name}/{name}: stripped whitespace from code value {value!r}")
                value = value.strip()
            if not value:
                report.warnings.append(f"{list_name}/{name}: skipped row with empty Code Value")
                continue
            values = out.setdefault(f"{list_name}/{name}", [])
            if value in values:
                report.warnings.append(f"{list_name}/{name}: duplicate code value {value!r} in CSV (kept first)")
                continue
            values.append(value)
    return out


def load_value_sources(cfg) -> dict:
    sources = {}
    for name, rel in (cfg.get("valueSources") or {}).items():
        data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        sources[name] = {"values": [c["alpha2"] for c in data["codes"]], "source": data["source"], "path": rel}
    return sources


# --------------------------------------------------------------------------- core

def compute_values(node: TaggedNode, codesets, exceptions, sources, report: Report):
    if node.ref not in codesets:
        raise GenerationError(f"{node.file}#{node.pointer}: x-codeset-ref '{node.ref}' not found in pinned codesets")
    values = list(codesets[node.ref])
    for exc in exceptions:
        if exc.get("codeset") != node.ref:
            raise GenerationError(
                f"{node.file}#{node.pointer}: exception codeset '{exc.get('codeset')}' does not match x-codeset-ref '{node.ref}'")
        for exp in exc.get("expandValues") or []:
            placeholder, src_name = exp["value"], exp["valuesFrom"]
            if src_name not in sources:
                raise GenerationError(f"{node.file}#{node.pointer}: unknown expansion source '{src_name}'")
            if placeholder not in values:
                raise GenerationError(f"{node.file}#{node.pointer}: expansion placeholder '{placeholder}' not in codeset {node.ref}")
            expansion = sorted({exp.get("prefix", "") + v for v in sources[src_name]["values"]})
            expansion = [v for v in expansion if v not in values]
            i = values.index(placeholder)
            values[i:i + 1] = expansion
            node.exceptions.append(f"expanded `{placeholder}` into {len(expansion)} values from {src_name}")
        for extra in exc.get("additionalValues") or []:
            if extra in values:
                report.warnings.append(f"{node.file}#{node.pointer}: additional value '{extra}' already in codeset {node.ref}")
                continue
            values.append(extra)
        if exc.get("additionalValues"):
            node.exceptions.append(f"retained {len(exc['additionalValues'])} additional values: {', '.join(exc['additionalValues'])}")
    node.new_values = values


def locate_enum_block(lines, tag_idx, enum_key):
    """Return (key_idx, start, end) for the sibling enum list of the tag at tag_idx."""
    ind = indent_of(lines[tag_idx])
    key_re = re.compile(rf"^ {{{ind}}}{re.escape(enum_key)}:\s*$")

    def in_mapping(j):
        line = lines[j]
        return not line.strip() or indent_of(line) >= ind

    candidates = []
    j = tag_idx + 1
    while j < len(lines) and in_mapping(j):
        if key_re.match(lines[j]):
            candidates.append(j)
        j += 1
    j = tag_idx - 1
    while j >= 0 and in_mapping(j):
        if key_re.match(lines[j]):
            candidates.append(j)
        j -= 1
    if len(candidates) != 1:
        raise GenerationError(f"line {tag_idx + 1}: expected one sibling '{enum_key}:' block, found {len(candidates)}")
    key_idx = candidates[0]
    # The block runs to the last list item; comment and blank lines between
    # items are kept and re-attached to the item that follows them.
    start = end = k = key_idx + 1
    while k < len(lines):
        line = lines[k]
        if ITEM_RE.match(line) and indent_of(line) >= ind:
            end = k + 1
        elif not (not line.strip() or (line.lstrip().startswith("#") and indent_of(line) >= ind)):
            break
        k += 1
    if end == start:
        raise GenerationError(f"line {key_idx + 1}: '{enum_key}:' must be a block list")
    item_indents = {indent_of(lines[k]) for k in range(start, end) if ITEM_RE.match(lines[k])}
    if len(item_indents) != 1:
        raise GenerationError(f"line {key_idx + 1}: inconsistent list indentation")
    return key_idx, start, end


def process_file(name, cfg, codesets, sources, report: Report) -> dict:
    """Generate one master; return {path: bytes} for the dist outputs."""
    master_path = SOURCE_DIR / name
    dist_yaml = DIST_DIR / name
    dist_json = dist_yaml.with_suffix(".json")

    raw = master_path.read_bytes().decode("utf-8")
    text = raw.replace("\r\n", "\n")
    try:
        doc = yaml.safe_load(text)
    except yaml.YAMLError as e:
        raise GenerationError(f"{name}: invalid YAML: {e}") from None
    lines = text.split("\n")

    # Preserve the line endings of the existing dist file (the VRP YAML is CRLF).
    eol = "\n"
    old_dist_yaml = old_dist_json = None
    old_dist_doc = None
    if dist_yaml.exists():
        old_dist_yaml = dist_yaml.read_bytes().decode("utf-8")
        if "\r\n" in old_dist_yaml:
            eol = "\r\n"
        old_dist_doc = yaml.safe_load(old_dist_yaml)
    if dist_json.exists():
        old_dist_json = dist_json.read_bytes().decode("utf-8")

    file_exceptions = [e for e in cfg.get("exceptions") or [] if e["file"] == name]
    file_ignores = [r for r in cfg.get("ignoredEnums") or [] if r["file"] == name]
    used_exceptions, used_ignore_patterns = set(), set()

    tagged, untagged = [], []
    for ptr, mapping in walk(doc):
        keys = [k for k in ENUM_KEYS if k in mapping]
        if "x-codeset-ref" in mapping:
            if len(keys) != 1:
                raise GenerationError(f"{name}#{ptr}: x-codeset-ref requires exactly one of {ENUM_KEYS}")
            ref = mapping["x-codeset-ref"]
            if not isinstance(ref, str) or ref.count("/") != 1 or ref.split("/")[0] not in cfg["codesetSource"]["lists"]:
                raise GenerationError(f"{name}#{ptr}: invalid x-codeset-ref {ref!r}")
            node = TaggedNode(name, ptr, ref, keys[0], list(mapping[keys[0]]))
            if old_dist_doc is not None:
                try:
                    node.dist_values = list(resolve(old_dist_doc, ptr)[keys[0]])
                except (KeyError, IndexError, TypeError):
                    node.dist_values = None
            tagged.append(node)
        else:
            for k in keys:
                untagged.append((ptr, k, mapping[k]))

    tag_lines = [i for i, line in enumerate(lines) if TAG_RE.match(line)]
    if len(tag_lines) != len(tagged):
        raise GenerationError(f"{name}: found {len(tag_lines)} x-codeset-ref lines but {len(tagged)} tagged nodes")

    replacements = []
    for idx, node in zip(tag_lines, tagged):
        if TAG_RE.match(lines[idx]).group(2) != node.ref:
            raise GenerationError(f"{name} line {idx + 1}: x-codeset-ref text/document mismatch")
        excs = [e for e in file_exceptions if e["pointer"] == node.pointer]
        used_exceptions.update(id(e) for e in excs)
        compute_values(node, codesets, excs, sources, report)
        report.referenced.add(node.ref)
        try:
            _, start, end = locate_enum_block(lines, idx, node.enum_key)
        except GenerationError as e:
            raise GenerationError(f"{name}#{node.pointer}: {e}") from None
        block = lines[start:end]
        if yaml.safe_load("\n".join(block)) != node.master_values:
            raise GenerationError(f"{name}#{node.pointer}: could not safely parse enum block (lines {start + 1}-{end})")
        item_indent = " " * indent_of(block[0])
        existing, attached, pending = {}, {}, []
        for line in block:
            m = ITEM_RE.match(line)
            if not m:
                pending.append(line)
                continue
            value = yaml.safe_load(f"- {m.group(2)}")[0]
            existing.setdefault(value, m.group(2))
            attached.setdefault(value, []).extend(pending)
            pending = []
        for value, extra in attached.items():
            if extra and value not in node.new_values:
                report.warnings.append(f"{name}#{node.pointer}: dropped comment attached to removed value '{value}'")
        new_block = []
        for v in node.new_values:
            new_block.extend(attached.get(v, []))
            prior = existing.get(v)
            new_block.append(f"{item_indent}- {prior if prior is not None and roundtrips(prior, v) else render_scalar(v)}")
        replacements.append((start, end, new_block))
        report.nodes.append(node)

    for e in file_exceptions:
        if id(e) not in used_exceptions:
            raise GenerationError(f"{name}: exception for {e['pointer']} does not match any tagged node")

    for start, end, new_block in sorted(replacements, reverse=True):
        lines[start:end] = new_block
    out_text = "\n".join(lines)
    out_doc = yaml.safe_load(out_text)

    # Verify the output: tagged enums hold exactly the computed string values,
    # and nothing else in the document changed.
    expected = yaml.safe_load(text)
    for node in tagged:
        got = resolve(out_doc, node.pointer)[node.enum_key]
        if got != node.new_values or not all(isinstance(v, str) for v in got):
            raise GenerationError(f"{name}#{node.pointer}: generated enum does not round-trip")
        if _yaml12.load("\n".join(f"- {render_scalar(v)}" for v in node.new_values)) != node.new_values:
            raise GenerationError(f"{name}#{node.pointer}: generated enum is ambiguous under YAML 1.2")
        resolve(expected, node.pointer)[node.enum_key] = node.new_values
    if out_doc != expected:
        raise GenerationError(f"{name}: generated document differs from master outside codeset enums")
    try:
        validate_openapi(out_doc)
    except Exception as e:  # noqa: BLE001
        raise GenerationError(f"{name}: generated document is not valid OpenAPI: {str(e).splitlines()[0]}") from None

    for ptr, key, values in untagged:
        rule = None
        for r in file_ignores:
            for pat in r["pointers"]:
                if fnmatch.fnmatchcase(ptr, pat):
                    rule = r
                    used_ignore_patterns.add((r["file"], pat))
                    break
            if rule:
                break
        entry = {"file": name, "pointer": ptr, "key": key, "values": values}
        if rule:
            report.ignored.append({**entry, "category": rule["category"], "reason": rule["reason"]})
        else:
            report.unclassified.append(entry)
    for r in file_ignores:
        for pat in r["pointers"]:
            if (r["file"], pat) not in used_ignore_patterns:
                report.warnings.append(f"{name}: ignoredEnums pattern `{pat}` matched no untagged enum")

    new_yaml = out_text.replace("\n", eol)
    new_json = json.dumps(out_doc, indent=2, ensure_ascii=False)
    changed = {"yaml": new_yaml != old_dist_yaml, "json": new_json != old_dist_json}
    report.files[name] = {"tagged": len(tagged), "changed": changed, "eol": "CRLF" if eol == "\r\n" else "LF"}
    return {dist_yaml: new_yaml.encode("utf-8"), dist_json: new_json.encode("utf-8")}


# --------------------------------------------------------------------------- report

def fmt_values(values, limit=12):
    if not values:
        return ""
    shown = ", ".join(f"`{v}`" for v in values[:limit])
    return shown + (f" … (+{len(values) - limit} more)" if len(values) > limit else "")


def count_cell(values):
    return f"**{len(values)}**: {fmt_values(values, 8)}" if values else ""


def diff_values(old, new):
    old_l = old or []
    added = [v for v in new if v not in old_l]
    removed = [v for v in old_l if v not in new]
    reordered = not added and not removed and list(old_l) != list(new)
    return added, removed, reordered


def build_report(report: Report, check: bool) -> str:
    m = report.meta
    out = ["# Codeset enum generation report", ""]
    out.append(f"- **Mode:** {'check (no files written)' if check else 'generate'}")
    out.append(f"- **Generated (UTC):** {m['timestamp']}")
    out.append(f"- **Codesets:** `{m['repo']}` @ `{m['commit']}` (branch `{m['branch']}`)")
    for name, s in m["sources"].items():
        src = s["source"]
        out.append(f"- **{name}:** {len(s['values'])} codes from {src['name']} {src['release']} (`{s['path']}`)")
    out.append("")

    if report.errors:
        out += ["## ❌ Errors", ""] + [f"- {e}" for e in report.errors] + [""]
        return "\n".join(out)

    out += ["## Files", "", "| File | Tagged enums | Dist YAML changed | Dist JSON changed | Line endings |", "|---|---|---|---|---|"]
    for name, f in report.files.items():
        out.append(f"| `{name}` | {f['tagged']} | {'**yes**' if f['changed']['yaml'] else 'no'} | "
                   f"{'**yes**' if f['changed']['json'] else 'no'} | {f['eol']} |")
    out.append("")

    dist_changes = []
    for n in report.nodes:
        added, removed, reordered = diff_values(n.dist_values, n.new_values)
        if n.dist_values is None or added or removed or reordered:
            dist_changes.append((n, added, removed, reordered))
    out += ["## Changes to dist enums", ""]
    if not dist_changes:
        out += ["No enum changes compared with the current dist files.", ""]
    else:
        out += ["| File | Pointer | Codeset | Added | Removed | Reordered |", "|---|---|---|---|---|---|"]
        for n, a, r, ro in dist_changes:
            new_note = " (enum added)" if n.dist_values is None else ""
            out.append(f"| `{n.file}` | `{n.pointer}`{new_note} | `{n.ref}` | {count_cell(a)} | "
                       f"{count_cell(r)} | {'yes' if ro else ''} |")
        out.append("")
        n_add = sum(1 for _, a, _, _ in dist_changes if a)
        n_rem = sum(1 for _, _, r, _ in dist_changes if r)
        n_ro = sum(1 for *_, ro in dist_changes if ro)
        out.insert(len(out) - len(dist_changes) - 3,
                   f"{len(dist_changes)} enums change: {n_add} with added values, {n_rem} with removed values, "
                   f"{n_ro} reordered only.\n")

    master_drift = [(n, *diff_values(n.master_values, n.new_values)) for n in report.nodes]
    master_drift = [d for d in master_drift if d[1] or d[2] or d[3]]
    out += ["<details><summary>Corrections relative to master enum values "
            f"({len(master_drift)} nodes)</summary>", ""]
    if master_drift:
        out += ["| File | Pointer | Codeset | Added | Removed | Reordered |", "|---|---|---|---|---|---|"]
        for n, a, r, ro in master_drift:
            out.append(f"| `{n.file}` | `{n.pointer}` | `{n.ref}` | {count_cell(a)} | "
                       f"{count_cell(r)} | {'yes' if ro else ''} |")
    else:
        out.append("Master enum values already match the codesets.")
    out += ["", "</details>", ""]

    exc_nodes = [n for n in report.nodes if n.exceptions]
    out += ["## Exceptions applied", ""]
    if exc_nodes:
        out += ["| File | Pointer | Codeset | Exception |", "|---|---|---|---|"]
        for n in exc_nodes:
            out.append(f"| `{n.file}` | `{n.pointer}` | `{n.ref}` | {'; '.join(n.exceptions)} |")
    else:
        out.append("None.")
    out.append("")

    out += ["## Ignored enums (left unchanged)", ""]
    cats = {}
    for i in report.ignored:
        cats.setdefault((i["category"], i["reason"]), []).append(i)
    for (cat, reason), items in cats.items():
        out += [f"<details><summary><b>{cat}</b>: {len(items)} enums. {reason}</summary>", ""]
        out += [f"- `{i['file']}` `{i['pointer']}` ({len(i['values'])} values)" for i in items]
        out += ["", "</details>", ""]

    if report.unclassified:
        out += ["## ⚠️ Unclassified untagged enums", "",
                "These enums have no `x-codeset-ref` and no `ignoredEnums` rule. Tag them or add an ignore rule.", ""]
        out += [f"- `{u['file']}` `{u['pointer']}`: {fmt_values(u['values'])}" for u in report.unclassified]
        out.append("")

    if report.warnings:
        out += ["## ⚠️ Warnings", ""] + [f"- {w}" for w in report.warnings] + [""]

    unused = sorted(set(report.codesets) - report.referenced)
    out += [f"<details><summary>Codesets not referenced by any master ({len(unused)})</summary>", ""]
    out += [f"- `{u}`" for u in unused] + ["", "</details>", ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- main

def write_all(outputs: dict):
    """Stage every output to a temp file, then swap them in; roll back on failure."""
    staged, originals, replaced = {}, {}, []
    try:
        for path, data in outputs.items():
            tmp = path.with_name(f".{path.name}.tmp")
            tmp.write_bytes(data)
            staged[path] = tmp
            originals[path] = path.read_bytes() if path.exists() else None
        for path, tmp in staged.items():
            os.replace(tmp, path)
            replaced.append(path)
    except OSError:
        for path in replaced:
            if originals[path] is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(originals[path])
        raise
    finally:
        for tmp in staged.values():
            tmp.unlink(missing_ok=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="do not write; exit 1 if dist is out of date")
    ap.add_argument("--codesets-dir", help="local directory containing the codeset CSVs")
    ap.add_argument("--report", help="write the markdown report to this path")
    args = ap.parse_args(argv)

    report = Report()
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    src = cfg["codesetSource"]
    report.meta = {
        "timestamp": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ"),
        "repo": src["repository"], "branch": src["branch"], "commit": src["commit"], "sources": {},
    }
    try:
        sources = load_value_sources(cfg)
        report.meta["sources"] = sources
        codesets = load_codesets(cfg, args.codesets_dir, report)
        report.codesets = codesets
        known_files = {p.name for p in SOURCE_DIR.glob("*.yaml")}
        for key in ("exceptions", "ignoredEnums"):
            for e in cfg.get(key) or []:
                if e["file"] not in known_files:
                    raise GenerationError(f"{key}: unknown master file '{e['file']}'")
        outputs = {}
        for name in sorted(known_files):
            outputs.update(process_file(name, cfg, codesets, sources, report))
        # Only write once every file has generated and validated successfully.
        if not args.check:
            write_all(outputs)
    except (GenerationError, yaml.YAMLError, OSError, KeyError) as e:
        msg = str(e) if isinstance(e, GenerationError) else f"{type(e).__name__}: {e}"
        report.errors.append(msg)
        gh("error", msg)

    md = build_report(report, args.check)
    if args.report:
        Path(args.report).write_text(md + "\n", encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(md + "\n")
    print(md)

    for w in report.warnings:
        gh("warning", w)
    for u in report.unclassified:
        gh("warning", f"Unclassified untagged enum: {u['file']}#{u['pointer']}")

    if report.errors:
        return 2
    changed = any(f["changed"]["yaml"] or f["changed"]["json"] for f in report.files.values())
    if args.check and changed:
        print("\nDist files are out of date. Run: python scripts/codesets/generate.py", file=sys.stderr)
        gh("error", "Dist files are out of date with source/openapi and the pinned codesets.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
