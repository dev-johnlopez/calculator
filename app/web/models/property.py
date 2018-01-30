# Import the database object (db) from the main application module
from app import db
from decimal import Decimal
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

    def __repr__(self):
        return '%s' % self.address

    #######################################################
    ################### Getter functions ##################
    #######################################################

    def getAddress(self):
        return self.address

    def getListPrice(self):
        return Decimal(self.listPrice)

    def getPurchasePrice(self):
        return Decimal(self.purchasePrice)

    def getTermLength(self):
        return self.termLength

    def getDownPayment(self):
        if(self.downPayment is None):
            return 0
        return Decimal(self.downPayment)

    def getInterestRate(self):
        if self.interestRate is None:
            return 0
        return Decimal(self.interestRate/100)

    def getUnits(self):
        return self.units

    def getVacancyRate(self):
        return Decimal(self.vacancyRate / 100)

    def getOccupancyRate(self):
        return Decimal(1 - self.getVacancyRate())

    def getTaxes(self):
        return Decimal(self.taxes)

    def getInsurancePremiums(self):
        return Decimal(self.insurancePremiums)

    def getPropertyManagementFee(self):
        return Decimal(self.propertyManagementFee / 100)

    def getCapExReserves(self):
        return Decimal(self.capEx / 100)

    def getMaintenance(self):
        return Decimal(self.maintenance)

    def getHOA(self):
        return Decimal(self.hoa)

    def getWater(self):
        return Decimal(self.water)

    def getGarbage(self):
        return Decimal(self.garbage)

    def getGas(self):
        return Decimal(self.gas)

    def getElectricity(self):
        return Decimal(self.electricity)

    def getOther(self):
        return Decimal(self.other)

    def getMonthlyPropertyTax(self):
        return Decimal(round(self.getTaxes() / 12,2))

    def getMonthlyInsurancePremiumExpense(self):
        return Decimal(round(self.getInsurancePremiums() / 12,2))


    #######################################################
    ################# Monthly Calculations ################
    #######################################################

    def getMonthlyIncome(self):
        scheduledIncome = 0
        for unit in self.units:
           scheduledIncome += unit.income
        return Decimal(round(scheduledIncome,2))

    def getMonthlyMortgagePayment(self):
        return Decimal(round(LoanCalculator.getMortgagePayment(self.getPurchasePrice() - self.getDownPayment(), self.getTermLength(), self.getInterestRate()),2))

    def getMonthlyPITI(self):
        return Decimal(round(LoanCalculator.getPITI(self.getMonthlyMortgagePayment(), self.getTaxes(), self.getInsurancePremiums()),2))

    def getMonthlyPropertyManagementExpense(self):
        return Decimal(round(self.getMonthlyIncome() * self.getPropertyManagementFee(),2))

    def getMonthlyCapExReserveExpense(self):
        return Decimal(round(self.getMonthlyIncome() * self.getCapExReserves(),2))

    def getMonthlyVacancyAndCreditLoss(self):
        return Decimal(round(self.getAnnualVacancyAndCreditLoss()/12,2))

    def getMonthlyOperatingExpenses(self):
        return Decimal(round(self.getMonthlyPropertyManagementExpense()
                + self.getMaintenance()
                + self.getHOA()
                + self.getWater()
                + self.getGarbage()
                + self.getGas()
                + self.getElectricity()
                + self.getOther()
                + self.getMonthlyPropertyTax()
                + self.getMonthlyInsurancePremiumExpense(),2))

    def getTotalMonthlyExpenses(self):
        return Decimal(round(self.getMonthlyOperatingExpenses() + self.getMonthlyMortgagePayment() + self.getMonthlyCapExReserveExpense() + self.getMonthlyVacancyAndCreditLoss(),2))

    #######################################################
    ################# Annual Calculations #################
    #######################################################

    def getAnnualIncome(self):
        return Decimal(round(self.getMonthlyIncome() * 12,2))

    def getAnnualMortgagePayments(self):
        return Decimal(round(self.getMonthlyMortgagePayment() * 12,2))

    def getAnnualPITI(self):
        return Decimal(round(self.getMonthlyPITI() * 12,2))

    def getAnnualPropertyManagementExpense(self):
        return Decimal(round(self.getMonthlyPropertyManagementExpense() * 12,2))

    def getAnnualCapExReserveExpense(self):
        return Decimal(round(self.getMonthlyCapExReserveExpense() * 12,2))

    def getAnnualOperatingExpenses(self):
        return Decimal(round(self.getMonthlyOperatingExpenses() * 12,2))

    def getTotalAnnualExpenses(self):
        return Decimal(round(self.getTotalMonthlyExpenses() * 12,2))

    def getAnnualVacancyAndCreditLoss(self):
        return Decimal(round(FinancialCalculator.getVacancyAndCreditLoss(self.getGrossScheduledIncome(0), self.getVacancyRate()),2))

    #######################################################
    ################# General Calculations ################
    #######################################################

    # Income to Value ratio
    def getGrossRentMultiplier(self):
        return Decimal(round(FinancialCalculator.getGrossRentMultiplier(self.getPurchasePrice(), self.getGrossScheduledIncome(0)),2))

    def getMarketValue(self):
        return Decimal(round(FinancialCalculator.getMarketValue(self.getGrossRentMultiplier(), self.getGrossScheduledIncome(0)),2))

    # Total rent payable for that year under current contracts
    # for occupied space + Total potential rent during vacancies
    # Note: Ignores vacancy. Used to calculate maximum revenue for a getNumberOfYearsForDoubledInvestment
    def getGrossScheduledIncome(self, totalPotentialRent):
        return FinancialCalculator.getGrossScheduledIncome(self.getAnnualIncome(), totalPotentialRent)

    # How to calculate the actual income of a property
    def getGrossOperatingIncome(self):
        return FinancialCalculator.getGrossOperatingIncome(self.getGrossScheduledIncome(0), self.getAnnualVacancyAndCreditLoss())

    # Property's income after reducing operating expenses,
    # vacancy, etc.
    #
    # Loan payments, depreciation, and capital expenditures
    # are not considered operating expenses.
    def getNetOperatingIncome(self):
        return FinancialCalculator.getNetOperatingIncome(self.getGrossOperatingIncome(), self.getAnnualOperatingExpenses())

    def getEstNetOperatingIncomeFromCapRate(self):
        return FinancialCalculator.getNetOperatingIncomeFromCapRate(self.getPurchasePrice(), self.getCapitalizationRate())

    # Capitalization rate is the rate at which you discount
    # future income to determine its present value.
    #
    # Cap rates are used to express the relationship
    # between a property's value and its Net
    # Operating Income (NOI)
    def getCapitalizationRate(self):
        return Decimal(FinancialCalculator.getCapitalizationRate(self.getNetOperatingIncome(), self.getPurchasePrice()))

    def getValueFromCapitalizationRate(self):
        return FinancialCalculator.getValueFromCapitalizationRate(self.getNetOperatingIncome(), self.getCapitalizationRate())

    # Net Income Multiple represents what a typical investor
    # would pay for each dollar of NOI.
    def getNetIncomeMultiplier(self):
        return Decimal(round(FinancialCalculator.getNetIncomeMultiplier(self.getCapitalizationRate()),2))

    def getPresentValueFromNIM(self):
        return Decimal(round(FinancialCalculator.getPresentValueFromNIM(self.getNetIncomeMultiplier(), self.getNetOperatingIncome()),2))

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
