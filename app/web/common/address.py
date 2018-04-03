# Import the database object (db) from the main application module
from app import db
from app.web.common import baseModel
from app.web.util.geocode import get_google_results


# Define a User model
class Address(baseModel.Base):

    __tablename__ = 'address'

    #relationships
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'))
    listing = db.relationship("Listing", back_populates="address")

    # Physical Address
    addressLine1    = db.Column(db.String(255),  nullable=False)
    addressLine2    = db.Column(db.String(255),  nullable=True)
    addressLine3    = db.Column(db.String(255),  nullable=True)
    city            = db.Column(db.String(255),  nullable=False)
    state           = db.Column(db.String(255),  nullable=False)
    postalCode      = db.Column(db.String(255),  nullable=False)

    # Geocoded Coordinates
    longitude = db.Column(db.Numeric(18,13))
    latitude = db.Column(db.Numeric(15,13))




    # New instance instantiation procedure
    # TODO - https://parserator.datamade.us/usaddress - address standardization
    # TODO - Do geocoding in init function
    #def __init__(self, addressLine1, addressLine2, addressLine3, city, state, postalCode):
    #    self.addressLine1 = addressLine1
    #    self.addressLine2 = addressLine2
    #    self.addressLine3 = addressLine3
    #    self.city = city
    #    self.state = state
    #    self.postalCode = postalCode

    def __init__(self, **kwargs):
        super(Address, self).__init__(**kwargs)
        #TODO - Format **kwargs and pass into the get_google_results function
        geoInfo = get_google_results("2820 N Greenview Ave, Chicago, IL 60657")
        if geoInfo is not None:
            self.latitude = geoInfo['latitude']
            self.longitude = geoInfo['longitude']

    def __repr__(self):
        if self.addressLine2 is None:
                return '%s, %s, %s %s' % (self.addressLine1, self.city, self.state, self.postalCode)
        return '%s %s, %s, %s %s' % (self.addressLine1, self.addressLine2, self.city, self.state, self.postalCode)
