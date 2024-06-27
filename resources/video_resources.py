from models.model import VideoItems, db
from flask import request


# To get all videos
def get_all_videos():
    videos = VideoItems.query.order_by('id').all()

    return videos


# To get a single video
def get_a_video(pk):
    video = VideoItems.query.get(pk)
    return video


# To Add a video
def add_video():
    data = request.json
    new_video = VideoItems(name=data['name'])
    db.session.add(new_video)
    db.session.commit()
    return new_video
    
