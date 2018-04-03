from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField, StringField
from wtforms.validators import DataRequired, Length, Optional
from app.web.common.forms.address import AddressForm
from app.web.analysis.forms.expenses import ExpenseForm

class DealForm(FlaskForm):
    #propertyType = SelectField('state', choices=[
    #                                        ("sfh", "Single Family Home"),
    #                                        ("multi", "Multi-Unit"),
    #                                        ("commercial", "Commercial")],
    #    validators=[DataRequired()])
    address = FormField(AddressForm)
    expenses = FieldList(FormField(ExpenseForm))
    property_type = SelectField('state', choices=[  ("", ""),
                                                    ("Singly Family Residence", "Singly Family Residence"),
                                                    ("Multi-Unit", "Multi-Unit")],
                                                    validators=[DataRequired()])
    bedrooms = IntegerField('bedrooms', validators=[Optional()])
    bathrooms = StringField('bathrooms', validators=[Optional()])
    garage = IntegerField('garage', validators=[Optional()])
    square_footage = IntegerField('square_footage', validators=[Optional()])
    year_built = IntegerField('year_built', validators=[Optional()])
    listPrice = IntegerField('listPrice', validators=[DataRequired()])
    arv    = IntegerField('arv', validators=[Optional()])
    rehabCost = IntegerField('rehabCost', validators=[Optional()])
    income = IntegerField('income', validators=[Optional()])
    seller_name = StringField('seller_name', validators=[DataRequired(), Length(min=0, max=255)])
    seller_phone = StringField('seller_phone', validators=[DataRequired(), Length(min=0, max=255)])
    seller_email = StringField('seller_email', validators=[DataRequired(), Length(min=0, max=255)])
