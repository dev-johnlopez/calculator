from app import db
from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask_security import login_required, current_user
from app.web.common.address import Address
from jinja2 import TemplateNotFound


analysis = Blueprint('analysis', __name__, template_folder="web/deal", url_prefix='/analysis')

@analysis.route('/analyze/<listing_id>')
@login_required
def analyze_listing(listing_id):
    return render_template('web/analysis/all.html',
                           title='View Analysis')

@analysis.route('/all')
@login_required
def all():
    return render_template('web/analysis/all.html',
                           title='View Analysis')


@analysis.route('/settings')
@login_required
def settings():
    return render_template('web/analysis/settings.html')
