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

    def __repr__(self):
        return '%s' % self.address
