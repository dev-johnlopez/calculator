# Import the database object (db) from the main application module
from app import db
from app.web.common import baseModel

property_contact_roles = db.Table('contactroles',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('propertycontact_id', db.Integer, db.ForeignKey('propertycontact.id'), primary_key=True)
)

# Define a User model
class PropertyContact(baseModel.Base):

    __tablename__ = 'propertycontact'

    roles = db.relationship('Role', secondary=property_contact_roles, lazy='subquery',
        backref=db.backref('contacts', lazy=True))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'),
        nullable=False)

    def __repr__(self):
        return '%s' % self.address
