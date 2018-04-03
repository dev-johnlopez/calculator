# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from app.web.common.joinTables import user_to_listing, roles_users
from flask_security import UserMixin



# Define a User model
class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(40))
    current_login_ip = db.Column(db.String(40))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    #Saved Listings
    listings = db.relationship('Listing', secondary=user_to_listing,
        backref=db.backref('listings', lazy=True))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.listings = []

    def __repr__(self):
        return '%s' % (self.email)
