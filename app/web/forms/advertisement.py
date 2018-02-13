from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField
from wtforms.validators import DataRequired, Length, Optional

class AdvertisementForm(FlaskForm):
    #propertyType = SelectField('state', choices=[
    #                                        ("sfh", "Single Family Home"),
    #                                        ("multi", "Multi-Unit"),
    #                                        ("commercial", "Commercial")],
    #    validators=[DataRequired()])
    address = FormField(AddressForm)
    askingPrice = IntegerField('askingPrice', validators=[Optional()])
    arv = IntegerField('arv', validators=[Otional()])
