from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField, StringField
from wtforms.validators import DataRequired, Length, Optional
from app.web.common.forms.addressForm import AddressForm

class ContactForm(FlaskForm):
    first_name = StringField('first_name', validators=[Optional()])
    last_name = StringField('last_name', validators=[Optional()])
    email = StringField('email', validators=[Optional()])
    phone = StringField('phone', validators=[Optional()])
