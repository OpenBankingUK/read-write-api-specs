# Codeset mapping report — Phase 1 (v4.0.1-Update1)

Generated 2026-10-20 11:10 UTC. Codeset source: `OpenBankingUK/External_Internal_CodeSets` @ `main` / `fd33a35d71403e1d62ed9a3827ecbce9c46a207f`.

Master files: `source/openapi/` (copies of `dist/openapi/` with `x-codeset-ref` added — no enum values changed). This report lists **issues and ignored items only**; nodes whose enum already matches its codeset exactly are not listed.

## Summary

| File | Enum nodes | Tagged | Tagged with discrepancies | Ignored (product) | Ignored (orphan) | Ignored (non-codeset) |
|---|---|---|---|---|---|---|
| `account-info-openapi.yaml` | 192 | 56 | 7 | 135 | 1 | 0 |
| `confirmation-funds-openapi.yaml` | 3 | 3 | 0 | 0 | 0 | 0 |
| `payment-initiation-openapi.yaml` | 90 | 89 | 12 | 0 | 1 | 0 |
| `vrp-openapi.yaml` | 31 | 24 | 1 | 0 | 3 | 4 |

## 1. Enum values that differ from the codeset

Missing values are in the CSV but absent from the spec (they will be **added** at generation); extra values are in the spec but not in the CSV (they will be **removed** unless an exception is approved).

| File | Node (JSON pointer) | x-codeset-ref | Missing from spec | Extra in spec | Notes |
|---|---|---|---|---|---|
| account-info | `/components/schemas/OBExternalBalanceSubType1Code` | `ISO_External_CodeSet/ExternalBalanceSubType1Code` | ADJT, BLCK, BLKD, DLOD, EAST, FCOL, FCOU, FORC, FUND, INTM, LRLD, NOTE, PDNG, PIPO, PRAV, RESV, SCOL, SCOU, THRE | — |  |
| account-info | `/components/schemas/OBInternalFinancialInstitutionIdentification4Code` | `OB_Internal_CodeSet/OBInternalFinancialInstitutionIdentification4Code` | UK.OBIE.NCC.[ISO3166-aplha2-CountryCode] | — | CSV value is a pattern/placeholder, not a literal enum value — needs decision |
| account-info | `/components/schemas/OBReadBalance1/properties/Data/properties/Balance/items/properties/Amount/properties/SubType` | `ISO_External_CodeSet/ExternalBalanceSubType1Code` | ADJT, BLCK, BLKD, DLOD, EAST, FCOL, FCOU, FORC, FUND, INTM, LRLD, NOTE, PDNG, PIPO, PRAV, RESV, SCOL, SCOU, THRE | — |  |
| account-info | `/components/schemas/OBReadBalance1/properties/Data/properties/Balance/items/properties/LocalAmount/properties/SubType` | `ISO_External_CodeSet/ExternalBalanceSubType1Code` | ADJT, BLCK, BLKD, DLOD, EAST, FCOL, FCOU, FORC, FUND, INTM, LRLD, NOTE, PDNG, PIPO, PRAV, RESV, SCOL, SCOU, THRE | — |  |
| account-info | `/components/schemas/OBStatement2/properties/StatementAmount/items/properties/Amount/properties/SubType` | `ISO_External_CodeSet/ExternalBalanceSubType1Code` | ADJT, BLCK, BLKD, DLOD, EAST, FCOL, FCOU, FORC, FUND, INTM, LRLD, NOTE, PDNG, PIPO, PRAV, RESV, SCOL, SCOU, THRE | — |  |
| account-info | `/components/schemas/OBStatement2/properties/StatementAmount/items/properties/LocalAmount/properties/SubType` | `ISO_External_CodeSet/ExternalBalanceSubType1Code` | ADJT, BLCK, BLKD, DLOD, EAST, FCOL, FCOU, FORC, FUND, INTM, LRLD, NOTE, PDNG, PIPO, PRAV, RESV, SCOL, SCOU, THRE | — |  |
| account-info | `/components/schemas/OBStatement2Detail/properties/StatementAmount/items/properties/LocalAmount/properties/SubType` | `ISO_External_CodeSet/ExternalBalanceSubType1Code` | ADJT, BLCK, BLKD, DLOD, EAST, FCOL, FCOU, FORC, FUND, INTM, LRLD, NOTE, PDNG, PIPO, PRAV, RESV, SCOL, SCOU, THRE | — |  |
| payment-initiation | `/components/schemas/ExternalDocumentType1Code` | `ISO_External_CodeSet/ExternalDocumentType1Code` | USAR, AROI, BOLD, CMCN, SOAC, TSUT, VCHR | — |  |
| payment-initiation | `/components/schemas/OBInternalFinancialInstitutionIdentification4Code` | `OB_Internal_CodeSet/OBInternalFinancialInstitutionIdentification4Code` | UK.OBIE.NCC.[ISO3166-aplha2-CountryCode] | — | CSV value is a pattern/placeholder, not a literal enum value — needs decision |
| payment-initiation | `/components/schemas/OBInternalPaymentChargeType1Code` | `OB_Internal_CodeSet/OBInternalPaymentChargeType1Code` | UK.OBIE.BalanceTransferOut, UK.OBIE.MoneyTransferOut | — |  |
| payment-initiation | `/components/schemas/OBWriteDomesticStandingOrderConsentResponse6/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| payment-initiation | `/components/schemas/OBWriteFileConsent3/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| payment-initiation | `/components/schemas/OBWriteFileConsentResponse4/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| payment-initiation | `/components/schemas/OBWriteInternationalConsent5/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| payment-initiation | `/components/schemas/OBWriteInternationalConsentResponse6/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| payment-initiation | `/components/schemas/OBWriteInternationalScheduledConsent5/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| payment-initiation | `/components/schemas/OBWriteInternationalScheduledConsentResponse6/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| payment-initiation | `/components/schemas/OBWriteInternationalStandingOrderConsent6/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| payment-initiation | `/components/schemas/OBWriteInternationalStandingOrderConsentResponse7/properties/Data/properties/Authorisation/properties/AuthorisationType` | `OB_Internal_CodeSet/OBInternalAuthorisation1Code` | Multiple | — |  |
| vrp | `/components/schemas/OBInternalFinancialInstitutionIdentification4Code` | `OB_Internal_CodeSet/OBInternalFinancialInstitutionIdentification4Code` | UK.OBIE.NCC.[ISO3166-aplha2-CountryCode] | — | CSV value is a pattern/placeholder, not a literal enum value — needs decision |

