from app import db
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, BooleanField, SelectField
from wtforms.validators import DataRequired, Optional
from app.web.criteria.forms.zone import ZoneForm
from app.web.util.enum.property_type import PropertyType
from app.web.criteria.models.zone import Zone

class CriteriaForm(FlaskForm):
    selected = BooleanField('selected', validators=[Optional()])
    property_type = SelectField('property_type', choices=PropertyType.choices(),
                                                    coerce=PropertyType.coerce,
                                                    validators=[Optional()])
    zones = FieldList(FormField(ZoneForm, default=lambda: Zone()))

#def populate_obj(self, contact):
#    if self.selected.data is True:
#        super(FlaskForm, self).populate_obj(contact)
