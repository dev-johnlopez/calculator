from app import db
from flask_wtf import FlaskForm
from wtforms import Form, FormField, IntegerField, SelectField, FieldList, DecimalField, StringField, widgets, SelectMultipleField
from wtforms.validators import DataRequired, Length, Optional
from app.web.common.forms.addressForm import AddressForm
from app.web.criteria.forms.criteria import CriteriaForm
from app.web.criteria.models.investment_criteria import InvestmentCriteria
from app.web.util.enum.property_type import PropertyType

class ContactForm(FlaskForm):
    first_name = StringField('first_name', validators=[Optional()])
    last_name = StringField('last_name', validators=[Optional()])
    email = StringField('email', validators=[Optional()])
    phone_number = StringField('phone', validators=[Optional()])
    contact_type = SelectField('type', choices=[("",""),
                                                ("Investor", "Investor"),
                                                ("Builder", "Builder"),
                                                ("Wholesaler", "Wholesaler"),
                                                ("Realtor", "Realtor"),
                                                ("Property Manager", "Property Manager"),
                                                ("Lender", "Lender"),
                                                ("Other Professional", "Other Professional")],
                                                validators=[Optional()])
    investment_strategy = SelectField('type', choices=[("",""),
                                                        ("TBD", "TBD"),
                                                        ("Rentals", "Rentals"),
                                                        ("Fix and Flips", "Fix and Flips"),
                                                        ("Land (Builder)", "Land (Builder)")],
                                                        validators=[Optional()])

    investment_criteria = SelectMultipleField('Label', choices=PropertyType.choices(),
                                                            option_widget = widgets.CheckboxInput(),
                                                            widget = widgets.ListWidget(prefix_label=False),
                                                            coerce=PropertyType.coerce)

    #investment_criteria = FieldList(FormField(CriteriaForm))

    def populate_obj(self, contact):
        profiles = []
        for profile in self.investment_criteria.data:
            new_profile = InvestmentCriteria()
            new_profile.property_type = profile
            profiles.append(new_profile)
        self.investment_criteria.data = profiles
        super(FlaskForm, self).populate_obj(contact)
