# Import the database object (db) from the main application module
from app import db
from app.web.common import baseModel
from app.web.util.enum.property_type import PropertyType
import enum

class InvestmentCriteria(baseModel.Base):
    __tablename__ = 'investment_criteria'
    property_type = db.Column(db.Enum(PropertyType))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'),
        nullable=False)
    zones = db.relationship('Zone', backref='profile', lazy=True, cascade="all, delete-orphan")
