from flask_wtf import FlaskForm
from wtforms import FormField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length
from app.web.forms.address import AddressForm

class UnitForm(FlaskForm):
    rent = IntegerField('rent', validators=[])
