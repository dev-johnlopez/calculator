from app import api, db
from app.web.listings.model import Listing
from flask.ext.restful import Api, Resource
from flask.ext.restful import fields, marshal_with
#flask_restful.fields



listing_fields = {
    'address': fields.String,
    'listPrice': fields.Integer,
    'arv': fields.Integer,
    'rehabCost': fields.Integer,
    'income': fields.Integer,
    'property_type': fields.String,
    'bedrooms': fields.Integer,
    'bathrooms': fields.String,
    'garage': fields.Integer,
    'square_footage': fields.Integer,
    'year_built': fields.Integer,
    'seller_name': fields.String,
    'seller_email': fields.String,
    'seller_phone': fields.String,
    'uri': fields.Url('listing')
}

class ListingsAPI(Resource):
    @marshal_with(listing_fields)
    def get(self):
        listings = Listing.query.all()
        return listings

    def post(self):
        pass

class ListingAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
