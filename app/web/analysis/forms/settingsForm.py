from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField, StringField
from wtforms.validators import DataRequired, Length, Optional
from app.web.analysis.forms.expenses import ExpenseForm

class SettingsForm(FlaskForm):
    operating_expenses = FieldList(FormField(ExpenseForm))
