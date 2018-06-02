from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField, StringField, HiddenField
from wtforms.validators import DataRequired, Length, Optional
from app.web.common.forms.addressForm import AddressForm

class NoCSRFContactForm(FlaskForm):
    id = HiddenField(validators=[Optional()])
    first_name = StringField('first_name', validators=[Optional()])
    last_name = StringField('last_name', validators=[Optional()])
    email = StringField('email', validators=[Optional()])
    phone_number = StringField('phone', validators=[Optional()])

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(NoCSRFContactForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)
