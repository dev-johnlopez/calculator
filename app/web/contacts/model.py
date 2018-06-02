# Import the database object (db) from the main application module
from app import db
from app.web.common import baseModel


# Define a User model
class Contact(baseModel.Base):

    __tablename__ = 'contact'
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    property_types = db.Column(db.String(500), nullable=True)
    investment_criteria = db.relationship('InvestmentCriteria', backref='contact', lazy=True, cascade="all, delete-orphan")
    investment_strategy = db.Column(db.String(255), nullable=True)
    contact_type = db.Column(db.String(255), nullable=True)
    #property_contacts = db.relationship('PropertyContact', backref='contact', lazy=True)

    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)
