from app import db
from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask_security import login_required, current_user
from jinja2 import TemplateNotFound
from app.web.forms.deal import DealForm
from app.web.forms.unit import UnitForm
from app.web.models.address import Address
from app.web.models.property import Property
from app.web.models.unit import Unit
from app.web.util.geocode import get_google_results
deal = Blueprint('deal', __name__, template_folder="web/deal", url_prefix='/deal')

@deal.route('/')
@deal.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = DealForm()
    if form.validate_on_submit():
        handleDealForm(None, form)
        return redirect(url_for('dashboard.index'))
    return render_template('web/deal/create.html',
                           title='Home',
                           form=form)

@deal.route('/create/sfr', methods=['GET', 'POST'])
@login_required
def createSFR():
    form = DealForm()
    if form.validate_on_submit():
        handleDealForm(None, form)
        return redirect(url_for('dashboard.index'))
    return render_template('web/deal/create.html',
                           title='Home',
                           form=form)

@deal.route('/create/multiunit', methods=['GET', 'POST'])
@login_required
def createMultiUnit():
    form = DealForm()
    if form.validate_on_submit():
        handleDealForm(None, form)
        return redirect(url_for('dashboard.index'))
    return render_template('web/deal/create.html',
                           title='Home',
                           form=form)

@deal.route('/<property_id>/view', methods=['GET', 'POST'])
@login_required
def view(property_id):
    property = Property.query.filter_by(id=property_id).first()
    form = DealForm()
    if form.validate_on_submit():
        form.populate_obj(property)
        db.session.add(property)
        db.session.commit()
        #handleDealForm(property, form)
    form = DealForm(obj=property)
    #form.loadFormFromProperty(property)
    return render_template('web/deal/view.html',
                           title='View Deal',
                           property=property,
                           form=form)

@deal.route('/<property_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(property_id):
    property = Property.query.filter_by(id=property_id).first()
    for unit in property.units:
        db.session.delete(unit)
    db.session.delete(property)
    db.session.commit()
    return redirect(url_for('dashboard.index'))


# Utility functions
def handleDealForm(property, form):
    address = None
    if property is None:
        property = Property()
        address = Address()
        property.address = address

    address = property.address
    address.addressLine1 = form.address.addressLine1.data
    address.addressLine2 = form.address.addressLine2.data
    address.addressLine3 = form.address.addressLine3.data
    address.city = form.address.city.data
    address.state = form.address.state.data
    address.postalCode = form.address.postalCode.data

    #geocode address
    geoInfo = get_google_results(address)
    if geoInfo is not None:
        address.latitude = geoInfo['latitude']
        address.longitude = geoInfo['longitude']

    #create deal
    property.askingPrice    = form.askingPrice.data
    property.purchasePrice    = form.purchasePrice.data
    property.downPayment    = form.downPayment.data
    property.interestRate    = form.interestRate.data

    #array of units
    for unit in property.units:
        db.session.delete(unit)

    property.units = []
    for unitForm in form.units:
        unit = Unit()
        unit.income = unitForm.income.data
        property.units.append(unit)

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
