from flask import request, Response
from models.model import app, db
from serializers.video_serializers import video_schema, videos_schema
from resources.video_resources import get_all_videos, get_a_video, add_video

# GET ALL VIDEOS
@app.route("/", methods=["GET"])
def all_videos():
    videos = get_all_videos()
    return videos_schema.jsonify(videos)


# GET A SINGLE VIDEO
@app.route("/video/<int:pk>", methods=["GET"])
def single_video(pk):
    video = get_a_video(pk)
    if video:
        return video_schema.jsonify(video)

    else:
        return Response('Video does not exist')
    


# ADD A VIDEO TO THE DATABASE
@app.route("/video/add", methods=["GET", "POST"])
def add_new_video():
    new_video = add_video()
    return videos_schema.jsonify(new_video)
    

# UPDATE A SINGLE VIDEO
@app.route('/video/update/<int:pk>', methods=['GET', "PUT"])
def update_video(pk):
    data = request.json
    video = get_a_video(pk)
    
    if video:
        if video.name:
            video.name = data['name']
            db.session.commit() 
            return video_schema.jsonify(video)
        
    else:
        return Response('Video does not exist')
        


# DELETE A SINGLE VIDEO
@app.route('/video/delete/<int:pk>', methods=('GET', 'DELETE'))
def delete_video(pk):
    video = get_a_video(pk)
    
    if video:
        db.session.delete(video)
        db.session.commit()
        return Response('Video was deleted successfully')
    else:
      return Response('Video does not exist')


# ADD LIKE TO A VIDEO
@app.route('/video/like/<int:pk>', methods=('GET', 'POST'))
def like_a_video(pk):
    video = get_a_video(pk)
    
    if video:
        video.likes += 1
        db.session.commit()
        return video_schema.jsonify(video)
    else:
      return Response('Video does not exist')  

# UNLIKE A SINGLE VIDEO
@app.route('/video/unlike/<int:pk>', methods=('GET', 'DELETE'))
def unlike_a_video(pk):
    video = get_a_video(pk)
    
    if video:
        if video.likes <= 0:
            video.likes = 0
            db.session.commit()
            return video_schema.jsonify(video)
        
        else:
            video.likes -= 1
            db.session.commit()
            return video_schema.jsonify(video)
    else:
      return Response('Video does not exist')



# ADD VIEWS TO A SINGLE VIDEO
@app.route('/video/views/<int:pk>', methods=('GET', 'POST'))
def add_video_views(pk):
    video = get_a_video(pk)
    
    if video:
        video.views += 1
        db.session.commit()
        return video_schema.jsonify(video)
    else:
      return Response('Video does not exist')