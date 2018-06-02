
from app import db
from sqlalchemy.ext.declarative import declared_attr
from flask_security import current_user

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    @declared_attr
    def create_user_id(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id'))
    #create_user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    #date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    #date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
    #                                        onupdate=db.func.current_timestamp())

    def __init__(self):
        super(Base,self).__init__()
        self.create_user_id = current_user.id

    def delete(self):
        db.session.delete(self)
