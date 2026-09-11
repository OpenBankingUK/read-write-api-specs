# OpenAPI `$ref` Sibling Compatibility POC

## Purpose

This proof of concept tests two standards-compliant ways to add a contextual
description where a reusable schema is referenced:

- OpenAPI 3.0.0 uses a Schema Object with a contextual `description` and a
  one-item `allOf` containing the `$ref`.
- OpenAPI 3.1.2 uses a contextual `description` directly beside the schema
  `$ref`, using JSON Schema Draft 2020-12 semantics.

The tests are intended to show which approach participating ASPSP toolchains
can parse and use. They do not propose a production specification change.

## Test artifacts

| Test | OpenAPI | Scope | Reference pattern | YAML | JSON |
|---|---|---|---|---|---|
| 1 | 3.0.0 | Complete OBL VRP specification | `description` with one-item `allOf` | [`vrp-openapi-3.0.0-allof.yaml`](./vrp-openapi-3.0.0-allof.yaml) | [`vrp-openapi-3.0.0-allof.json`](./vrp-openapi-3.0.0-allof.json) |
| 2 | 3.0.0 | Minimal `GET /hello` API | `description` with one-item `allOf` | [`hello-world-openapi-3.0.0-allof.yaml`](./hello-world-openapi-3.0.0-allof.yaml) | [`hello-world-openapi-3.0.0-allof.json`](./hello-world-openapi-3.0.0-allof.json) |
| 3 | 3.1.2 | Complete OBL VRP specification | Direct `$ref` and `description` siblings | [`vrp-openapi-3.1.2-ref-siblings.yaml`](./vrp-openapi-3.1.2-ref-siblings.yaml) | [`vrp-openapi-3.1.2-ref-siblings.json`](./vrp-openapi-3.1.2-ref-siblings.json) |
| 4 | 3.1.2 | Minimal `GET /hello` API | Direct `$ref` and `description` siblings | [`hello-world-openapi-3.1.2-ref-siblings.yaml`](./hello-world-openapi-3.1.2-ref-siblings.yaml) | [`hello-world-openapi-3.1.2-ref-siblings.json`](./hello-world-openapi-3.1.2-ref-siblings.json) |

The complete VRP cases exercise five contextual descriptions:

- `OBReferredDocumentInformation.RelatedDate`
- `OBRegulatoryAuthority2.CountryCode`
- `OBStructuredRegulatoryReporting3.Date`
- `OBStructuredRegulatoryReporting3.Country`
- `OBStructuredRegulatoryReporting3.Amount`

## Where to find the test patterns

The expected `$ref` and `description` siblings can be found at these locations
in the OpenAPI 3.1.2 artifacts:

| Artifact | Schema location |
|---|---|
| VRP | `components.schemas.OBReferredDocumentInformation.properties.RelatedDate` |
| VRP | `components.schemas.OBRegulatoryAuthority2.properties.CountryCode` |
| VRP | `components.schemas.OBStructuredRegulatoryReporting3.properties.Date` |
| VRP | `components.schemas.OBStructuredRegulatoryReporting3.properties.Country` |
| VRP | `components.schemas.OBStructuredRegulatoryReporting3.properties.Amount` |
| Hello World | `paths./hello.get.responses.200.content.application/json.schema` |

For example, the VRP artifact contains:

```yaml
RelatedDate:
  description: Date associated with the referred document line.
  $ref: '#/components/schemas/ISODateTime'
```

The OpenAPI 3.0.0 artifacts use the equivalent `description` and one-item
`allOf` pattern at the same locations:

```yaml
RelatedDate:
  description: Date associated with the referred document line.
  allOf:
    - $ref: '#/components/schemas/ISODateTime'
```

## Requested testing

Please test at least:

1. One OpenAPI 3.0.0 artifact: test 1 or test 2.
2. One OpenAPI 3.1.2 artifact: test 3 or test 4.

Use whichever serialization your system normally consumes. Testing both YAML
and JSON is useful if your toolchain handles them through different code paths.

For each selected artifact, record whether your system can:

- import or parse the document without an error;
- validate the document;
- generate models, client code, server stubs, or other normal outputs;
- render the contextual description at the reference usage site;
- preserve the referenced schema's constraints and properties; and
- process the `GET /hello` response where the dummy API is used.

For the dummy APIs, the expected response body is:

```json
{
  "message": "Hello, world!"
}
```

The contextual description at the response schema usage site is:
`The greeting returned specifically by GET /hello.`

## Results

Copy one row per tested artifact and include exact error messages in the notes
where possible.

| Participant / system | Tool and version | Test | Format | Import / parse | Validation | Generation or rendering | Contextual description retained | Referenced constraints retained | Notes / errors |
|---|---|---:|---|---|---|---|---|---|---|
|  |  |  | YAML / JSON | Pass / Fail | Pass / Fail / N/A | Pass / Fail / N/A | Yes / No / N/A | Yes / No / N/A |  |

## Interpretation

- If test 1 or 2 succeeds, the system supports the OAS 3.0.0 `allOf` pattern
  used to attach a contextual description to a referenced schema.
- If test 3 or 4 succeeds, the system supports OAS 3.1.2 schema `$ref`
  siblings for this use case.
- A parser accepting a file does not by itself prove full support. Rendering,
  generation, and preservation of the referenced schema should be reported
  separately.

The description is an annotation. This POC tests whether tooling retains and
exposes the contextual annotation; it does not assume that every tool will
display it in the same place or treat it as replacing the reusable component's
description.
