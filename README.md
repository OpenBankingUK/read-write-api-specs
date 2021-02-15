# Read/Write Data API Specification

## Overview

This is the Open Banking API specifications repository.

## Releases

API specifications are tagged according to the revision they match e.g. the v3.1.7 revision be tagged as `v3.1.7`. This tag will form a Release. To retrieve the files for a given release be sure to use the appropriate URL, e.g.:

```https://github.com/OpenBankingUK/open-banking-specs/releases/tag/v3.1.7```

## Specifications in OpenAPI format

This space contains Read/Write Data API Specifications in [OpenAPI](https://github.com/OAI/OpenAPI-Specification#the-openapi-specification) format.

### OpenAPI 2.0 Formats (Swagger)

- [Account Information](./dist/openapi/account-info-openapi.yaml)
- [Payment Initiation](./dist/openapi/payment-initiation-openapi.yaml)
- [Confirmation of Funds](./dist/openapi/confirmation-funds-openapi.yaml)
- [Events API](./dist/openapi/events-openapi.yaml)
- [Event Notifications API](./dist/openapi/event-notifications-openapi.yam) (TPP Endpoint sample)

### OpenAPI 3.0 Formats

The currently published OpenAPI 3.0 files are results of automatic conversions from the 2.0 formats. These conversions produce verbose output where some object references are resolved and copied to their respective endpoints. Although these files are logicaly identical to their 2.0 counterparts, they are to be replaced by sanitised versions to improve their readability.

- [Account Information](./dist/openapi/account-info-openapi.yaml)
- [Payment Initiation](./dist/openapi/payment-initiation-openapi.yaml)
- [Confirmation of Funds](./dist/openapi/confirmation-funds-openapi.yaml)
- [Events API](./dist/openapi/events-openapi.yaml)
- [Event Notifications API](./dist/openapi/event-notifications-openapi.yam) (TPP Endpoint sample)