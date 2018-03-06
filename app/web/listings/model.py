# Import the database object (db) from the main application module
from app import db
from app.web.common import baseModel, address


# Define a User model
class Listing(baseModel.Base):

    __tablename__ = 'listing'

    address = db.relationship("Address", uselist=False, back_populates="listing")
    listPrice    = db.Column(db.Integer)
    arv    = db.Column(db.Integer)
    rehabCost = db.Column(db.Integer)
    income = db.Column(db.Integer)
    property_type = db.Column(db.String(255),  nullable=True)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    garage = db.Column(db.Integer)
    square_footage = db.Column(db.Integer)
    year_built = db.Column(db.Integer)
    seller_name = db.Column(db.String(255),  nullable=True)
    seller_phone = db.Column(db.String(255),  nullable=True)
    seller_email = db.Column(db.String(255),  nullable=True)

    def __repr__(self):
        return '%s' % self.address
