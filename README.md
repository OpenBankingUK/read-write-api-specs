# Read/Write Data API Specification

## Overview

This is the Open Banking API specifications repository.

## Releases

API specifications will be tagged according to the revision they match e.g. the first version will be `v3.0-RC3`. This tag will form a Release. To retrieve the files for a given release be sure to use the appropriate URL, e.g.:

```https://github.com/OpenBankingUK/open-banking-specs/releases/tag/v3.0-RC3```

## APIs

There are two ways to access this collection API Specifications.

The files for each specification, are grouped into format specific folders, that means as a consumer, if you are always interested in consuming OpenApi format only, then you can find all specifications in one directory `dist/openapi` and ignore orthers, similarly `dist/swagger` etc.

Alternatively following table provides another view, which lists OBIE R/W functional API resources, and the corrresponding files in different formats.

|API|Formats|
|---|---|
|Account Information|- [Open API - Flattened JSON](../read-write-api-specs/dist/openapi-flattened/account-info-openapi-flattened.json)<BR/>- [Open API - JSON](./dist/openapi/account-info-openapi.json)<BR/>- [Open API - YAML](./dist/openapi/account-info-openapi.yaml)<BR/>- [Swagger - Flattened JSON](dist/swagger-flattened/account-info-swagger-flattened.json)<BR/>- [Swagger - JSON](./dist/swagger/account-info-swagger.json)<BR/>- [Swagger - YAML](./dist/swagger/account-info-swagger.yaml)|
|Payment Initiation|- [Open API - Flattened JSON](./dist/openapi-flattened/payment-initiation-openapi-flattened.json)<BR/>- [Open API - JSON](./dist/openapi/payment-initiation-openapi.json)<BR/>- [Open API - YAML](./dist/openapi/payment-initiation-openapi.yaml)<BR/>- [Swagger - Flattened JSON](./dist/swagger-flattened/payment-initiation-swagger-flattened.json)<BR/>- [Swagger - JSON](./dist/swagger/payment-initiation-swagger.json)<BR/>- [Swagger - YAML](./dist/swagger/payment-initiation-swagger.yaml)|
|Confirmation of Funds|- [Open API - Flattened JSON](./dist/openapi-flattened/confirmation-funds-openapi-flattened.json)<BR/>- [Open API - JSON](./dist/openapi/confirmation-funds-openapi.json)<BR/>- [Open API - YAML](./dist/openapi/confirmation-funds-openapi.yaml)<BR/>- [Swagger - Flattened JSON](./dist/swagger-flattened/confirmation-funds-swagger-flattened.json)<BR/>- [Swagger - JSON](./dist/swagger/confirmation-funds-swagger.json)<BR/>- [Swagger - YAML](./dist/swagger/confirmation-funds-swagger.yaml)|
|Events API (Combines Events Subscriptions and Polling)|- [Open API - Flattened JSON](./dist/openapi-flattened/events-openapi-flattened.json)<BR/>- [Open API - JSON](./dist/openapi/events-openapi.json)<BR/>- [Open API - YAML](./dist/openapi/events-openapi.yaml)<BR/>- [Swagger - Flattened JSON](./dist/swagger-flattened/events-swagger-flattened.json)<BR/>- [Swagger - JSON](./dist/swagger/events-swagger.json)<BR/>- [Swagger - YAML](./dist/swagger/events-swagger.yaml)|
|`Event Subscription`* (use **events** instead)|- [Open API - Flattened JSON](./dist/openapi-flattened/event-subscriptions-openapi-flattened.json)<BR/>- [Open API - JSON](./dist/openapi/event-subscriptions-openapi.json)<BR/>- [Open API - YAML](./dist/openapi/event-subscriptions-openapi.yaml)<BR/>- [Swagger - Flattened JSON](./dist/swagger-flattened/event-subscriptions-swagger-flattened.json)<BR/>- [Swagger - JSON](./dist/swagger/event-subscriptions-swagger.json)<BR/>- [Swagger - YAML](./dist/swagger/event-subscriptions-swagger.yaml)|
|`Aggregated Polling`* (use **events** instead)|- [Open API - Flattened JSON](./dist/openapi-flattened/aggregated-polling-openapi-flattened.json)<BR/>- [Open API - JSON](./dist/openapi/aggregated-polling-openapi.json)<BR/>- [Open API - YAML](./dist/openapi/aggregated-polling-openapi.yaml)<BR/>- [Swagger - Flattened JSON](./dist/swagger-flattened/aggregated-polling-swagger-flattened.json)<BR/>- [Swagger - JSON](./dist/swagger/aggregated-polling-swagger.json)<BR/>- [Swagger - YAML](./dist/swagger/aggregated-polling-swagger.yaml)|
|`Callback-urls`* (use **events** instead)|- [Open API - Flattened JSON](./dist/openapi-flattened/callback-urls-openapi-flattened.json)<BR/>- [Open API - JSON](./dist/openapi/callback-urls-openapi.json)<BR/>- [Open API - YAML](./dist/openapi/callback-urls-openapi.yaml)<BR/>- [Swagger - Flattened JSON](./dist/swagger-flattened/callback-urls-swagger-flattened.json)<BR/>- [Swagger - JSON](./dist/swagger/callback-urls-swagger.json)<BR/>- [Swagger - YAML](./dist/swagger/callback-urls-swagger.yaml)|
|Event Notifications API (TPP Endpoint sample)|- [Open API - Flattened JSON](./dist/openapi-flattened/event-notifications-openapi-flattened.json)<BR/>- [Open API - JSON](./dist/openapi/event-notifications-openapi.json)<BR/>- [Open API - YAML](./dist/openapi/event-notifications-openapi.yaml)<BR/>- [Swagger - Flattened JSON](./dist/swagger-flattened/event-notifications-swagger-flattened.json)<BR/>- [Swagger - JSON](./dist/swagger/event-notifications-swagger.json)<BR/>- [Swagger - YAML](./dist/swagger/event-notifications-swagger.yaml)|

`*` represents deprecated resources - maintained only for the backward compatibility reasons. Shall be dropped in the next minor/major version update.

