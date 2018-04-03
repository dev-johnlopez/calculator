from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Optional

#
#
#   DO NOT USE THIS AS A STANDALONE FORM. CSRF IS DISABLED!
#   Temp solution until refactored
#
#

class ExpenseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=0, max=255)])
