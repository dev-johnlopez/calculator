#!flask/bin/python
import unittest
from decimal import Decimal
#from math import round
from flask_security import current_user
from app import db
from base import BaseTestCase
from app.web.models.property import Property
from app.web.models.unit import Unit
from app.web.models.address import Address
from app.web.util.geocode import get_google_results

class PropertyTestCase(BaseTestCase):

    def setUp(self):
        super(PropertyTestCase,self).setUp()
        with self.client:
            self.login("ad@min.com", "admin")
            property = Property()
            self.initProperty(property)
            db.session.add(property)
            db.session.commit()
            self.logout()

    def test_property_is_not_null(self):
        prop = Property.query.first()
        self.assertTrue(prop is not None)

    def test_get_address(self):
        prop = Property.query.first()
        self.assertTrue(prop.address == prop.getAddress())

    def test_get_list_price(self):
        prop = Property.query.first()
        self.assertTrue(prop.getListPrice() == 400000)

    def test_get_purchase_price(self):
        prop = Property.query.first()
        self.assertTrue(prop.getPurchasePrice() == 300000)

    def test_get_term_length(self):
        prop = Property.query.first()
        self.assertTrue(prop.getTermLength() == 30)

    def test_get_down_payment(self):
        prop = Property.query.first()
        self.assertTrue(prop.getDownPayment() == 0)

    def test_get_interest_rate(self):
        prop = Property.query.first()
        self.assertTrue(abs(prop.getInterestRate()-Decimal(0.045))<0.00000001)

    def test_get_unit_count(self):
        prop = Property.query.first()
        self.assertTrue(len(prop.getUnits()) == 2)

    def test_get_vacancy_rate(self):
        prop = Property.query.first()
        self.assertTrue(abs(prop.getVacancyRate()-Decimal(0.07))<0.00000001)

    def test_get_occupancy_rate(self):
        prop = Property.query.first()
        self.assertTrue(abs(prop.getOccupancyRate()-Decimal(0.93))<0.00000001)

    def test_get_taxes(self):
        prop = Property.query.first()
        self.assertTrue(prop.getTaxes() == 1000)

    def test_get_insurance_premiums(self):
        prop = Property.query.first()
        self.assertTrue(prop.getInsurancePremiums() == 500)

    def test_get_property_management_fee(self):
        prop = Property.query.first()
        self.assertTrue(abs(prop.getPropertyManagementFee()-Decimal(0.1))<0.00000001)

    def test_get_capex_reserves(self):
        prop = Property.query.first()
        self.assertTrue(abs(prop.getCapExReserves()-Decimal(0.07))<0.00000001)

    def test_get_maintenance(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMaintenance() == 100)

    def test_get_hoa(self):
        prop = Property.query.first()
        self.assertTrue(prop.getHOA() == 200)

    def test_get_water(self):
        prop = Property.query.first()
        self.assertTrue(prop.getWater() == 10)

    def test_get_garbage(self):
        prop = Property.query.first()
        self.assertTrue(prop.getGarbage() == 10)

    def test_get_gas(self):
        prop = Property.query.first()
        self.assertTrue(prop.getGas() == 50)

    def test_get_electricity(self):
        prop = Property.query.first()
        self.assertTrue(prop.getElectricity() == 50)

    def test_get_other(self):
        prop = Property.query.first()
        self.assertTrue(prop.getOther() == 0)

    def test_get_monthly_income(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMonthlyIncome() == 3000)

    def test_get_monthly_mortgage_payment(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMonthlyMortgagePayment() == 1520.06)

    def test_get_monthly_piti(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMonthlyPITI() == 1645.06)

    def test_get_monthly_property_management_expense(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMonthlyPropertyManagementExpense() == 300)

    def test_get_monthly_capex_reserve_expense(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMonthlyCapExReserveExpense() == 210)

    def test_get_monthly_vacancy_and_credit_loss(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMonthlyVacancyAndCreditLoss() == 210)

    def test_get_monthly_operating_expenses(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMonthlyOperatingExpenses() == 845)

    def test_get_total_monthly_expenses(self):
        prop = Property.query.first()
        self.assertTrue(prop.getTotalMonthlyExpenses() == 2785.06)

    def test_get_annual_income(self):
        prop = Property.query.first()
        self.assertTrue(prop.getAnnualIncome() == 36000)

    def test_get_annual_mortgage_payments(self):
        prop = Property.query.first()
        self.assertTrue(prop.getAnnualMortgagePayments() == 18240.72)

    def test_get_annual_piti(self):
        prop = Property.query.first()
        self.assertTrue(prop.getAnnualPITI() == 19740.72)

    def test_get_annual_property_management_expense(self):
        prop = Property.query.first()
        self.assertTrue(prop.getAnnualPropertyManagementExpense() == 3600)

    def test_get_annual_capex_reserve_expense(self):
        prop = Property.query.first()
        self.assertTrue(prop.getAnnualCapExReserveExpense() == 2520)

    def test_get_annual_operating_expenses(self):
        prop = Property.query.first()
        self.assertTrue(prop.getAnnualOperatingExpenses() == 10140)

    def test_get_total_annual_expenses(self):
        prop = Property.query.first()
        self.assertTrue(prop.getTotalAnnualExpenses() == 33420.72)

    def test_get_annual_vacancy_and_credit_loss(self):
        prop = Property.query.first()
        self.assertTrue(prop.getAnnualVacancyAndCreditLoss() == 2520)

    # Income to Value ratio
    def test_get_gross_rent_multiplier(self):
        prop = Property.query.first()
        self.assertTrue(prop.getGrossRentMultiplier() == 8.33)

    def test_get_market_value(self):
        prop = Property.query.first()
        self.assertTrue(prop.getMarketValue() == 299880)

    def test_getGrossScheduledIncome(self):
        prop = Property.query.first()
        self.assertTrue(prop.getGrossScheduledIncome(0) == 36000)

    def test_getGrossOperatingIncome(self):
        prop = Property.query.first()
        self.assertTrue(prop.getGrossOperatingIncome() == 33480)

    def test_getNetOperatingIncome(self):
        prop = Property.query.first()
        self.assertTrue(prop.getNetOperatingIncome() == 23340)

    def test_getEstNetOperatingIncomeFromCapRate(self):
        prop = Property.query.first()
        self.assertTrue(prop.getEstNetOperatingIncomeFromCapRate() == 23340)

    def test_getCapitalizationRate(self):
        prop = Property.query.first()
        self.assertTrue(abs(prop.getCapitalizationRate()-Decimal(0.0778))<0.00000001)

    def test_getValueFromCapitalizationRate(self):
        prop = Property.query.first()
        self.assertTrue(prop.getValueFromCapitalizationRate() == 300000)

    def test_getNetIncomeMultiplier(self):
        prop = Property.query.first()
        self.assertTrue(prop.getNetIncomeMultiplier() == 12.85)

    def test_getPresentValueFromNIM(self):
        prop = Property.query.first()
        self.assertTrue(prop.getPresentValueFromNIM() == 299919.00)


    # Utility functions
    def initProperty(self, property):
        address = Address()
        property.address = address

        address = property.address
        address.addressLine1 = "2820 N. Greenview Ave."
        address.addressLine2 = "Unit I"
        address.addressLine3 = ""
        address.city = "Chicago"
        address.state = "IL"
        address.postalCode = "60657"

        #geocode address
        geoInfo = get_google_results(address)
        address.latitude = geoInfo['latitude']
        address.longitude = geoInfo['longitude']

        #create deal
        property.listPrice    = 400000
        property.purchasePrice    = 300000
        property.downPayment    = 0
        property.interestRate    = 4.5
        property.termLength = 30

        unit = Unit()
        unit.income = 1500
        property.units.append(unit)

        unit = Unit()
        unit.income = 1500
        property.units.append(unit)

        #Average time of no revenue
        property.vacancyRate = 7

        #General Expenses
        property.taxes = 1000
        property.insurancePremiums = 500
        property.propertyManagementFee = 10
        property.capEx = 7

        #Monthly Expenses
        property.maintenance = 100
        property.hoa = 200
        property.water = 10
        property.garbage = 10
        property.gas = 50
        property.electricity = 50
        property.other = 0
