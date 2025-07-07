from flask_restful import reqparse

# Parsers
user_args = reqparse.RequestParser()
user_args.add_argument('email', type=str, required=True)

rating_args = reqparse.RequestParser()
rating_args.add_argument('email', type=str, required=True)
rating_args.add_argument('videoID', type=str, required=True)
rating_args.add_argument('overallRating', type=int, required=True)
rating_args.add_argument('feedback', type=str)
rating_args.add_argument('thumbsUp', type=bool, default=True, required=True)
rating_args.add_argument('videoTimestamp', type=float, required=True)
    # dimension ratings will be added