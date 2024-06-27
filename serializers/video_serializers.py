from models.model import app, VideoItems
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VideoItems
        load_instance = True

video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)