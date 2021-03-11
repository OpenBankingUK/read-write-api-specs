# Read/Write Data API Specification

## Overview

This is the Open Banking API specifications repository.

## Releases

API specifications are tagged according to the revision they match e.g. the v3.1.7 revision be tagged as `v3.1.7`. This tag will form a Release. To retrieve the files for a given release be sure to use the appropriate URL, e.g.:

```https://github.com/OpenBankingUK/open-banking-specs/releases/tag/v3.1.7```

## Specifications in OpenAPI formats

This space contains Read/Write Data API Specifications in [OpenAPI](https://github.com/OAI/OpenAPI-Specification#the-openapi-specification) format.

### Account Information 

- [Swagger (OpenAPI 2.0) - YAML](./dist/swagger/account-info-swagger.yaml) 
- [Swagger (OpenAPI 2.0) - JSON](./dist/swagger/account-info-swagger.json)
- [OpenAPI 3.0 - YAML](./dist/openapi/account-info-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/account-info-openapi.json)

### Payment Initiation

- [Swagger (OpenAPI 2.0) - YAML](./dist/swagger/payment-initiation-swagger.yaml) 
- [Swagger (OpenAPI 2.0) - JSON](./dist/swagger/payment-initiation-swagger.json)
- [OpenAPI 3.0 - YAML](./dist/openapi/payment-initiation-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/payment-initiation-openapi.json)

### Confirmation of Funds

- [Swagger (OpenAPI 2.0) - YAML](./dist/swagger/confirmation-funds-swagger.yaml) 
- [Swagger (OpenAPI 2.0) - JSON](./dist/swagger/confirmation-funds-swagger.json)
- [OpenAPI 3.0 - YAML](./dist/openapi/confirmation-funds-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/confirmation-funds-openapi.json)

### Events API

- [Swagger (OpenAPI 2.0) - YAML](./dist/swagger/events-swagger.yaml) 
- [Swagger (OpenAPI 2.0) - JSON](./dist/swagger/events-swagger.json)
- [OpenAPI 3.0 - YAML](./dist/openapi/events-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/events-openapi.json)


### Event Notifications API (TPP Endpoint sample)

- [Swagger (OpenAPI 2.0) - YAML](./dist/swagger/event-notifications-swagger.yaml) 
- [Swagger (OpenAPI 2.0) - JSON](./dist/swagger/event-notifications-swagger.json)
- [OpenAPI 3.0 - YAML](./dist/openapi/event-notifications-openapi.yaml) 
- [OpenAPI 3.0 - JSON](./dist/openapi/event-notifications-openapi.json)

The currently published OpenAPI 3.0 files are results of automatic conversions from the 2.0 formats. These conversions produce verbose output where some object references are resolved and copied to their respective endpoints. Although these files are logicaly identical to their 2.0 counterparts, they are to be replaced by sanitised versions to improve their readability.
