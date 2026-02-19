# Changelog

## Unreleased

### Fixed

- [CDRW-4136] Updated description of `OBExternalStatusReason1Code` to point to correct codeset name in AIS, PIS, CBPII, Events and VRP.

### Changed

- [CDRW-4136] Updated `ErrorCode` $ref in PIS to use `OBExternalStatusReason1Code`, matching rest of OpenAPI files (previously used `OBInternalErrorResponseError1Code`)
- [CDRW-4960] Updated endpoint summary descriptions and tags to align to usage.  This has resulted in `Payment Details` endpoints now being catagorised and listed with their payment type.

## v4.0.1 Release Candidate 2 - 2026-02-04

### Added

- Added `LWMH`, `LXMH`, & `TWYR` to `OBFrequency6Code` in AIS and PIS
- Added `SLCT` to `OBFrequency2` in AIS
- Added example values to `fromBookingDateTime`, `toBookingDateTime`, `fromStatementDateTime` and `toStatementDateTime`.

### Changed

- Updated example value in Error responses from `AC17` to `U001` in AIS and Events
- [CDRW-4948] Description for `OBReadStatement2/Data/Statement/StatementFee/RateType` changed to "This code indicates the specific type of fee rate (e.g., AER, EAR)"
- [CDRW-4948] Description for `OBReadStatement2/Data/Statement/StatementInterest/RateType` changed to "This code specifies the type of interest (e.g., BOE Base Rate, Fixed Rate, Gross)"
- [CDRW-4949] Updated descriptions for `fromBookingDateTime`, `toBookingDateTime`, `fromStatementDateTime` and `toStatementDateTime` to clarify that the timezone component **must not** be present, as per the Spec pages.

## v4.0.1 Release Candidate 1 - 2026-01-05

### Added

- Added `NONE` to `OBFrequency2` in AIS

### Removed

- Removed duplicate `WEEK` from `OBFrequency6Code` in PIS

## v4.0.1 Draft 1 - 2025-11-20

### Added

- Added clarity to file endpoint descriptions regarding ASPSPs specifying available content types. Affects
  `200AccountsAccountIdStatementsStatementIdFileRead`, `200FilePaymentConsentsConsentIdFileRead`, and
  `200FilePaymentsFilePaymentIdReportFileRead` (#195)
- Added a note to the top-level description of all swagger files about _conditional_ and _required_ fields (#209)
- `CRYP` added to `ExternalPurpose1Code`
- Added the following codes to `OBInternalStatementFeeType1Code`:
  - `UK.OBIE.InstalmentPlan`
  - `UK.OBIE.ReturnedPayment`
- Added the following codes to `OBInternalStatementInterestType1Code`:
  - `UK.OBIE.InstalmentPlan`
  - `UK.OBIE.MoneyTransfer`
- Added rate limit headers to all OpenAPI files
- Introduced a new `OBIntermediaryAgent` class which can appear up to 3 times in payload as `IntermediaryAgent1`,
  `IntermediaryAgent2` and `IntermediaryAgent3`.
  - This is used in `OBReadTransaction6/Data/Transaction`
  - Returning these fields requires use of the `ReadTransactionDetail` permission
- Deprecated `PaymentContextCode` values have been reintroduced to VRP and PIS OpenAPI files.
  - For the avoidance of doubt - these values __must not__ be accepted in a new consent and may only be accepted for 
    payment against a v3 VRP consent migrated to v4.
  - They may optionally be returned for a historical payment or consent migrated to v4 when using a `GET` request.
- `OBDomesticRefundAccount1` class definition added to the Payment Initiation and VRP OpenAPI files.
- `HTTP 422` has been added as a response code - this should be used when a duplicate Idempotency code is submitted.

### Changed

- Standardized all regex patterns in YAML files to be surrounded by single quotes and on a single line, for robustness,
  reliability and consistency (#192)
- Updated usages of `OBInternalConsentStatus1Code` in to use re-usable domain-specific consent status codes (#204).
  Changed codes:
  - Changed to `OBInternalConsentStatus2Code` in all PIS consents except File Payments
  - Changed to `OBInternalConsentStatus3Code` in only PIS File Payments consents
- Remap `ReferredDocumentAmount` from `Int32` to `OBActiveCurrencyAndAmount_SimpleType` in AIS, PIS, & VRP (#205)
- Updated usages of `ExternalPaymentTransactionStatus1Code` for PIS and VRP to use re-usable endpoint-specific payment
  status codes (#208). Codes changed:
  - `ExternalPaymentTransactionStatus1Code` used in Domestic Standing Orders and International Standing Orders
  - `ExternalPaymentTransactionStatus2Code` used in Domestic Scheduled Payments and International Scheduled Payments
  - `ExternalPaymentTransactionStatus3Code` used in Domestic Payments and International Payments
  - `ExternalPaymentTransactionStatus4Code` used in File Payments
  - `ExternalPaymentTransactionStatus5Code` used in Domestic VRP
- `Meta` and `Links` have been made conditional in the VRP OpenAPI file.
- VRP `OBCashAccountDebtorWithName` max length is increased from 70 to 350 characters and is no longer `mandatory`.
- Updated `ReferredDocumentInformation/LineDetails` string length to 2048 max characters.
- The `Refund` field in the Payment Initiation and VRP OpenAPI files has been updated to point to the newly added 
  `OBDomesticRefundAccount1` class.

### Removed

- Remove legacy v3 artefact `OBAddressTypeCode` from Account Information (#202)
- Removed `x-fapi-financial-id` from the Event Notifications OpenAPI file.
- `CANC` removed from VRP payment status enum list

### Fixed

- Fixed typo in `PointInTime` description from `CountPerSide` to `CountPerPeriod` in PIS (#194)
- Corrected description wording for `OBMandateRelatedInformation1/MandateIdentification` in PIS (#203)
- Fixed regex patterns to match the spec pages (#192):
  - Fixed missing `^` and `$` throughout PIS
  - Fixed `\` escaping in AIS
