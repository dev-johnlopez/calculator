from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField
from wtforms.validators import DataRequired, Length, Optional
from app.web.models.unit import Unit
from app.web.forms.address import AddressForm
from app.web.forms.unit import UnitForm

class DealForm(FlaskForm):
    #propertyType = SelectField('state', choices=[
    #                                        ("sfh", "Single Family Home"),
    #                                        ("multi", "Multi-Unit"),
    #                                        ("commercial", "Commercial")],
    #    validators=[DataRequired()])
    address = FormField(AddressForm)
    listPrice = IntegerField('listPrice', validators=[Optional()])
    purchasePrice = IntegerField('purchasePrice', validators=[Optional()])
    downPayment = IntegerField('downPayment', validators=[Optional()])
    #financedAmount = IntegerField('financedAmount', validators=[Optional()])
    termLength = IntegerField('termLength', validators=[Optional()])
    interestRate = DecimalField('interestRate', validators=[Optional()])
    vacancyRate = DecimalField('vacancyRate', validators =[Optional()])
    units = FieldList(FormField(UnitForm, default=lambda: Unit()), min_entries=0, validators=[Optional()])
    taxes = IntegerField('taxes', validators=[Optional()])
    insurancePremiums = IntegerField('insurancePremiums', validators=[Optional()])
    propertyManagementFee = DecimalField('propertyManagementFee', validators=[Optional()])
    capEx = DecimalField('capEx', validators=[Optional()])
    maintenance = IntegerField('maintenance', validators=[Optional()])
    hoa = IntegerField('hoa', validators=[Optional()])
    water = IntegerField('water', validators=[Optional()])
    garbage = IntegerField('garbage', validators=[Optional()])
    gas = IntegerField('gas', validators=[Optional()])
    electricity = IntegerField('electricity', validators=[Optional()])
    other = IntegerField('other', validators=[Optional()])

    def loadFormFromProperty(self, property):
        self.address.addressLine1.data = property.address.addressLine1
        self.address.addressLine2.data = property.address.addressLine2
        self.address.addressLine3.data = property.address.addressLine3
        self.address.city.data = property.address.city
        self.address.state.data = property.address.state
        self.address.postalCode.data = property.address.postalCode
        #self.address = AddressForm(obj=property.address)
        #self.address.loadFormFromAddress(obj=property.address)
        self.units = []
        for unit in property.units:
            unitForm = UnitForm(obj=unit)
            self.units.append(unitForm)

        self.listPrice.data = property.listPrice
        self.purchasePrice.data = property.purchasePrice
        self.downPayment.data = property.downPayment
        #self.financedAmount = property.financedAmount
        self.interestRate.data = property.interestRate * 100
        self.vacancyRate.data = property.vacancyRate * 100
        self.taxes.data = property.taxes
        self.insurancePremiums.data = property.insurancePremiums
        self.propertyManagementFee.data = property.propertyManagementFee * 100
        self.capEx.data = property.capEx * 100
        self.maintenance.data = property.maintenance
        self.hoa.data = property.hoa
        self.water.data = property.water
        self.garbage.data = property.garbage
        self.gas.data = property.gas
        self.electricity.data = property.electricity
        self.other.data = property.other
