from models.model import app, ImageItems
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)





class ImageScheme(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ImageItems
        load_instance = True
        
image_schema = ImageScheme()
images_schema = ImageScheme(many=True)