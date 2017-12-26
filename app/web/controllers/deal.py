from app import db
from flask import Blueprint, render_template, abort, flash
from flask_security import login_required, current_user
from jinja2 import TemplateNotFound
from app.web.forms.deal import DealForm
from app.web.forms.unit import UnitForm
from app.web.models.address import Address
from app.web.models.property import Property
deal = Blueprint('deal', __name__, template_folder="web/deal", url_prefix='/deal')

@deal.route('/')
@deal.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = DealForm()
    if form.validate_on_submit():
        createDealFromForm(form)
    else:
        flash('%s' % current_user)
    form.units.append_entry(UnitForm())
    form.units.append_entry(UnitForm())
    form.units.append_entry(UnitForm())
    form.units.append_entry(UnitForm())
    return render_template('web/deal/create.html',
                           title='Home',
                           form=form)


# Utility functions
def createDealFromForm(form):
    #create address
    address = Address()
    address.addressLine1 = form.address.addressLine1.data
    address.addressLine2 = form.address.addressLine2.data
    address.addressLine3 = form.address.addressLine3.data
    address.city = form.address.city.data
    address.state = form.address.state.data
    address.postalCode = form.address.postalCode.data
    #create deal
    property = Property()
    property.address = address
    property.listPrice    = form.listPrice.data
    property.purchasePrice    = form.purchasePrice.data
    property.downPayment    = form.downPayment.data
    property.interestRate    = form.interestRate.data

    #array of units

    #Average time of no revenue
    property.vacancyRate = form.vacancyRate.data

    #General Expenses
    property.taxes = form.taxes.data
    property.insurancePremiums = form.insurancePremiums.data
    property.propertyManagementFee = form.propertyManagementFee.data
    property.capEx = form.capEx.data

    #Monthly Expenses
    property.maintenance = form.maintenance.data
    property.hoa = form.hoa.data
    property.water = form.water.data
    property.garbage = form.garbage.data
    property.gas = form.gas.data
    property.electricity = form.electricity.data
    property.other = form.other.data

    db.session.add(property)
    db.session.commit()
