from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField, StringField
from wtforms.validators import DataRequired, Length, Optional
from app.web.common.forms.addressForm import AddressForm
from app.web.contacts.forms.no_csrf_contact import NoCSRFContactForm



class PropertyDetailsForm(FlaskForm):
    property_type = SelectField('state', choices=[  ("sfr", "Singly Family Residence"),
                                                    ("multi", "Multi-Unit")],
                                                    validators=[DataRequired()])
    bedrooms = IntegerField('bedrooms', validators=[Optional()])
    bathrooms = IntegerField('bathrooms', validators=[Optional()])
    garage = IntegerField('garage', validators=[Optional()])
    square_footage = IntegerField('square_footage', validators=[Optional()])
    year_built = IntegerField('year_built', validators=[Optional()])

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(PropertyDetailsForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)


class ListingForm(FlaskForm):
    #propertyType = SelectField('state', choices=[
    #                                        ("sfh", "Single Family Home"),
    #                                        ("multi", "Multi-Unit"),
    #                                        ("commercial", "Commercial")],
    #    validators=[DataRequired()])
    address = FormField(AddressForm)
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
    #seller_id = SelectField('Seller', choices=[0, ""], validators=[Optional()])
    #seller = FormField(NoCSRFContactForm)
