from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models import db, UserModel
from parsers import user_args

user_args = reqparse.RequestParser()
user_args.add_argument('email', type=str, required=True)

userFields = {
    'userID': fields.Integer,
    'email': fields.String
}

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
    
class User(Resource):
    @marshal_with(userFields)
    def get(self, userID):
        user = UserModel.query.get(userID)
        if not user:
            abort(404, "User not found")
        return user

    def delete(self, userID):
        user = UserModel.query.get(userID)
        if not user:
            abort(404, "User not found")
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}
    
    def patch(self, userID):
        args = user_args.parse_args()
        user = UserModel.query.get(userID)
        if not user:
            abort(404, "User not found")
        user.email = args["email"]
        db.session.commit()
        return user
        