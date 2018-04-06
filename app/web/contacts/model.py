# Import the database object (db) from the main application module
from app import db
from app.web.common import baseModel
from app.web.listings.models.propertyContact import PropertyContact

# Define a User model
class Contact(baseModel.Base):

    __tablename__ = 'contact'
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    property_contacts = db.relationship('PropertyContact', backref='contact', lazy=True)

    def __repr__(self):
        return '%s' % self.name
