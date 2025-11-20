# Changelog

## v4.0.1 - 2025-11-20

### Added

- Added clarity to file endpoint descriptions regarding ASPSPs specifying available content types. Affects 
  AIS `200AccountsAccountIdStatementsStatementIdFileRead`, `200FilePaymentConsentsConsentIdFileRead`, and
  `200FilePaymentsFilePaymentIdReportFileRead` (#195)

### Removed

- Remove legacy v3 artefact `OBAddressTypeCode` from Account Information (#202)

### Fixed

- Fixed typo in `PointInTime` description from `CountPerSide` to `CountPerPeriod` in PIS (#194)
- Corrected description wording for `OBMandateRelatedInformation1/MandateIdentification` in PIS (#203)
