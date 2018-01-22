
class FinancialCalculator():
    #   Here is a great little parlor trick to calculate
    #   the approximate number of years for an investment to
    #   double in value at a particular rate of compound
    #   interest.
    #
    #   Simply take the rate of growth and divide it by 72.
    #   Keep in mind that the answer is not precise; you would
    #   need to divide into 72.73 to nail the exact amount

    # @growthRate : The rate of growth
    # @exactMatch : Determines if it should be a rounded return value
    #               the exact time it takes to double
    @staticmethod
    def getNumberOfYearsForDoubledInvestment(growthRate, exactMatch):
        if exactMatch:
            return 72.73 / growthRate
        else:
            return 72 / growthRate


    #
    #   With compound interest, you apply the interest rate to the
    #   original principal and also to all accumulated interest. This
    #   is different from simple interest, where you apply the interest
    #   rate only to the original principal amount.
    #

    @staticmethod
    def getFutureValue(principal, periodicRate, numPeriods):
        return principal * (1 + periodicRate) ^ numPeriods

    @staticmethod
    def getAmount(principal, rate, time):
        return principal * (1 + (rate * time))


    # Present Value of a property - need to look at the book
    # to better document
    @staticmethod
    def getPresentValue(futureValue, interestRate, numPeriods):
        return futureValue / ((1 + i) ^ numPeriods)

    # Income to Value ratio
    @staticmethod
    def getGrossRentMultiplier(marketValue, scheduledIncome):
        return marketValue/scheduledIncome

    @staticmethod
    def getMarketValue(grossRentMultiplier, scheduledIncome):
        return grossRentMultiplier * scheduledIncome

    # Annual income of a property if all rentable space
    # were rented and all rent collected.
    #
    # Maximum potential income wiithout regard to vacancy
    # or credit loss


    # Total rent payable for that year under current contracts
    # for occupied space + Total potential rent during vacancies
    @staticmethod
    def getGrossScheduledIncome(totalPlannedIncome, totalPotentialRent):
        return totalPlannedIncome + totalPotentialRent

    @staticmethod
    def getVacancyAndCreditLoss(grossScheduledIncome, lossPercentage):
        return grossScheduledIncome * lossPercentage

    # How to calculate the actual income of a property

    @staticmethod
    def getGrossOperatingIncome(grossScheduledIncome, vacancyAndCreditLoss):
        return grossScheduledIncome - vacancyAndCreditLoss

    # Property's income after reducing operating expenses,
    # vacancy, etc.
    #
    # Loan payments, depreciation, and capital expenditures
    # are not considered operating expenses.

    @staticmethod
    def getNetOperatingIncome(grossOperatingIncome, operatingExpenses):
        return grossOperatingIncome - operatingExpenses

    @staticmethod
    def getNetOperatingIncomeFromCapRate(value, capRate):
        return value * capRate

    # Capitalization rate is the rate at which you discount
    # future income to determine its present value.
    #
    # Cap rates are used to express the relationship
    # between a property's value and its Net
    # Operating Income (NOI)
    @staticmethod
    def getCapitalizationRate(netOperatingIncome, value):
        return netOperatingIncome / value

    @staticmethod
    def getValueFromCapitalizationRate(netOperatingIncome, capRate):
        return netOperatingIncome / capRate

    # Net Income Multiple represents what a typical investor
    # would pay for each dollar of NOI.

    @staticmethod
    def getNetIncomeMultiplier(capRate):
        return 1 / capRate

    @staticmethod
    def getPresentValueFromNIM(netIncomeMultiplier, netOperatingIncome):
        return netIncomeMultiplier * netOperatingIncome

    # Taxable income
    @staticmethod
    def getTaxableIncome(netOperatingIncome, mortgageInterest,
                            propertyDepereciation, capitalDepreciation,
                            loanAmortization, interestEarned):
        return netOperatingIncome - mortgageInterest - propertyDepereciation - capitalDepreciation - loanAmortization + interestEarned

    # Cash Flow
    # Need to add discounted cashflow sometime... Chapter 23 (Calc 16)

    @staticmethod
    def getCashFlowBeforeTaxes(netOperatingIncome, debtService,
                                capitalAdditions, loanProceeds,
                                interestEarned):
        return netOperatingIncome - debtService - capitalAdditions + loanProceeds + interestEarned

    @staticmethod
    def getCashFlowAfterTaxes(cashFlowBeforeTaxes, incomeTaxLiability):
        return cashFlowBeforeTaxes - incomeTaxLiability

    @staticmethod
    def getCashOnCashReturn(annualCashFlow, cashInvested):
        return annualCashFlow / cashInvested

    # Sales Proceeds
    @staticmethod
    def getSalesProceedsBeforeTaxes(sellingPrice, costsOfSale,
                                        mortgagePayment):
        return sellingPrice - costsOfSale - mortgagePayment

    @staticmethod
    def getSalesProceedsAfterTaxes(salesProceedsBeforeTaxes, taxOnSale):
        return salesProceedsBeforeTaxes - taxOnSale

    # Need to add other calculations from chapter 23 onward...
