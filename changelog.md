# Changelog

For v4.0.1 the following approach has been adopted for identifying changes:

- [Known Issues](https://openbanking.atlassian.net/wiki/spaces/DZ/pages/47546479/Known+Specification+Issues) - these are tagged with the KI identifier, e.g. [v40_KI45]
- [Change Requests](https://openbanking.atlassian.net/wiki/spaces/WOR/pages/3872948225/2025-09-11+EAG+for+v4.x.x+Standards+release+Workshop+4#Discussion-material) - these are tagged with the CR number used in the consultations, e.g. [CR4a]
- EAG/Consultation items - Items included in the consultations are tagged with an identifier representing the consultation period they were introduced, e.g. [v4.0.1 RC 1]
- Feedback remediation - Technical errata and other minor corrections identified by participants or OBL during the Advanced Information period for Release Candidates 1 and 2 with an appropriate identifier for internal OBL traceability e.g. [CDRW-5006]

**Consultations:**

- [v4.x.x Consultation 1](https://openbanking.atlassian.net/wiki/spaces/WOR/pages/3880550401/Feedback+-+V4.x.x+Consultation+1)
- [v4.0.1 Draft 1](https://openbanking.atlassian.net/wiki/spaces/WOR/pages/4096950276/Feedback+-+v4.0.1+Draft+1)
- [v4.0.1 Release Candidate 1](https://openbanking.atlassian.net/wiki/spaces/WOR/pages/4203282434/Feedback+-+v4.0.1+Release+Candidate+1)
- [v4.0.1 Release Candidate 2](https://openbanking.atlassian.net/wiki/spaces/WOR/pages/4309942273/Feedback+-+v4.0.1+Release+Candidate+2)

## v4.0.1-Update1 - TBD

### Added

- Added CBPII OpenAPI tags for `Funds Confirmation Consents` and `Funds Confirmations` to improve Swagger UI grouping and navigation.
- Added optional `x-jws-signature` request header support across all CBPII operations to align with the Open Banking spec pages/standard.
- Added optional `x-jws-signature` response header support across CBPII success and error responses to align with the Open Banking spec pages/standard.
- Added reusable CBPII OpenAPI examples for successful request/response payloads, key parameters, and error payloads.

### Changed

- Updated CBPII endpoint descriptions for consent creation, consent retrieval, consent deletion and funds confirmation creation to provide clearer behaviour and outcome detail.
- Standardised CBPII OpenAPI description formatting for consistency (single-line where suitable, `>-`/`|-` block scalar usage where appropriate, paragraph spacing, inline code formatting, and emphasised notes).
- Updated CBPII security scheme descriptions to align with Open Banking/FAPI context and clarify `Authorization` header usage.
- Updated `x-jws-signature` to be optional in CBPII request/response modelling to align with the Open Banking spec pages/standard.
- Updated CBPII enum descriptions to link directly to the relevant codeset CSV files.
- Refactored CBPII `OBInternalAccountIdentification4Code` into a reusable schema reference.
- Refactored CBPII Confirmation of Funds OpenAPI data dictionary schemas to use reusable component references aligned to the spec pages:
  - `OBFundsConfirmationConsent1/Data` now references `OBFundsConfirmationConsentData1`
  - `OBFundsConfirmationConsentResponse1/Data` now references `OBFundsConfirmationConsentDataResponse1`
  - `OBFundsConfirmation1/Data` now references `OBFundsConfirmationData1`
  - `OBFundsConfirmationResponse1/Data` now references `OBFundsConfirmationDataResponse1`
  - `OBFundsConfirmationConsent1/Data/DebtorAccount` and `OBFundsConfirmationConsentResponse1/Data/DebtorAccount` now reference `OBCashAccountDebtorWithName`
  - `OBFundsConfirmation1/Data/InstructedAmount` and `OBFundsConfirmationResponse1/Data/InstructedAmount` now reference `OBActiveOrHistoricCurrencyAndAmount`
  - `OBFundsConfirmation1/Data/InstructedAmount/Amount` and `OBFundsConfirmationResponse1/Data/InstructedAmount/Amount` now reference `OBActiveCurrencyAndAmount_SimpleType`
  - `OBFundsConfirmation1/Data/InstructedAmount/Currency` and `OBFundsConfirmationResponse1/Data/InstructedAmount/Currency` now reference `ActiveOrHistoricCurrencyCode`

### Removed

- Removed **unused** CBPII response/schema components `404Error` and `Identification_0`.
- Removed **unused** CBPII header parameter `x-idempotency-key` (CBPII has no idempotent endpoints).

## v4.0.1 - 2026-04-01

### Added

- [CDRW-5005] Added `CRYP` to `OBExternalPurpose1Code` in AIS to align with PIS, where `CRYP` (CryptoAssets) was already present as part of the CR4a change.
- [CDRW-5045] Updated all ASPSP endpoints with descriptions describing their use.
- [v40_KI45] Added `LWMH`, `LXMH`, & `TWYR` to `OBFrequency6Code` in AIS and PIS
- [v40_KI45] Added `SLCT` to `OBFrequency2` in AIS
- [CDRW-4937] Added example values to `fromBookingDateTime`, `toBookingDateTime`, `fromStatementDateTime` and `toStatementDateTime`.
- [v40_KI46] Added `NONE` to `OBFrequency2` in AIS
- [CDRW-4760] Added clarity to file endpoint descriptions regarding ASPSPs specifying available content types. Affects
  `200AccountsAccountIdStatementsStatementIdFileRead`, `200FilePaymentConsentsConsentIdFileRead`, and
  `200FilePaymentsFilePaymentIdReportFileRead` (#195)
- [CR7] Added a note to the top-level description of all swagger files about _conditional_ and _required_ fields (#209)
- [CR4a] `CRYP` added to `ExternalPurpose1Code`
- [CR1] Added the following codes to `OBInternalStatementFeeType1Code`:
  - `UK.OBIE.InstalmentPlan`
  - `UK.OBIE.ReturnedPayment`
- [CR1] Added the following codes to `OBInternalStatementInterestType1Code`:
  - `UK.OBIE.InstalmentPlan`
  - `UK.OBIE.MoneyTransfer`
- [v4.x.x Consultation 1] Added rate limit headers to all OpenAPI files
- [CR2] Introduced a new `OBIntermediaryAgent` class which can appear up to 3 times in payload as `IntermediaryAgent1`,
  `IntermediaryAgent2` and `IntermediaryAgent3`.
  - This is used in `OBReadTransaction6/Data/Transaction`
  - Returning these fields requires use of the `ReadTransactionDetail` permission
- [v40_KI25] Deprecated `PaymentContextCode` values have been reintroduced to VRP and PIS OpenAPI files.
  - For the avoidance of doubt - these values **must not** be accepted in a new consent and may only be accepted for payment against a v3 VRP consent migrated to v4.
  - They may optionally be returned for a historical payment or consent migrated to v4 when using a `GET` request.
- [v40_KI7] `OBDomesticRefundAccount1` class definition added to the Payment Initiation and VRP OpenAPI files.
- [v4.0.1 Draft 1] `HTTP 422` has been added as a response code - this should be used when a duplicate Idempotency code is submitted.

### Changed

- [CDRW-5046] Added missing enum values to `ExternalDocumentType1Code` in AIS: `AROI`, `BOLD`, `CMCN`, `SOAC`, `TSUT`, `USAR`, `VCHR`
- [CDRW-4136] Updated `ErrorCode` $ref name in PIS to use `OBExternalStatusReason1Code`, matching rest of OpenAPI files (previously used `OBInternalErrorResponseError1Code`)
- [CDRW-4960] Updated endpoint summaries and tags to align to usage.  This has resulted in `Payment Details` endpoints now being categorised and listed with their payment type.
- [CDRW-4909] Improved description formatting for `RateLimit-Policy`, `RateLimit`, and `x-client-id`, to match spec pages formatting.
- [v40_KI42] Updated location of `ExternalDocumentFormat1Code` to `ISO_External_Codeset` in description.
- [CDRW-5014] Updated example value in Error responses from `AC17` to `U001` in AIS and Events
- [v40_KI48] Description for `OBReadStatement2/Data/Statement/StatementFee/RateType` changed to "This code indicates the specific type of fee rate (e.g., AER, EAR)"
- [v40_KI48] Description for `OBReadStatement2/Data/Statement/StatementInterest/RateType` changed to "This code specifies the type of interest (e.g., BOE Base Rate, Fixed Rate, Gross)"
- [CDRW-4949] Updated descriptions for `fromBookingDateTime`, `toBookingDateTime`, `fromStatementDateTime` and `toStatementDateTime` to clarify that the timezone component **must not** be present, as per the Spec pages.
- [v40_KI30] Standardized all regex patterns in YAML files to be surrounded by single quotes and on a single line, for robustness, reliability and consistency (#192)
- [v4.0.1 Draft 1] Updated usages of `OBInternalConsentStatus1Code` in to use re-usable domain-specific consent status codes (#204).
  Changed codes:
  - Changed to `OBInternalConsentStatus2Code` in all PIS consents except File Payments
  - Changed to `OBInternalConsentStatus3Code` in only PIS File Payments consents
- [v40_KI36] Remap `ReferredDocumentAmount` from `Int32` to `OBActiveCurrencyAndAmount_SimpleType` in AIS, PIS, & VRP (#205)
- [v4.0.1 Draft 1] Updated usages of `ExternalPaymentTransactionStatus1Code` for PIS and VRP to use re-usable endpoint-specific payment
  status codes (#208). Codes changed:
  - `ExternalPaymentTransactionStatus1Code` used in Domestic Standing Orders and International Standing Orders
  - `ExternalPaymentTransactionStatus2Code` used in Domestic Scheduled Payments and International Scheduled Payments
  - `ExternalPaymentTransactionStatus3Code` used in Domestic Payments and International Payments
  - `ExternalPaymentTransactionStatus4Code` used in File Payments
  - `ExternalPaymentTransactionStatus5Code` used in Domestic VRP
- [v4.0.1 Draft 1] `Meta` and `Links` have been made conditional in the VRP OpenAPI file.
- [v40_KI5] VRP `OBCashAccountDebtorWithName` max length is increased from 70 to 350 characters and is no longer `mandatory`.
- [v4.0.1 Draft 1] Updated `ReferredDocumentInformation/LineDetails` string length to 2048 max characters.
- [v40_KI7] The `Refund` field in the Payment Initiation and VRP OpenAPI files has been updated to point to the newly added `OBDomesticRefundAccount1` class.

### Removed

- [CDRW-5012] Removed duplicate `WEEK` from `OBFrequency6Code` in PIS
- [CDRW-4765] Remove legacy v3 artefact `OBAddressTypeCode` from Account Information (#202)
- [CDRW-4878] Removed `x-fapi-financial-id` from the Event Notifications OpenAPI file.
- [v40_KI41] `CANC` removed from VRP payment status enum list

### Fixed

- [CDRW-4136] Updated description of `OBExternalStatusReason1Code` to point to correct codeset name in AIS, PIS, CBPII, Events and VRP.
- [CDRW-5043] Corrected typos and improved description clarity across all OpenAPI specification files:
  - Fixed double word "as as" to "as" in top-level description (AIS, CBPII, Events, PIS, VRP)
  - Corrected "dentification" to "Identification" in multiple field descriptions (AIS)
  - Fixed article usage: "an rate" to "a rate" (AIS), "an servicing" to "a servicing" (AIS, PIS, VRP), and "an Callback" to "a Callback" (Events)
  - Fixed spelling errors: "crebit" to "credit" (AIS), "memebership" to "membership" (AIS), "statments" to "statements" (AIS), "reefer" to "refer" (PIS), "lust" to "list" (VRP)
  - Corrected GitHub URL typo: "External_Interal_CodeSets" to "External_Internal_CodeSets" (Events)
  - Fixed whitespace artifacts in descriptions (removed escaped underscores) (Events)
  - Improved grammar: "AWAU and RJCT only can returned" to "Only AWAU and RJCT can be returned" (VRP)
  - Clarified wording: "can not" to "cannot" (VRP), "this include" to "this includes" (VRP)
- [CDRW-5053] - Updated rate limit + client ID header information in event-notifications-openapi (TPP endpoint for Event Notification API Specification) to be specific to TPPs and updated description on endpoint to describe use.
- [CDRW-4729] Fixed typo in `PointInTime` description from `CountPerSide` to `CountPerPeriod` in PIS (#194)
- [CDRW-4802] Corrected description wording for `OBMandateRelatedInformation1/MandateIdentification` in PIS (#203)
- [v40_KI30] Fixed regex patterns to match the spec pages (#192):
  - Fixed missing `^` and `$` throughout PIS
  - Fixed `\` escaping in AIS
