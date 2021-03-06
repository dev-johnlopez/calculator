from app import db
from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask_security import login_required, current_user
from app.web.contacts.model import Contact
from app.web.criteria.models.investment_criteria import InvestmentCriteria
from app.web.criteria.forms.criteria import CriteriaForm
from app.web.contacts.forms.contact import ContactForm
from jinja2 import TemplateNotFound


contacts = Blueprint('contacts', __name__, template_folder="web/contacts", url_prefix='/contacts')

@contacts.route('/all')
@login_required
def all():
    contacts = current_user.getContactsForUser()
    return render_template('web/contacts/all.html',
                           title='View Contacts',
                           contacts=contacts)

@contacts.route('/view/<contact_id>', methods=['GET'])
@login_required
def view(contact_id):
    contact = Contact.query.filter_by(id=contact_id).first()
    return render_template('web/contacts/view.html',
                           title=contact,
                           contact=contact,
                           matching_listings=getMatchingListingsForContact(contact))


@contacts.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact()
        form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contacts.all'))
    elif len(form.errors) > 0:
        flash(form.errors, 'danger')
    #form.createStandardPropertyTypes()
    return render_template('web/contacts/create.html',
                           title='New Contact',
                           form=form)

@contacts.route('/edit/<contact_id>', methods=['GET', 'POST'])
@login_required
def edit(contact_id):
    form = ContactForm()
    contact = Contact.query.filter_by(id=contact_id).first()
    if form.validate_on_submit():
        form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contacts.all'))
    elif len(form.errors) > 0:
        flash(form.errors, 'danger')
    form = ContactForm(obj=contact)
    form.investment_criteria.data = [(c.property_type) for c in contact.investment_criteria]
    return render_template('web/contacts/create.html',
                           title='Edit Contact',
                           form=form)

@contacts.route('/delete/<contact_id>', methods=['GET', 'POST'])
@login_required
def delete(contact_id):
    contact = Contact.query.filter_by(id=contact_id).first()
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts.all'))



def getMatchingListingsForContact(contact):
    return current_user.listings
