from app import db
from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask_security import login_required, current_user
from app.web.contacts.model import Contact
from app.web.criteria.models.investment_criteria import InvestmentCriteria
from app.web.criteria.forms.criteria import CriteriaForm
from app.web.criteria.forms.zone import ZoneForm
from jinja2 import TemplateNotFound


criteria = Blueprint('criteria', __name__, template_folder="web/criteria", url_prefix='/criteria')

@criteria.route('/view/<criteria_id>', methods=['GET'])
@login_required
def view(criteria_id):
    criteria = InvestmentCriteria.query.filter_by(id=criteria_id).first()
    return render_template('web/criteria/view.html',
                           title="Investor Criteria",
                           criteria=criteria)


@criteria.route('/<contact_id>/create', methods=['GET', 'POST'])
@login_required
def create(contact_id):
    form = CriteriaForm()
    if form.validate_on_submit():
        contact = Contact.query.filter_by(id=contact_id).first()
        criteria = InvestmentCriteria()
        form.populate_obj(criteria)
        contact.investment_criteria.append(criteria)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contacts.view', contact_id=contact_id))
    elif len(form.errors) > 0:
        flash(form.errors, 'danger')
    return render_template('web/criteria/create.html',
                           title='Edit Criteria',
                           form=form)

@criteria.route('/edit/<criteria_id>', methods=['GET', 'POST'])
@login_required
def edit(criteria_id):
    form = CriteriaForm()
    criteria = InvestmentCriteria.query.filter_by(id=criteria_id).first()
    if form.validate_on_submit():
        form.populate_obj(criteria)
        db.session.add(criteria)
        db.session.commit()
        return redirect(url_for('contacts.view', contact_id=criteria.contact.id))
    elif len(form.errors) > 0:
        flash(form.errors, 'danger')
    form = CriteriaForm(obj=criteria)
    return render_template('web/criteria/create.html',
                           title='Edit Criteria',
                           form=form)

@criteria.route('/delete/<criteria_id>', methods=['GET', 'POST'])
@login_required
def delete(criteria_id):
    criteria = InvestmentCriteria.query.filter_by(id=criteria_id).first()
    contact = criteria.contact
    db.session.delete(criteria)
    db.session.commit()
    return redirect(url_for('contacts.view', contact_id=contact.id))
