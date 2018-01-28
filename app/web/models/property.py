# Import the database object (db) from the main application module
from app import db
from app.web.models import baseModel, unit
from app.web.util.calculations import FinancialCalculator
from app.web.util.loan import LoanCalculator


# Define a User model
class Property(baseModel.Base):

    __tablename__ = 'property'

    address = db.relationship("Address", uselist=False, back_populates="property")
    listPrice    = db.Column(db.Integer)
    purchasePrice    = db.Column(db.Integer)
    downPayment    = db.Column(db.Integer)
    interestRate    = db.Column(db.Numeric(6,4))
    termLength = db.Column(db.Integer)

    #array of units
    units = db.relationship('Unit', backref='property', lazy=True)
    #Average time of no revenue
    vacancyRate = db.Column(db.Numeric(7,4), default=0)

    #General Expenses
    taxes = db.Column(db.Integer, default=0)
    insurancePremiums = db.Column(db.Integer, default=0)
    propertyManagementFee = db.Column(db.Numeric(7,4), default=0, onupdate=0)
    capEx = db.Column(db.Numeric(7,4), default=0, onupdate=0)

    #Monthly Expenses
    maintenance = db.Column(db.Integer, default=0)
    hoa = db.Column(db.Integer, default=0)
    water = db.Column(db.Integer, default=0)
    garbage = db.Column(db.Integer, default=0)
    gas = db.Column(db.Integer, default=0)
    electricity = db.Column(db.Integer, default=0)
    other = db.Column(db.Integer, default=0)

    # New instance instantiation procedure
    #def __init__(self, name, address):
    #    self.name = name
    #    self.address = address

    def __repr__(self):
        return '%s' % self.address

    # Getter functions

    def getAddress(self):
        return self.address

    def getListPrice(self):
        return self.listPrice

    def getPurchasePrice(self):
        return self.purchasePrice

    def getTermLength(self):
        return self.termLength

    def getDownPayment(self):
        return self.downPayment

    def getInterestRate(self):
        return self.interestRate/100

    def getUnits(self):
        return self.units

    def getVacancyRate(self):
        return self.vacancyRate / 100

    def getOccupancyRate(self):
        return 1 - self.getVacancyRate()

    def getTaxes(self):
        return self.taxes

    def getInsurancePremiums(self):
        return self.insurancePremiums

    def getPropertyManagementFee(self):
        return self.propertyManagementFee / 100

    def getCapExReserves(self):
        return self.capEx / 100

    def getMaintenance(self):
        return self.maintenance

    def getHOA(self):
        return self.hoa

    def getWater(self):
        return self.water

    def getGarbage(self):
        return self.garbage

    def getGas(self):
        return self.gas

    def getElectricity(self):
        return self.electricity

    def getOther(self):
        return self.other


    # Monthly Calculations
    def getMonthlyIncome(self):
        scheduledIncome = 0
        for unit in self.units:
           scheduledIncome += unit.income
        return scheduledIncome

    def getMonthlyMortgagePayment(self):
        return LoanCalculator.getMortgagePayment(self.getPurchasePrice(), self.getTermLength(), self.getInterestRate())

    def getMonthlyPITI(self):
        return LoanCalculator.getPITI(self.getMonthlyMortgagePayment(), self.getTaxes(), self.getInsurancePremiums())

    def getMonthlyPropertyManagementExpense(self):
        return self.getMonthlyIncome() * self.getPropertyManagementFee()

    def getMonthlyCapExReserveExpense(self):
        return self.getMonthlyIncome() * self.getCapExReserves()

    def getMonthlyVacancyAndCreditLoss(self):
        return self.getMonthlyIncome() * self.getVacancyRate()

    def getMonthlyOperatingExpenses(self):
        annualExpenses = self.getTaxes() + self.getInsurancePremiums()
        propertyManagementExpense = self.getMonthlyPropertyManagementExpense()
        reserves = self.getMonthlyCapExReserveExpense() + self.getMonthlyVacancyAndCreditLoss()
        return self.getMaintenance() + self.getHOA() + self.getWater() + self.getGarbage() + self.getGas() + self.getElectricity() + self.getOther() + annualExpenses/12 + propertyManagementExpense + reserves

    def getTotalMonthlyExpenses(self):
        return self.getMonthlyOperatingExpenses() + self.getMonthlyMortgagePayment()

    # Annual Calculations
    def getAnnualIncome(self):
        return self.getMonthlyIncome() * 12

    def getAnnualMortgagePayments(self):
        return self.getMonthlyMortgagePayment() * 12

    def getAnnualPITI(self):
        return self.getMonthlyPITI() * 12

    def getAnnualPropertyManagementExpense(self):
        return self.getMonthlyPropertyManagementExpense() * 12

    def getAnnualCapExReserveExpense(self):
        return self.getMonthlyCapExReserveExpense() * 12

    def getAnnualOperatingExpenses(self):
        return self.getMonthlyOperatingExpenses() * 12

    def getTotalAnnualExpenses(self):
        return self.getTotalMonthlyExpenses() * 12

    # Total rent payable for that year under current contracts
    # for occupied space + Total potential rent during vacancies
    # Note: Ignores vacancy. Used to calculate maximum revenue for a getNumberOfYearsForDoubledInvestment
    def getAnnualGrossScheduledIncome(self, totalPotentialRent):
        return FinancialCalculator.getGrossScheduledIncome(self.getAnnualIncome(), totalPotentialRent)

    # General Calculations
    # TODO: Validate if the remaining should be monthly vs annually

    def lengthUntilDoubledInvestment(growthRate, exactMatch):
        return FinancialCalculator.getNumberOfYearsForDoubledInvestment(growthRate, exactMatch)

    def getFutureValue(principal, periodicRate, numPeriods):
        return FinancialCalculator.getFutureValue(princiapl, periodicRate, numPeriods)

    def getAmount(principal, rate, time):
        return FinancialCalculator.getAmount(principal, rate, time)

    # Present Value of a property - need to look at the book
    # to better document
    def getPresentValue(interestRate, numPeriods):
        return FinancialCalculator.getPresentValue(self.getPurchasePrice(), interestRate, numPeriods)

    # Income to Value ratio
    def getGrossRentMultiplier(self):
        return FinancialCalculator.getGrossRentMultiplier(self.getPurchasePrice(), self.getMonthlyIncome())

    def getMarketValue(self):
        return FinancialCalculator.getMarketValue(self.getGrossRentMultiplier(), self.getScheduledIncome())


    def getAnnualVacancyAndCreditLoss(self):
        return FinancialCalculator.getVacancyAndCreditLoss(self.getAnnualGrossScheduledIncome(0), self.getVacancyRate())

    # How to calculate the actual income of a property
    def getGrossOperatingIncome(self):
        return FinancialCalculator.getGrossOperatingIncome(self.getAnnualGrossScheduledIncome(0), self.getAnnualVacancyAndCreditLoss())

    # Property's income after reducing operating expenses,
    # vacancy, etc.
    #
    # Loan payments, depreciation, and capital expenditures
    # are not considered operating expenses.
    def getNetOperatingIncome(self):
        #TODO - calculate expenses
        return FinancialCalculator.getNetOperatingIncome(self.getGrossOperatingIncome(), self.getAnnualOperatingExpenses())

    def getEstNetOperatingIncomeFromCapRate(self, capRate):
        return FinancialCalculator.getNetOperatingIncomeFromCapRate(self.getPurchasePrice(), self.getCapitalizationRate())

    # Capitalization rate is the rate at which you discount
    # future income to determine its present value.
    #
    # Cap rates are used to express the relationship
    # between a property's value and its Net
    # Operating Income (NOI)
    def getCapitalizationRate(self):
        return FinancialCalculator.getCapitalizationRate(self.getNetOperatingIncome(), self.getPurchasePrice())

    def getValueFromCapitalizationRate(self):
        return FinancialCalculator.getValueFromCapitalizationRate(self.getNetOperatingIncome(), self.getCapitalizationRate())

    # Net Income Multiple represents what a typical investor
    # would pay for each dollar of NOI.
    def getNetIncomeMultiplier(self):
        return FinancialCalculator.getNetIncomeMultiplier(self.getCapitalizationRate())

    def getPresentValueFromNIM(self):
        return FinancialCalculator.getPresentValueFromNIM(self.getNetIncomeMultiplier(), self.getNetOperatingIncome())

    # Taxable income
    def getTaxableIncome(self, netOperatingIncome, mortgageInterest,
                            propertyDepereciation, capitalDepreciation,
                            loanAmortization, interestEarned):
        return FinancialCalculator.getTaxableIncome(self.getNetOperatingIncome(), mortgageInterest,
                                propertyDepereciation, capitalDepreciation,
                                loanAmortization, interestEarned)

    # Cash Flow
    # Need to add discounted cashflow sometime... Chapter 23 (Calc 16)
    def getMonthlyCashflowBeforeTaxes(self, capitalAdditions, loanProceeds,
                                interestEarned):
        return self.getCashFlowBeforeTaxes(capitalAdditions, loanProceeds, interestEarned) / 12

    def getCashFlowBeforeTaxes(self, capitalAdditions, loanProceeds,
                                interestEarned):
        return FinancialCalculator.getCashFlowBeforeTaxes(self.getNetOperatingIncome(), self.getAnnualMortgagePayments(),
                                    capitalAdditions, loanProceeds,
                                    interestEarned)

    def getCashFlowAfterTaxes(self, cashFlowBeforeTaxes, incomeTaxLiability):
        return FinancialCalculator.getCashFlowAfterTaxes(cashFlowBeforeTaxes, incomeTaxLiability)

    def getCashOnCashReturn(self, annualCashFlow, cashInvested):
        return FinancialCalculator.getCashOnCashReturn(annualCashFlow, cashInvested)

    # Sales Proceeds
    def getSalesProceedsBeforeTaxes(self, sellingPrice, costsOfSale,
                                        mortgagePayment):
        return FinancialCalculator.getSalesProceedsBeforeTaxes(sellingPrice, costsOfSale,
                                            mortgagePayment)

    def getSalesProceedsAfterTaxes(self, salesProceedsBeforeTaxes, taxOnSale):
        return FinancialCalculator.getSalesProceedsAfterTaxes(salesProceedsBeforeTaxes, taxOnSale)
