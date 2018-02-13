import os

from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS') or 'config.DevelopmentConfig')

# Setup DB
db = SQLAlchemy(app)

# Setup Blueprints
from app.web.controllers.dashboard import dashboard
from app.web.controllers.deal import deal
from app.web.controllers.settings import settings
app.register_blueprint(dashboard)
app.register_blueprint(deal)
app.register_blueprint(settings)


from app.web.models import userSettings
from app.web.models import user
from app.web.models import role
from app.web.models import address
from app.web.models import property as propertyModel

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, user.User, role.Role)
security = Security(app, user_datastore)

#Setup Mail
mail = Mail(app)

#Setup Admin
admin = Admin(app, name='RE Analyzer', template_mode='bootstrap3')

class ReturnView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('dashboard.index'))

admin.add_view(ModelView(user.User, db.session))
admin.add_view(ModelView(propertyModel.Property, db.session))
admin.add_view(ModelView(address.Address, db.session))
admin.add_view(ModelView(role.Role, db.session))
admin.add_view(ReturnView(name="Exit",endpoint="return"))

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
@app.template_filter('currency')
def currency_filter(s):
    return locale.currency( s, grouping=True )

@app.template_filter('percent')
def percent_filter(s):
    return '%s%%' % s
