# Import the database object (db) from the main application module
from app import db
from app.web.models import baseModel
from flask_security import RoleMixin

class Role(baseModel.Base, RoleMixin):
    __tablename__ = 'role'
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