### Approved exceptions (from `source/codeset-config.yaml`)

- `payment-initiation-openapi.yaml` `/components/schemas/OBRisk1/properties/PaymentContextCode` — retains BillPayment, EcommerceGoods, EcommerceServices, Other, PartyToParty, PispPayee (deprecated). No other discrepancies found on this node.
- `vrp-openapi.yaml` `/components/schemas/OBRisk1/properties/PaymentContextCode` — retains BillPayment, EcommerceGoods, EcommerceServices, Other, PartyToParty, PispPayee (deprecated). No other discrepancies found on this node.

## 2. Naming / reference issues

Descriptions or schema names that reference a codeset name which does not exist in the CSVs, or differs from the mapped codeset.

| File | Node | Text references | Mapped to | Issue |
|---|---|---|---|---|
| account-info | `OBBalanceType1Code` | schema name `OBBalanceType1Code` | `ExternalBalanceType1Code` | schema name differs from codeset name (informational) |
| account-info | `OBExternalMandateClassification1Code` | `OBExternalClassification1Code` | `OBExternalMandateClassification1Code` | name not in any CSV |
| account-info | `OBCommunicationMethod` | schema name `OBCommunicationMethod` | `OBExternalCommunicationMethod2Code` | schema name differs from codeset name (informational) |
| account-info | `OBCreditDebitCode_0` | schema name `OBCreditDebitCode_0` | `OBInternalCreditDebitCode` | schema name differs from codeset name (informational) |
| account-info | `OBCreditDebitCode_1` | schema name `OBCreditDebitCode_1` | `OBInternalCreditDebitCode` | schema name differs from codeset name (informational) |
| account-info | `OBCreditDebitCode_2` | schema name `OBCreditDebitCode_2` | `OBInternalCreditDebitCode` | schema name differs from codeset name (informational) |
| account-info | `OBExternalAccountSubType1Code` | schema name `OBExternalAccountSubType1Code` | `OBExternalCashAccountType1Code` | schema name differs from codeset name (informational) |
| account-info | `OBExternalBalanceSubType1Code` | schema name `OBExternalBalanceSubType1Code` | `ExternalBalanceSubType1Code` | schema name differs from codeset name (informational) |
| account-info | `OBExternalPurpose1Code` | schema name `OBExternalPurpose1Code` | `ExternalPurpose1Code` | schema name differs from codeset name (informational) |
| account-info | `OBFrequency2` | schema name `OBFrequency2` | `OBFrequency2Code` | schema name differs from codeset name (informational) |
| account-info | `OBFileFormat` | schema name `OBFileFormat` | `ExternalDocumentFormat1Code` | schema name differs from codeset name (informational) |
| vrp | `OBExternalCreditorReferenceType1Code` | schema name `OBExternalCreditorReferenceType1Code` | `ExternalCreditorReferenceType1Code` | schema name differs from codeset name (informational) |
| vrp | `OBExternalAccountType1Code` | schema name `OBExternalAccountType1Code` | `OBInternalAccountType1Code` | schema name differs from codeset name (informational) |

