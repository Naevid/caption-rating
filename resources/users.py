from flask_restful import Resource, fields, marshal_with
from models import db, UserModel
from parsers import user_args

# Marshalling
userFields = {
    'userID': fields.Integer,
    'email': fields.String
}

# Restful Resrouce
class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201