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