## 3. Ignored — codeset fields without an enum list (string only)

These reference a codeset in their description but have no `enum`/`x-namespaced-enum`. Left untouched and untagged as agreed.

| File | Node | Codeset referenced |
|---|---|---|
| account-info | `OBExternalStatusReason1Code` | `OBExternalStatusReason1Code` |
| account-info | `OBStatusReason.StatusReasonCode` | `OBExternalStatusReason1Code` |
| confirmation-funds | `OBExternalStatusReason1Code` | `OBExternalStatusReason1Code` |
| confirmation-funds | `OBStatusReason.StatusReasonCode` | `OBExternalStatusReason1Code` |
| payment-initiation | `OBExternalStatusReason1Code` | `OBExternalStatusReason1Code` |
| payment-initiation | `OBPaymentStatusReason.StatusReasonCode` | `OBExternalStatusReason1Code` |
| payment-initiation | `OBStatusReason.StatusReasonCode` | `OBExternalStatusReason1Code` |
| payment-initiation | `OBWritePaymentDetails1.StatusDetail.StatusReason` | `OBExternalStatusReason1Code` |
| vrp | `OBExternalStatusReason1Code` | `OBExternalStatusReason1Code` |
| vrp | `OBPaymentStatusReason.StatusReasonCode` | `OBExternalStatusReason1Code` |
| vrp | `OBStatusReason.StatusReasonCode` | `OBExternalStatusReason1Code` |

## 4. Ignored — unreferenced (orphan) schemas

Defined in `components/schemas` but not `$ref`'d anywhere in the file. Not tagged; candidates for removal or for tagging if they are meant to be used.

| File | Schema | Values | Closest codeset |
|---|---|---|---|
| account-info | `OBFrequencyPeriodType` | ADHO, YEAR, DAIL, INDA, MNTH, QURT, MIAN, WEEK | `OBFrequency2Code` partial (ADHO not in CSV; CSV adds MOVE, NONE, SLCT, TEND) — needs decision |
| payment-initiation | `OBAddressTypeCode` | Business, Correspondence, DeliveryTo, MailTo, POBox, Postal, Residential, Statement | Legacy long-name form of `OBAddressType2Code` — no CSV match |
| vrp | `OBExternalStatus2Code` | AUTH, AWAU, RJCT | `OBInternalConsentStatus2Code` (missing COND) |
| vrp | `OBAddressTypeCode` | Business, Correspondence, DeliveryTo, MailTo, POBox, Postal, Residential, Statement | Legacy long-name form of `OBAddressType2Code` — no CSV match |
| vrp | `OBVRPStatusReasonCode` | UK.OBIE.ExemptionNotApplied, UK.OBIE.OtherReason | None — values not in any CSV |

## 5. Ignored — enums not backed by a codeset

| File | Node | Values | Reason |
|---|---|---|---|
| vrp | `/paths/~1domestic-vrp-consents~1{ConsentId}/patch/requestBody/content/application~1json-patch+json/schema/items.op` | add, remove, replace, move, copy, test | RFC 6902 JSON Patch operation |
| vrp | `OBDomesticVRPControlParameters.PeriodicLimits/items.PeriodType` | Day, Week, Fortnight, Month, Half-year, Year | VRP control-parameter period; no codeset CSV |
| vrp | `OBDomesticVRPControlParameters.PeriodicLimits/items.PeriodAlignment` | Consent, Calendar | VRP control-parameter alignment; no codeset CSV |
| vrp | `OBPAFundsAvailableResult1.FundsAvailable` | Available, NotAvailable | VRP funds-confirmation result; no codeset CSV |

## 6. Ignored — PCA / BCA / Product area

Known-flawed area; enums here are not consistently represented in the codeset CSVs. Not tagged, values untouched. Exception: `ProductType` matches `OBInternalProductType1Code` exactly and **is tagged**.

