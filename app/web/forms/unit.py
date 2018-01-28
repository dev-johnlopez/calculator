from flask_wtf import FlaskForm
from wtforms import FormField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length
from app.web.forms.address import AddressForm

#Create a filter form to inherit from with csrf_enabled = False
#class FilterForm(FlaskForm):
#    def __init__(self, csrf_enabled=False, *args, **kwargs):
#        super(FilterForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

class UnitForm(FlaskForm):
    income = IntegerField('rent', validators=[])

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(UnitForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

    def loadFormFromUnit(self, unit):
        self.rent.data = unit.income
