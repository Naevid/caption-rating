from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models import db, RatingModel, UserModel, VideoModel

rating_args = reqparse.RequestParser()
rating_args.add_argument('userID', type=int, required=True)
rating_args.add_argument('videoID', type=str, required=True)
rating_args.add_argument('overallRating', type=int, required=True)
rating_args.add_argument('feedback', type=str, required=False)
rating_args.add_argument('thumbsUp', type=bool, default=True, required=True)
rating_args.add_argument('videoTimestamp', type=float, required=True)

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
    def get(self, ratingID=None):
        if ratingID:
            rating = RatingModel.query.get(ratingID)
            if not rating:
                abort(404, "Rating not found")
            return rating
        else:
            ratings = RatingModel.query.all()
            return ratings
        
    @marshal_with(ratingFields)
    def post(self):
        args = rating_args.parse_args()
        rating = RatingModel(
            userID = args["userID"],
            videoID = args["videoID"],
            overallRating = args["overallRating"],
            feedback = args['feedback'],
            thumbsUp = args['thumbsUp'],
            videoTimestamp = args['videoTimestamp']
        )
        db.session.add(rating)
        db.session.commit()
        return rating, 201
    
    @marshal_with(ratingFields)
    def patch(self, ratingID):
        args = rating_args.parse_args()
        rating = RatingModel.query.get(ratingID)
        if not rating:
            abort(404, "Rating not found")
        rating.overallRating = args["overallRating"]
        rating.feedback = args["feedback"]
        rating.thumbsUp = args["thumbsUp"]
        db.session.commit()
        return rating
    
    def delete(self, ratingID):
        rating = RatingModel.query.get(ratingID)
        if not rating:
            abort(404, "Rating not found")
        db.session.delete(rating)
        db.session.commit()
        return {"message": "Rating deleted successfully"}, 200
        
