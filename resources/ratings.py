from flask_restful import Resource, fields, marshal_with, abort
from models import db, RatingModel
from parsers import rating_args

#Marshalling
ratingFields = {
    'ratingID': fields.Integer,
    'userID': fields.Integer,
    'videoID': fields.String,
    'overallRating': fields.Integer,
    'feedback': fields.String,
    'thumbsUp': fields.Boolean,
    'submittedAt': fields.DateTime,
    'videoTimestamp': fields.Integer,
}

class Ratings(Resource):
    @marshal_with(ratingFields)
    def get(self):
        ratings = RatingModel.query.all()
        return ratings