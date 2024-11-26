# Changelog for v4.0 Release 3 - DRAFT

Please refer to the [Known Issues](https://openbanking.atlassian.net/wiki/spaces/DZ/pages/47546479/Known+Specification+Issues) for additional information on the fixes listed below.

## Changes

1. v40_KI16 - Multi-auth status updated to AWAF
    + Addresses Known Issue v40_KI16 where File and International payments had AWAU incorrectly listed in the MultiAuthorisation status enum.
2. v40_KI18 - Add missing RCVD value to OBWriteDomesticResponse5
    + Addresses Known Issue v40_KI18 where RCVD was missing from OBWriteDomesticResponse5 Status enum.
3. v40_KI19 - Adds missing dash in phone number examples
    + Addresses Known Issue v40_KI19 where the dash "-" is missing from the example phone numbers.
4. v40_KI22 - Update File Payment FileType enum
    + Addresses Known Issue v40_KI22 where `UK.OBIE.PaymentInitiation.4.0` was missing from File Payments `FileType` enumeration.  This replaces `UK.OBIE.PaymentInitiation.3.1`
5. v40_KI24 - Update File Payments OBWriteFile2 object
    + Addresses Known Issue v40_KI24 where `OBWriteFile2` was missing `CredtorAgent` from the `Initiation` object and `UltimateDebtor` referenced the `UltimateCreditor` schema.
