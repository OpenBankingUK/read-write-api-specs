# Changelog for v4.0 Update 5 DRAFT

Please refer to the [Known Issues](https://openbanking.atlassian.net/wiki/spaces/DZ/pages/47546479/Known+Specification+Issues) for additional information on the fixes listed below.

## [v4.0 Update 5 DRAFT]

### Added

- Added reference to Open License in README.md (#191).
- Added DCSV to OBFileFormat schema in account-info-openapi. This address v40_KI42

### Changed

- v40_KI34 - Update regex for LEI in PIS & VRP  
  - Addresses v40_KI34 which aligns the PIS regex for LEI to the spec pages and updates the VRP swagger to include the regex & example.
- Updated Payment Status enums to match Spec pages.
  - Some payment status codes were present on the Spec pages but not in the swagger.
 
### Fixed

- Fixed VRP PATCH operation description and schema.
  - The description was appearing in the `format` field and has been moved to the correct `description` field. Additonally the request body schemea has been updated to fully reflect [RFC 6902](https://datatracker.ietf.org/doc/html/rfc6902).
- Corrected a regex typo in AIS `OB_CodeMnemonic` (#189). Related to v40_KI30.
