import os

from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask_mail import Mail
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS') or 'config.DevelopmentConfig')

from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Setup DB
db = SQLAlchemy(app)

# Setup Blueprints
from app.web.listings.controller import listings
from app.web.analysis.controller import analysis
from app.web.contacts.controller import contacts
from app.web.criteria.controller import criteria
#from app.web.common.controller import common
app.register_blueprint(listings)
app.register_blueprint(analysis)
app.register_blueprint(contacts)
app.register_blueprint(criteria)
#app.register_blueprint(common)


from app.web.common.joinTables import roles_users, user_to_listing
#from app.web.listings.models.propertyContact import PropertyContact
from app.web.listings.models.listing import Listing
from app.web.auth.models.role import Role
from app.web.auth.models.user import User
from app.web.common.address import Address
from app.web.contacts.model import Contact
from app.web.criteria.models.investment_criteria import InvestmentCriteria
from app.web.criteria.models.zone import Zone


# API Setup
from flask_restful import Api
api = Api(app)

from app.web.listings.api import ListingsAPI, ListingAPI
api.add_resource(ListingsAPI, '/api/v1.0/listings', endpoint = 'listings')
api.add_resource(ListingAPI, '/api/v1.0/listings/<int:id>', endpoint = 'listing')

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

#Setup Mail
mail = Mail(app)

#Setup Admin
admin = Admin(app, name='RE Analyzer', template_mode='bootstrap3')
admin.add_view(ModelView(Listing, db.session))
#admin.add_view(ModelView(PropertyContact, db.session))
admin.add_view(ModelView(Contact, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Address, db.session))
admin.add_view(ModelView(Role, db.session))

class ReturnView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('dashboard.index'))

if not app.debug and os.environ.get('HEROKU') is None:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/recalculator.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('microblog startup')

if os.environ.get('HEROKU') is not None:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('microblog startup')

import locale
locale.setlocale( locale.LC_ALL, '' )

@app.errorhandler(404)
def page_not_found(e):
    if current_user is None:
        return redirect( url_for_security('login') )
    return render_template('web/common/404.html',
                            title='Whoops!')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('web/common/500.html',
                            title='Whoops!')

@app.template_filter('currency')
def currency_filter(s):
    return locale.currency( s, grouping=True )

@app.template_filter('percent')
def percent_filter(s):
    return '%s%%' % s

#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404
