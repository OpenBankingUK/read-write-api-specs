#!/usr/bin/env bash

# install umldiagram from https://bitbucket.org/openbankingteam/uml-generator/src/master/
umldiagram --src=./dist/swagger/account-info-swagger.yaml --dir=uml-diagrams\
	--schema=OBReadConsent1\
	--schema=OBReadConsentResponse1\
	--schema=OBReadAccount6\
	--schema=OBReadBalance1\
	--schema=OBReadTransaction6\
	--schema=OBReadBeneficiary5\
	--schema=OBReadDirectDebit2\
	--schema=OBReadStandingOrder6\
	--schema=OBReadProduct2\
	--schema=OBBCAData1\
	--schema=OBBCAData1\
	--schema=OBPCAData1\
	--schema=OBReadOffer1\
	--schema=OBParty2\
	--schema=OBReadParty2\
	--schema=OBReadParty3\
	--schema=OBReadScheduledPayment3\
	--schema=OBBCAData1.properties.Overdraft\
	# --schema=OBBCAData1.OtherFeesCharges\ # fix nested objects
	# --schema=Overdraft.OverdraftTierBandSet\ # fix nested objects
	# --schema=LoanInterest\
	# --schema=Repayment\

umldiagram --src=./dist/swagger/payment-initiation-swagger.yaml --dir=uml-diagrams\
	--schema=OBRisk1\
	--schema=OBSCASupportData1\
	--schema=OBWriteFundsConfirmationResponse1\
	--schema=OBWriteDomestic2\
	--schema=OBWriteDomesticConsent4\
	--schema=OBWriteDomesticConsentResponse5\
	--schema=OBWriteDomesticResponse5\
	--schema=OBWritePaymentDetailsResponse1\
	--schema=OBWriteDomesticScheduledConsent4\
	--schema=OBWriteDomesticScheduledConsentResponse5\
	--schema=OBWriteDomesticScheduled2\
	--schema=OBWriteDomesticScheduledResponse5\
	--schema=OBWritePaymentDetailsResponse1\
	--schema=OBWriteDomesticStandingOrderConsent5\
	--schema=OBWriteDomesticStandingOrderConsentResponse6\
	--schema=OBWriteDomesticStandingOrder3\
	--schema=OBWriteDomesticStandingOrderResponse6\
	--schema=OBWritePaymentDetailsResponse1\
	--schema=OBWriteInternationalConsent5\
	--schema=OBWriteInternationalConsentResponse6\
	--schema=OBWriteFundsConfirmationResponse1\
	--schema=OBWriteInternational3\
	--schema=OBWriteInternationalResponse5\
	--schema=OBWritePaymentDetailsResponse1\
	--schema=OBWriteInternationalScheduledConsent5\
	--schema=OBWriteInternationalScheduledConsentResponse6\
	--schema=OBWriteFundsConfirmationResponse1\
	--schema=OBWriteInternationalScheduled3\
	--schema=OBWriteInternationalScheduledResponse6\
	--schema=OBWritePaymentDetailsResponse1\
	--schema=OBWriteInternationalStandingOrderConsent6\
	--schema=OBWriteInternationalStandingOrderConsentResponse7\
	--schema=OBWriteInternationalStandingOrder4\
	--schema=OBWriteInternationalStandingOrderResponse7\
	--schema=OBWritePaymentDetailsResponse1\
	--schema=OBWriteFileConsent3\
	--schema=OBWriteFileConsentResponse4\
	--schema=OBWriteFile2\
	--schema=OBWriteFileResponse3\
	--schema=OBWritePaymentDetailsResponse1\
	# --schema=OBWritePaymentDetails1\
	# --schema=OBDomesticRefundAccount1\
	# --schema=OBInternationalRefundAccount1\
	# --schema=OBDomesticScheduled2\
	# --schema=OBDomesticStandingOrder3\
	# --schema=OBInternational3\
	# --schema=OBExchangeRate2\
	# --schema=OBInternationalScheduled3\
	# --schema=OBInternationalStandingOrder4\
	# --schema=OBFile2\
	# --schema=OBAuthorisation1\
	# --schema=OBMultiAuthorisation1\
	# --schema=OBDomestic2\

umldiagram --src=./dist/swagger/confirmation-funds-swagger.yaml --dir=uml-diagrams\
	--schema=OBFundsConfirmationConsent1\
	--schema=OBFundsConfirmationConsentResponse1\
	--schema=OBFundsConfirmation1\
	--schema=OBFundsConfirmationResponse1\
