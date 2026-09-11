# ASPSP OpenAPI `$ref` Compatibility Test

## What we need you to test

Open Banking specifications reuse schema components with `$ref`, but sometimes
need a different contextual `description` at each usage site. This test compares
two standards-compliant ways of expressing that requirement:

- **OpenAPI 3.0.0:** a contextual `description` with a one-item `allOf`
  containing the `$ref`;
- **OpenAPI 3.1.2:** a contextual `description` directly beside the schema
  `$ref`.

We want to understand whether each approach works throughout ASPSP toolchains,
including parsing, validation, documentation rendering, and code or model
generation. This is a focused interoperability test, not a test of complete
OpenAPI 3.0.0 or 3.1.2 conformance, and does not itself propose a production
specification change.

The results will help determine whether future Open Banking specifications
should continue using the OpenAPI 3.0.0 `allOf` pattern or move to OpenAPI
3.1.2 `$ref` siblings for contextual descriptions.

## Test artifacts

| Test | OpenAPI | Scope | Reference pattern | YAML | JSON |
|---|---|---|---|---|---|
| 1 | 3.0.0 | Complete Open Banking VRP specification | `description` with one-item `allOf` | [`vrp-openapi-3.0.0-allof.yaml`](./vrp-openapi-3.0.0-allof.yaml) | [`vrp-openapi-3.0.0-allof.json`](./vrp-openapi-3.0.0-allof.json) |
| 2 | 3.0.0 | Minimal `GET /hello` API | `description` with one-item `allOf` | [`hello-world-openapi-3.0.0-allof.yaml`](./hello-world-openapi-3.0.0-allof.yaml) | [`hello-world-openapi-3.0.0-allof.json`](./hello-world-openapi-3.0.0-allof.json) |
| 3 | 3.1.2 | Complete Open Banking VRP specification | Direct `$ref` and `description` siblings | [`vrp-openapi-3.1.2-ref-siblings.yaml`](./vrp-openapi-3.1.2-ref-siblings.yaml) | [`vrp-openapi-3.1.2-ref-siblings.json`](./vrp-openapi-3.1.2-ref-siblings.json) |
| 4 | 3.1.2 | Minimal `GET /hello` API | Direct `$ref` and `description` siblings | [`hello-world-openapi-3.1.2-ref-siblings.yaml`](./hello-world-openapi-3.1.2-ref-siblings.yaml) | [`hello-world-openapi-3.1.2-ref-siblings.json`](./hello-world-openapi-3.1.2-ref-siblings.json) |

The VRP artifacts are complete specifications intended to exercise normal
ASPSP processing. The Hello World artifacts isolate the reference pattern if a
failure in the larger VRP document is difficult to diagnose. The Hello World
files describe an API contract only; no live endpoint is provided.

Use either YAML or JSON, whichever your tooling normally consumes. They express
the same test and the serialization format is not part of this investigation.

## Minimum test request

Please test at least one matched pair so that the OpenAPI 3.0.0 and 3.1.2
results cover the same API scope:

- **Complete VRP pair:** tests 1 and 3; or
- **Minimal Hello World pair:** tests 2 and 4.

Where possible, test all four:

1. Start with the two minimal Hello World files to isolate support for each
   reference pattern.
2. Test the two complete VRP files through the same tooling to confirm that the
   result holds for a realistic Open Banking specification.

## Where to inspect the patterns

The locations below apply to both YAML and JSON.

### Tests 1 and 3: complete VRP specification

The same five schema properties use the 3.0.0 `allOf` pattern in test 1 and
the 3.1.2 `$ref` sibling pattern in test 3:

- `/components/schemas/OBReferredDocumentInformation/properties/RelatedDate`
- `/components/schemas/OBRegulatoryAuthority2/properties/CountryCode`
- `/components/schemas/OBStructuredRegulatoryReporting3/properties/Date`
- `/components/schemas/OBStructuredRegulatoryReporting3/properties/Country`
- `/components/schemas/OBStructuredRegulatoryReporting3/properties/Amount`

Test 1 expresses each usage like this:

```yaml
RelatedDate:
  description: Date associated with the referred document line.
  allOf:
    - $ref: '#/components/schemas/ISODateTime'
```

Test 3 expresses the equivalent usage like this:

```yaml
RelatedDate:
  description: Date associated with the referred document line.
  $ref: '#/components/schemas/ISODateTime'
```

### Tests 2 and 4: minimal Hello World API

Inspect the response schema at:

`/paths/~1hello/get/responses/200/content/application~1json/schema`

Test 2 uses:

```yaml
schema:
  description: The greeting returned specifically by GET /hello.
  allOf:
    - $ref: '#/components/schemas/HelloMessage'
```

Test 4 uses:

```yaml
schema:
  $ref: '#/components/schemas/HelloMessage'
  description: The greeting returned specifically by GET /hello.
```

Both files define `HelloMessage` as an object with a required string property
named `message` and include this example:

```json
{
  "message": "Hello, world!"
}
```

## How to test

Run each selected file through the way your organisation normally uses an Open
Banking API specification. This might be import, validation, documentation
rendering, code generation, or another process. You do not need to test
activities that are not part of your normal workflow.

We need three results for each test:

1. **Overall result:** Did the file work for your normal use?
2. **Contextual description:** Was the usage-specific description retained or
   displayed?
3. **Referenced schema:** Were the referenced type, properties, required
   fields, formats, and other constraints retained?

For Hello World, `message` should remain a required string and the usage-site
description should be `The greeting returned specifically by GET /hello.` For
VRP, inspect one or more of the five properties listed above.
