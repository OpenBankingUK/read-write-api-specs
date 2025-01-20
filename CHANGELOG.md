# Changelog for v4.0 Update 4 - DRAFT

Please refer to the [Known Issues](https://openbanking.atlassian.net/wiki/spaces/DZ/pages/47546479/Known+Specification+Issues) for additional information on the fixes listed below.

## Changes

1. v40_KI27 - Add additional enum value to `ExternalEntryStatus1Code`  
    Addresses Known Issue v40_KI27 which adds `RJCT` to `ExternalEntryStatus1Code` to support backwards compatibility with previous versions of the spec.
2. v40_KI28 - Address issues with `MandateRelatedInformation`  
    Addresses Known Issue v40_KI28:
    * Updated `MandateRelatedInformation\Frequency\Type` to support complex patterns from v3 as well as 4 character ISO codes
    * Adds the following enumeration values to `OBFrequency6Code`:
        * WODL
        * FOWK
        * TWMH
        * FOMH
        * FIMH
        * ALMH
        * NONE
3. v40_KI29 - Restore `NumberOfPayments` to Standing Orders  
    Addresses Known Issue v40_KI29 which restores `NumberOfPayments` to the following areas:
    * `OBReadStandingOrder6/Data/StandingOrder/NumberOfPayments`
    * `OBDomesticStandingOrder3/NumberOfPayments`
    * `OBInternationalStandingOrder4/NumberOfPayments`
