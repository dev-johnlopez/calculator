from app import db
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired
from app.web.util.enum.zone_type import ZoneType

class ZoneForm(FlaskForm):
    zone_type = SelectField("Type", choices=ZoneType.choices(), coerce=ZoneType.coerce, validators=[DataRequired()])
    zone_code = StringField('Code', validators=[DataRequired()])

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(ZoneForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)
