from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length

#
#
#   DO NOT USE THIS AS A STANDALONE FORM. CSRF IS DISABLED!
#   Temp solution until refactored
#
#

class AddressForm(FlaskForm):
    addressLine1 = StringField('addressLine1', validators=[DataRequired(), Length(min=0, max=255)])
    addressLine2 = StringField('addressLine2', validators=[Length(min=0, max=255)])
    addressLine3 = StringField('addressLine3', validators=[Length(min=0, max=255)])
    city = StringField('city', validators=[DataRequired(), Length(min=0, max=255)])
    state = SelectField('state', choices=[  ("", ""),
                                            ("AL", "AL"),
                                            ("AK", "AK"),
                                            ("AZ", "AZ"),
                                            ("AR", "AR"),
                                            ("CA", "CA"),
                                            ("CO", "CO"),
                                            ("CT", "CT"),
                                            ("DE", "DE"),
                                            ("FL", "FL"),
                                            ("GA", "GA"),
                                            ("HI", "HI"),
                                            ("ID", "ID"),
                                            ("IL", "IL"),
                                            ("IN", "IN"),
                                            ("IA", "IA"),
                                            ("KS", "KS"),
                                            ("KY", "KY"),
                                            ("LA", "LA"),
                                            ("ME", "ME"),
                                            ("MD", "MD"),
                                            ("MA", "MA"),
                                            ("MI", "MI"),
                                            ("MN", "MN"),
                                            ("MS", "MS"),
                                            ("MO", "MO"),
                                            ("MT", "MT"),
                                            ("NE", "NE"),
                                            ("NV", "NV"),
                                            ("NH", "NH"),
                                            ("NJ", "NJ"),
                                            ("NM", "NM"),
                                            ("NY", "NY"),
                                            ("NC", "NC"),
                                            ("ND", "ND"),
                                            ("OH", "OH"),
                                            ("OK", "OK"),
                                            ("OR", "OR"),
                                            ("PA", "PA"),
                                            ("RI", "RI"),
                                            ("SC", "SC"),
                                            ("SD", "SD"),
                                            ("TN", "TN"),
                                            ("TX", "TX"),
                                            ("UT", "UT"),
                                            ("VT", "VT"),
                                            ("VA", "VA"),
                                            ("WA", "WA"),
                                            ("WV", "WV"),
                                            ("WI", "WI"),
                                            ("WY", "WY")],
        validators=[DataRequired()])
    postalCode = StringField('postalcode', validators=[DataRequired(), Length(min=0, max=5)])

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(AddressForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

    def loadFormFromAddress(self, address):
        self.addressLine1.data = address.addressLine1
        self.addressLine2.data = address.addressLine2
        self.addressLine3.data = address.addressLine3
        self.city.data = address.city
        self.state.data = address.state
        self.postalCode.data = address.postalCode
