# Read/Write Data API Specification

## Overview

This is the Open Banking API specifications repository.

## Releases


API specifications are tagged according to the revision they match e.g. the v4.0.0 revision will be tagged as `v4.0.0`. 
This tag will form a Release. To retrieve the files for a given release be sure to use the appropriate URL, e.g.:

```https://github.com/OpenBankingUK/open-banking-specs/releases/tag/v4.0.0```

## Specifications in OpenAPI formats

This space contains Read/Write Data API Specifications in 
[OpenAPI](https://github.com/OAI/OpenAPI-Specification#the-openapi-specification) format.

### Source (master) files

The files in [`source/openapi/`](./source/openapi/) are the master OpenAPI files for the Account Information, Payment Initiation, Confirmation of Funds and VRP profiles. Enums backed by an Open Banking codeset carry an `x-codeset-ref` (e.g. `OB_Internal_CodeSet/OBInternalAuthorisation1Code` or `ISO_External_CodeSet/ExternalPurpose1Code`) referencing the [External_Internal_CodeSets](https://github.com/OpenBankingUK/External_Internal_CodeSets) CSVs. The pinned codeset version and approved exceptions are in [`source/codeset-config.yaml`](./source/codeset-config.yaml).

The configuration also records an interim NCC expansion exception for the planned generator: replace `UK.OBIE.NCC.[ISO3166-aplha2-CountryCode]` with concrete values such as `UK.OBIE.NCC.GB`, using all officially assigned ISO 3166-1 alpha-2 country codes (including territories), while retaining `UK.OBIE.BICFI`. Reserved, withdrawn and user-assigned codes are excluded. The generator must use a pinned, versioned country list and apply this consistently to the AIS, PIS and VRP YAML/JSON outputs, preserving `x-namespaced-enum` rather than introducing a restrictive standard `enum`. This is a project workaround pending BA agreement, not confirmation that every country has a supported NCC scheme. Generator support and country-list selection are pending; no generated values have been changed yet.

### Account Information 

- [OpenAPI 3.0 - YAML](./dist/openapi/account-info-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/account-info-openapi.json)

### Payment Initiation

- [OpenAPI 3.0 - YAML](./dist/openapi/payment-initiation-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/payment-initiation-openapi.json)

### Confirmation of Funds

- [OpenAPI 3.0 - YAML](./dist/openapi/confirmation-funds-openapi.yaml)
- [OpenAPI 3.0 - JSON](./dist/openapi/confirmation-funds-openapi.json)

### VRP

- [OpenAPI 3.0 - YAML](./dist/openapi/vrp-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/vrp-openapi.json)

### Events API

- [OpenAPI 3.0 - YAML](./dist/openapi/events-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/events-openapi.json)

### Event Notifications API (TPP Endpoint sample)

- [OpenAPI 3.0 - YAML](./dist/openapi/event-notifications-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/event-notifications-openapi.json)

## License

Please refer to our [Open License](https://www.openbanking.org.uk/open-licence/).
