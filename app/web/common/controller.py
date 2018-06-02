from app import db, app
from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask_security import login_required, current_user, url_for_security
from app.web.listings.forms import ListingForm
from app.web.listings.model import Listing
from app.web.common.address import Address
from jinja2 import TemplateNotFound


common = Blueprint('common', __name__, url_prefix='/')
