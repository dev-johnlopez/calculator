# Import the database object (db) from the main application module
from app import db
from app.web.models import baseModel

# Define a User model
class Unit(baseModel.Base):

    __tablename__ = 'unit'

    income = db.Column(db.Integer, default=0)

    property_id = db.Column(db.Integer, db.ForeignKey('property.id'),
        nullable=False)

    # New instance instantiation procedure
    #def __init__(self, income):
    #    self.income = income

    def __repr__(self):
        return '%s' % self.income