| Root schema | Enum nodes | Distinct property names |
|---|---|---|
| `OBBCAData1` | 47 | AgreementPeriod, ApplicationFrequency, BankInterestRateType, CalculationFrequency, CalculationMethod, CappingPeriod, DepositInterestAppliedCoverage, Destination, FeeCategory, FeeFreeLengthPeriod, FeeRateType, FeeType, FixedVariableInterestRateType, MinMaxType, OverdraftInterestChargingCoverage, OverdraftType, Segment, TariffType, TierBandMethod |
| `OBPCAData1` | 44 | ApplicationFrequency, BankInterestRateType, CalculationFrequency, CalculationMethod, CappingPeriod, DepositInterestAppliedCoverage, Destination, FeeCategory, FeeRateType, FeeType, FixedVariableInterestRateType, MinMaxType, OverdraftInterestChargingCoverage, OverdraftType, Segment, TierBandMethod |
| `OBReadProduct2` | 30 | AgreementPeriod, AmountType, ApplicationFrequency, BankInterestRateType, CalculationFrequency, DepositInterestAppliedCoverage, Destination, FeeFreeLengthPeriod, FeeType, LoanProviderInterestRateType, MaxHolidayPeriod, MaxTermPeriod, MinTermPeriod, OverdraftInterestChargingCoverage, OverdraftType, RepaymentFrequency, RepaymentType, Segment, TariffType, TierBandMethod |
| `OB_FeeCategory1Code` | 1 | OB_FeeCategory1Code |
| `OB_FeeFrequency1Code_0` | 1 | OB_FeeFrequency1Code_0 |
| `OB_FeeFrequency1Code_1` | 1 | OB_FeeFrequency1Code_1 |
| `OB_FeeFrequency1Code_2` | 1 | OB_FeeFrequency1Code_2 |
| `OB_FeeFrequency1Code_3` | 1 | OB_FeeFrequency1Code_3 |
| `OB_FeeFrequency1Code_4` | 1 | OB_FeeFrequency1Code_4 |
| `OB_FeeType1Code` | 1 | OB_FeeType1Code |
| `OB_InterestCalculationMethod1Code` | 1 | OB_InterestCalculationMethod1Code |
| `OB_InterestFixedVariableType1Code` | 1 | OB_InterestFixedVariableType1Code |
| `OB_InterestRateType1Code_0` | 1 | OB_InterestRateType1Code_0 |
| `OB_InterestRateType1Code_1` | 1 | OB_InterestRateType1Code_1 |
| `OB_MinMaxType1Code` | 1 | OB_MinMaxType1Code |
| `OB_OverdraftFeeType1Code` | 1 | OB_OverdraftFeeType1Code |
| `OB_Period1Code` | 1 | OB_Period1Code |

## 7. Codesets in the CSVs not used by any tagged node

`OBExternalStatusReason1Code` is referenced by string-only fields (section 3). The rest are not referenced by any v4.0.1 AIS/PIS/CBPII/VRP enum (some may be used by the Events APIs, which are out of scope).

- `ISO_External_CodeSet/ExternalAccountIdentification1Code` (4 values)
- `ISO_External_CodeSet/ExternalAuthenticationChannel1Code` (4 values)
- `ISO_External_CodeSet/ExternalAuthorityIdentification1Code` (1 values)
- `ISO_External_CodeSet/ExternalChargeType1Code` (12 values)
- `ISO_External_CodeSet/ExternalDateType1Code` (4 values)
- `ISO_External_CodeSet/ExternalDocumentAmountType1Code` (26 values)
- `ISO_External_CodeSet/ExternalDocumentLineType1Code` (19 values)
- `ISO_External_CodeSet/ExternalDocumentPurpose1Code` (2 values)
- `ISO_External_CodeSet/ExternalGarnishmentType1Code` (3 values)
- `ISO_External_CodeSet/ExternalInformationType1Code` (6 values)
- `ISO_External_CodeSet/ExternalMandateReason1Code` (48 values)
- `ISO_External_CodeSet/ExternalMandateSuspensionReason1Code` (6 values)
- `ISO_External_CodeSet/ExternalPersonIdentification1Code` (10 values)
- `ISO_External_CodeSet/ExternalSystemBalanceType1Code` (70 values)
- `ISO_External_CodeSet/ExternalTaxAmountType1Code` (5 values)
- `OB_Internal_CodeSet/OBEventType1Code` (4 values)
- `OB_Internal_CodeSet/OBExternalEventAccountAccessConsentLinkedAccountUpdateReason1Code` (2 values)
- `OB_Internal_CodeSet/OBExternalStatusReason1Code` (330 values)

## 8. Items needing your decision

1. **`OBInternalFinancialInstitutionIdentification4Code`** — CSV value `UK.OBIE.NCC.[ISO3166-aplha2-CountryCode]` is a pattern (and misspells *alpha2*). Aligning literally would add it as an enum value. Options: expand per country, add an exception, or fix the CSV.
2. **Orphan schemas** (section 4) — remove, leave, or tag? `OBFrequencyPeriodType` mapping is ambiguous.
3. **`AuthorisationType` missing `Multiple`** on File and International consent request/response and Domestic Standing Order consent response — will be added at generation per your direction.
4. **Balance `SubType`** — currently BCUR/LCUR only; will be expanded to the full `ExternalBalanceSubType1Code` (21 values) per your direction.

