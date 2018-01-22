# Import the database object (db) from the main application module
from app import db
from app.web.models import baseModel, unit
from app.web.util.calculations import FinancialCalculator


# Define a User model
class Property(baseModel.Base):

    __tablename__ = 'property'

    address = db.relationship("Address", uselist=False, back_populates="property")
    listPrice    = db.Column(db.Integer)
    purchasePrice    = db.Column(db.Integer)
    downPayment    = db.Column(db.Integer)
    interestRate    = db.Column(db.Numeric(6,4))

    #array of units
    units = db.relationship('Unit', backref='property', lazy=True)
    #Average time of no revenue
    vacancyRate = db.Column(db.Numeric(7,4))

    #General Expenses
    taxes = db.Column(db.Integer)
    insurancePremiums = db.Column(db.Integer)
    propertyManagementFee = db.Column(db.Numeric(7,4))
    capEx = db.Column(db.Numeric(7,4))

    #Monthly Expenses
    maintenance = db.Column(db.Integer)
    hoa = db.Column(db.Integer)
    water = db.Column(db.Integer)
    garbage = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    electricity = db.Column(db.Integer)
    other = db.Column(db.Integer)

    # New instance instantiation procedure
    #def __init__(self, name, address):
    #    self.name = name
    #    self.address = address

    def __repr__(self):
        return '%s' % self.address

    def getScheduledIncome():
        scheduledIncome = 0
        for unit in self.units:
           scheduledIncome += unit.income
        return scheduledIncome

    def lengthUntilDoubledInvestment(growthRate, exactMatch):
        return FinancialCalculator.getNumberOfYearsForDoubledInvestment(growthRate, exactMatch)

    def getFutureValue(principal, periodicRate, numPeriods):
        return FinancialCalculator.getFutureValue(princiapl, periodicRate, numPeriods)

    def getAmount(principal, rate, time):
        return FinancialCalculator.getAmount(principal, rate, time)

    # Present Value of a property - need to look at the book
    # to better document
    def getPresentValue(interestRate, numPeriods):
        return FinancialCalculator.getPresentValue(self.purchasePrice, interestRate, numPeriods)

    # Income to Value ratio
    def getGrossRentMultiplier():
        return FinancialCalculator.getGrossRentMultiplier(self.purchasePrice, self.getScheduledIncome())

    def getMarketValue():
        return FinancialCalculator.getMarketValue(self.getGrossRentMultiplier(), self.getScheduledIncome())

    # Annual income of a property if all rentable space
    # were rented and all rent collected.
    #
    # Maximum potential income wiithout regard to vacancy
    # or credit loss


    # Total rent payable for that year under current contracts
    # for occupied space + Total potential rent during vacancies
    def getGrossScheduledIncome(totalPlannedIncome, totalPotentialRent):
        return FinancialCalculator.getGrossScheduledIncome(self.getScheduledIncome() * 12, totalPotentialRent)

    def getVacancyAndCreditLoss(lossPercentage):
        return FinancialCalculator.getVacancyAndCreditLoss(self.getGrossScheduledIncome(), lossPercentage)

    # How to calculate the actual income of a property
    def getGrossOperatingIncome(vacancyAndCreditLoss):
        return FinancialCalculator.getGrossOperatingIncome(self.getGrossScheduledIncome(), vacancyAndCreditLoss)

    # Property's income after reducing operating expenses,
    # vacancy, etc.
    #
    # Loan payments, depreciation, and capital expenditures
    # are not considered operating expenses.
    def getNetOperatingIncome(grossOperatingIncome, operatingExpenses):
        return FinancialCalculator.getNetOperatingIncome(self.getGrossOperatingIncome(), operatingExpenses)

    def getEstNetOperatingIncomeFromCapRate(capRate):
        return FinancialCalculator.getNetOperatingIncomeFromCapRate(self.purchasePrice, self.getCapitalizationRate())

    # Capitalization rate is the rate at which you discount
    # future income to determine its present value.
    #
    # Cap rates are used to express the relationship
    # between a property's value and its Net
    # Operating Income (NOI)
    def getCapitalizationRate():
        return FinancialCalculator.getCapitalizationRate(self.getNetOperatingIncome(), self.purchasePrice)

    def getValueFromCapitalizationRate():
        return FinancialCalculator.getValueFromCapitalizationRate(self.getNetOperatingIncome(), self.getCapitalizationRate())

    # Net Income Multiple represents what a typical investor
    # would pay for each dollar of NOI.
    def getNetIncomeMultiplier():
        return FinancialCalculator.getNetIncomeMultiplier(self.getCapitalizationRate)

    def getPresentValueFromNIM():
        return FinancialCalculator.getPresentValueFromNIM(self.getNetIncomeMultiplier(), self.getNetOperatingIncome())

    # Taxable income
    def getTaxableIncome(netOperatingIncome, mortgageInterest,
                            propertyDepereciation, capitalDepreciation,
                            loanAmortization, interestEarned):
        return FinancialCalculator.getTaxableIncome(self.getNetOperatingIncome(), mortgageInterest,
                                propertyDepereciation, capitalDepreciation,
                                loanAmortization, interestEarned)

    # Cash Flow
    # Need to add discounted cashflow sometime... Chapter 23 (Calc 16)
    def getCashFlowBeforeTaxes(netOperatingIncome, debtService,
                                capitalAdditions, loanProceeds,
                                interestEarned):
        return FinancialCalculator.getCashFlowBeforeTaxes(self.getNetOperatingIncome(), debtService,
                                    capitalAdditions, loanProceeds,
                                    interestEarned)

    def getCashFlowAfterTaxes(cashFlowBeforeTaxes, incomeTaxLiability):
        return FinancialCalculator.getCashFlowAfterTaxes(cashFlowBeforeTaxes, incomeTaxLiability)

    def getCashOnCashReturn(annualCashFlow, cashInvested):
        return FinancialCalculator.getCashOnCashReturn(annualCashFlow, cashInvested)

    # Sales Proceeds
    def getSalesProceedsBeforeTaxes(sellingPrice, costsOfSale,
                                        mortgagePayment):
        return FinancialCalculator.getSalesProceedsBeforeTaxes(sellingPrice, costsOfSale,
                                            mortgagePayment)

    def getSalesProceedsAfterTaxes(salesProceedsBeforeTaxes, taxOnSale):
        return FinancialCalculator.getSalesProceedsAfterTaxes(salesProceedsBeforeTaxes, taxOnSale)
