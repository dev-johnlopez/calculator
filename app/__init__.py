from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object('config')

# Setup DB
db = SQLAlchemy(app)

# Setup Blueprints
from app.web.controllers.dashboard import dashboard
from app.web.controllers.deal import deal
app.register_blueprint(dashboard)
app.register_blueprint(deal)


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
admin.add_view(ReturnView(name="Exit",endpoint="return"))
