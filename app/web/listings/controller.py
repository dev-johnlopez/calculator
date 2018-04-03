from app import db
from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask_security import login_required, current_user
from app.web.listings.forms import ListingForm
from app.web.listings.model import Listing
from app.web.common.address import Address
from jinja2 import TemplateNotFound


listings = Blueprint('listings', __name__, template_folder="web/listings", url_prefix='/listings')

@listings.route('/all')
@login_required
def all():
    listings = Listing.query.all()
    return render_template('web/listings/all.html',
                           title='View Listings',
                           listings=listings)

@listings.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ListingForm()
    if form.validate_on_submit():
        listing = Listing()
        address = Address()
        listing.address = address
        form.populate_obj(listing)
        db.session.add(listing)
        db.session.commit()
        return redirect(url_for('listings.all'))
    return render_template('web/listings/create.html',
                           title='New Listing',
                           form=form)

@listings.route('/edit/<listing_id>', methods=['GET', 'POST'])
@login_required
def edit(listing_id):
    form = ListingForm()
    listing = Listing.query.filter_by(id=listing_id).first()
    if form.validate_on_submit():
        form.populate_obj(listing)
        db.session.add(listing)
        db.session.commit()
        return redirect(url_for('listings.all'))
    form = ListingForm(obj=listing)
    return render_template('web/listings/create.html',
                           title='Edit Listing',
                           form=form)

@listings.route('/delete/<listing_id>', methods=['GET', 'POST'])
@login_required
def delete(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()
    db.session.delete(listing)
    db.session.commit()
    return redirect(url_for('listings.all'))

@listings.route('/save/<listing_id>', methods=['GET', 'POST'])
@login_required
def save(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()
    current_user.listings.append(listing)
    db.session.add(current_user)
    db.session.commit()
    return redirect(url_for('listings.all'))

@listings.route('/saved', methods=['GET', 'POST'])
@login_required
def saved_listings():
    listings = current_user.listings
    return render_template('web/listings/all.html',
                           title='Saved Listings',
                           listings=listings)

@listings.route('/my_listings', methods=['GET', 'POST'])
@login_required
def my_listings():
    listings = Listing.query.filter_by(create_user_id=current_user.id)
    return render_template('web/listings/all.html',
                           title='My Listings',
                           listings=listings)
