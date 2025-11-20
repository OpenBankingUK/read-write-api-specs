# Changelog

## v4.0.1 - 2025-11-20

### Added

- Added clarity to file endpoint descriptions regarding ASPSPs specifying available content types. Affects
  `200AccountsAccountIdStatementsStatementIdFileRead`, `200FilePaymentConsentsConsentIdFileRead`, and
  `200FilePaymentsFilePaymentIdReportFileRead` (#195)

### Changed

- Standardized all regex patterns in YAML files to be surrounded by single quotes and on a single line, for robustness,
  reliability and consistency (#192)

### Removed

- Remove legacy v3 artefact `OBAddressTypeCode` from Account Information (#202)

### Fixed

- Fixed typo in `PointInTime` description from `CountPerSide` to `CountPerPeriod` in PIS (#194)
- Corrected description wording for `OBMandateRelatedInformation1/MandateIdentification` in PIS (#203)
- Fixed regex patterns to match the spec pages (#192):
  - Fixed missing `^` and `$` throughout PIS
  - Fixed `\` escaping in AIS