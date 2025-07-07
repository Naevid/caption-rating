from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from resources.users import Users
from resources.videos import Videos
from resources.ratings import Ratings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

from models import db

    
api.add_resource(Users, '/api/users/')
api.add_resource(Videos, '/api/videos/')
api.add_resource(Ratings, '/api/ratings/')


@app.route("/")
def home ():
    return "Testing 123"

if __name__ == '__main__':
    app.run(debug=True)