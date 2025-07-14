from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models import db, VideoModel
from youtube import fetchMetadata

videos_args = reqparse.RequestParser()
videos_args.add_argument("videoID", type=str, required=True)

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

class Videos(Resource):
    @marshal_with(videoFields)
    def get(self, videoID=None):
        if videoID:
            video = VideoModel.query.get(videoID)
            if not video:
                abort(404, "Video not found")
            return video
        else:
            videos = VideoModel.query.all()
            return videos
    
    @marshal_with(videoFields)
    def post(self, videoID):
        metadata = fetchMetadata(videoID)
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
        return video, 201
    
    def delete(self, videoID):
        video = VideoModel.query.get(videoID)
        if not video:
            abort(404, "Video not found")
        db.session.delete(video)
        db.session.commit()
        return {"message": "Video deleted"}
