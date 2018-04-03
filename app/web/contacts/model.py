# Import the database object (db) from the main application module
from app import db
from app.web.common import baseModel


# Define a User model
class Contact(baseModel.Base):

    __tablename__ = 'contact'

    name = db.Column(db.String(255),  nullable=False)

    def __repr__(self):
        return '%s' % self.name
