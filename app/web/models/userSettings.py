from app import db
from app.web.models import baseModel, user

# Define a UserSettings model
class UserSettings(baseModel.Base):

    __tablename__ = 'usersettings'

    #relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #user = db.relationship("User", back_populates="settings")
