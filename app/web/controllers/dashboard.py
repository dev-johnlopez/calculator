from flask import Blueprint, render_template, abort
from flask_security import login_required, current_user
from jinja2 import TemplateNotFound
from app.web.models.property import Property

dashboard = Blueprint('dashboard', __name__, template_folder="web/dashboard")

@dashboard.route('/')
@dashboard.route('/index')
@login_required
def index():
    return render_template('web/dashboard/home.html',
                           title='Home',
                           properties=Property.query.filter_by(create_user_id=current_user.id),
                           user=current_user)
