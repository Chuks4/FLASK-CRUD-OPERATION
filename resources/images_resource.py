from models.model import ImageItems, db
from flask import request



def get_all_images():
    imgs = ImageItems.query.order_by('id').all()
    return imgs



def get_an_image(pk):
    img = ImageItems.query.get(pk)
    return img

def add_image():
    data = request.json
    new_video = ImageItems(name=data['name'])
    db.session.add(new_video)
    db.session.commit()
    return new_video