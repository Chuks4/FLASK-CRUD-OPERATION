from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practice.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
# app.app_context().push()



class VideoItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return self.name
    





class ImageItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    likes = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return self.name
    






