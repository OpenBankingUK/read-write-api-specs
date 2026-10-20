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

**Edit the masters, not `dist/`.** The AIS, PIS, CBPII and VRP files in `dist/openapi/` are generated from the masters by [`scripts/codesets/generate.py`](./scripts/codesets/generate.py). Every `x-codeset-ref` enum is replaced with the codeset's `Code Value`s in CSV order, the approved exceptions are applied, and everything else is copied unchanged. The `x-codeset-ref` keys stay in the masters only and are removed from `dist/`. The JSON files are regenerated from the YAML. The generator fails without writing anything if a reference doesn't resolve, an exception doesn't match, or the output isn't valid OpenAPI. Enums without `x-codeset-ref` are left unchanged and must match an `ignoredEnums` rule in the config; otherwise they're reported as unclassified.

The [Codeset enums workflow](./.github/workflows/codeset-enums.yml) runs on pull requests that touch `source/`, `dist/openapi/`, or `scripts/codesets/`. For branches in this repository it commits the regenerated dist files back to the PR branch for review. For forks it only checks that dist is up to date. Its report (changed enums, exceptions applied, ignored enums and warnings) is shown in the job summary and uploaded as the `codeset-report` artifact. To run it locally:

```sh
pip install -r scripts/codesets/requirements.txt
python scripts/codesets/generate.py            # regenerate dist/openapi
python scripts/codesets/generate.py --check    # exit 1 if dist is out of date
```

Interim NCC exception: `UK.OBIE.NCC.[ISO3166-aplha2-CountryCode]` is replaced with concrete values such as `UK.OBIE.NCC.GB` for every officially assigned ISO 3166-1 alpha-2 code (countries and territories), while `UK.OBIE.BICFI` and the `x-namespaced-enum` key are kept. The country list is vendored and pinned in [`scripts/codesets/data/iso3166-1-alpha2.json`](./scripts/codesets/data/iso3166-1-alpha2.json) (Debian `iso-codes` v4.20.1). This is a project workaround pending BA agreement. It does not confirm that every country has a supported NCC scheme.

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
