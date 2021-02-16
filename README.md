# Read/Write Data API Specification

## Overview

This is the Open Banking API specifications repository.

## Releases

API specifications are tagged according to the revision they match e.g. the v3.1.7 revision be tagged as `v3.1.7`. This tag will form a Release. To retrieve the files for a given release be sure to use the appropriate URL, e.g.:

```https://github.com/OpenBankingUK/open-banking-specs/releases/tag/v3.1.7```

## Specifications in OpenAPI formats

This space contains Read/Write Data API Specifications in [OpenAPI](https://github.com/OAI/OpenAPI-Specification#the-openapi-specification) format.

- Account Information 
    * [Swagger (Open API 2.0)](./dist/swagger/account-info-swagger.yaml) 
    * [Open API 3.0](./dist/swagger/account-info-swagger-openapi-3.json)
- Payment Initiation
    - [Swagger (Open API 2.0)](./dist/swagger/payment-initiation-swagger.yaml)
    - [Open API 3.0](./dist/swagger/payment-initiation-swagger-openapi-3.json)
- Confirmation of Funds
    - [Swagger (Open API 2.0)](./dist/swagger/confirmation-funds-swagger.yaml)
    - [Open API 3.0](./dist/swagger/confirmation-funds-swagger-openapi-3.json)
- Events API
    - [Swagger (Open API 2.0)](./dist/swagger/events-swagger.yaml)
    - [Open API 3.0](./dist/swagger/events-swagger-openapi-3.json)
- Event Notifications API (TPP Endpoint sample)
    - [Swagger (Open API 2.0)](./dist/swagger/event-notifications-swagger.yaml) 
    - [Open API 3.0](./dist/swagger/event-notifications-swagger-openapi-3.json)

The currently published OpenAPI 3.0 files are results of automatic conversions from the 2.0 formats. These conversions produce verbose output where some object references are resolved and copied to their respective endpoints. Although these files are logicaly identical to their 2.0 counterparts, they are to be replaced by sanitised versions to improve their readability.
