# Import the database object (db) from the main application module
from app import db
from app.web.common import baseModel
from app.web.util.enum.zone_type import ZoneType

class Zone(baseModel.Base):
    __tablename__ = 'zone'
    investment_criteria_id = db.Column(db.Integer, db.ForeignKey('investment_criteria.id'),
        nullable=False)

    zone_type = db.Column(db.Enum(ZoneType))
    zone_code = db.Column(db.String(255), nullable=True)
