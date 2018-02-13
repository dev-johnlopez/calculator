from app import db
from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask_security import login_required, current_user
from jinja2 import TemplateNotFound

settings = Blueprint('settings', __name__, template_folder="web/homne", url_prefix='/settings')

@settings.route('/')
@login_required
def index():
    return render_template('web/settings/settings.html',
                           title='Settings')
