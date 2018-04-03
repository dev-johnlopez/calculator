from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField, StringField
from wtforms.validators import DataRequired, Length, Optional
from app.web.common.forms.addressForm import AddressForm

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[Optional()])
    phone = StringField('phone', validators=[Optional()])
