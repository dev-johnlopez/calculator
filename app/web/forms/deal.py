from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField
from wtforms.validators import DataRequired, Length, Optional
from app.web.forms.address import AddressForm
from app.web.forms.unit import UnitForm

class DealForm(FlaskForm):
    #propertyType = SelectField('state', choices=[
    #                                        ("sfh", "Single Family Home"),
    #                                        ("multi", "Multi-Unit"),
    #                                        ("commercial", "Commercial")],
    #    validators=[DataRequired()])
    address = FormField(AddressForm)
    listPrice = IntegerField('listPrice', validators=[DataRequired(), Optional()])
    purchasePrice = IntegerField('purchasePrice', validators=[DataRequired(), Optional()])
    downPayment = IntegerField('downPayment', validators=[DataRequired(), Optional()])
    financedAmount = IntegerField('financedAmount', validators=[Optional()])
    interestRate = DecimalField('interestRate', validators=[DataRequired(), Optional()])
    vacancyRate = DecimalField('vacancyRate', validators =[Optional()])
    units = FieldList(FormField(UnitForm), min_entries=0)
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
