from flask_restful import Resource, fields, marshal_with, abort
from models import db, VideoModel
from youtube import fetchMetadata

# Marshalling
videoFields = {
    'videoID': fields.String,
    'title': fields.String,
    'channel': fields.String,
    'duration': fields.Integer,
    'created': fields.DateTime,
    'likes': fields.Integer,
    'views': fields.Integer,
    'captionLikes': fields.Integer,
    'language': fields.String
}

# Restful Resource
class Videos(Resource):
    @marshal_with(videoFields)
    def get(self):
        videos = VideoModel.query.all()
        return videos
    
    @marshal_with(videoFields)
    def post(self, videoID):
        metadata = fetchMetadata
        video = VideoModel(
            videoID = videoID,
            title = metadata['title'],
            channel = metadata['channel'],
            duration = metadata['duration'],
            thumbnail = metadata['thumbnail'],
            created = metadata['created'],
            likes = metadata['likes'],
            views = metadata['views'],
            language = metadata['language']
        )
        db.session.add(video)
        db.session.commit()
        videos = VideoModel.query.all()
        return videos, 201