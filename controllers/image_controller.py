from resources.images_resource import get_all_images, get_an_image
from serializers.image_serializers import image_schema, images_schema
from models.model import db, app
from flask import request, Response


# GET ALL IMAGES
@app.route('/images', methods=['GET', 'POST'])
def all_images():
    imgs = get_all_images()
    return images_schema.jsonify(imgs)



# GET AN IMAGE
@app.route('/images/<int:pk>', methods=['GET'])
def single_image(pk):
    img = get_an_image(pk)
    if img:
        return image_schema.jsonify(img)
    else:
      return Response('Image does not exist')
    
    
    
# ADD SINGLE IMAGE
@app.route('/images/add', methods=('GET', 'POST'))
def add_new_image():
    new_img = add_new_image()
    return image_schema.jsonify(new_img)


# UPDATE A SINGLE IMAGE
@app.route('/images/update/<int:pk>', methods=('GET', 'PUT'))
def update_image(pk):
    data = request.json
    img = get_an_image(pk)
    
    if img:
        if img.name:
            img.name = data['name']
            db.session.commit()
            return image_schema.jsonify(img)
    else:
      return Response('Image does not exist')
    



# DELETE AN IMAGE
@app.route('/images/delete/<int:pk>', methods=['GET', 'DELETE'])
def delete_img(pk):
    img = get_an_image(pk)
    
    if img:
        db.session.delete(img)
        db.session.commit()   
        return Response('Image was deleted successfully')
    else:
      return Response('Image does not exist')
    

# LIKE AN IMAGE
@app.route('/images/like/<int:pk>', methods=['GET', 'POST'])
def add_like(pk):
    img = get_an_image(pk)
    
    if img:
        img.likes += 1
        db.session.commit()
        return image_schema.jsonify(img)
    else:
      return Response('Image does not exist')
    
    

# UNLIKE AN IMAGE
@app.route('/images/unlike/<int:pk>', methods=['GET', 'DELETE'])
def remove_like(pk):
    img = get_an_image(pk)
    
    if img:
        if img.likes <= 0:
            img.likes = 0
            db.session.commit()
            return image_schema.jsonify(img)
        else:
            img.likes -= 1
            db.session.commit()
            return image_schema.jsonify(img)
    else:
      return Response('Image does not exist')
    

    


# ADD VIEWS
@app.route('/images/views/<int:pk>', methods=['GET', 'POST'])
def add_image_views(pk):
    img = get_an_image(pk)
    
    if img:
        img.views += 1
        db.session.commit()
        return image_schema.jsonify(img)
    else:
        return Response('Image does not exist')