# Import the database object (db) from the main application module
from app import db
from app.web.models import baseModel


# Define a User model
class Property(baseModel.Base):

    __tablename__ = 'property'

    address = db.relationship("Address", uselist=False, back_populates="property")
    listPrice    = db.Column(db.Integer)
    purchasePrice    = db.Column(db.Integer)
    downPayment    = db.Column(db.Integer)
    interestRate    = db.Column(db.Numeric(2,4))

    #array of units

    #Average time of no revenue
    vacancyRate = db.Column(db.Numeric(3,4))

    #General Expenses
    taxes = db.Column(db.Integer)
    insurancePremiums = db.Column(db.Integer)
    propertyManagementFee = db.Column(db.Numeric(3,4))
    capEx = db.Column(db.Numeric(3,4))

    #Monthly Expenses
    maintenance = db.Column(db.Integer)
    hoa = db.Column(db.Integer)
    water = db.Column(db.Integer)
    garbage = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    electricity = db.Column(db.Integer)
    other = db.Column(db.Integer)

    # New instance instantiation procedure
    #def __init__(self, name, address):
    #    self.name = name
    #    self.address = address

    def __repr__(self):
        return '%s' % self.address
