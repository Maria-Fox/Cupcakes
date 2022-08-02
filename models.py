"""Models for Cupcake app."""
from email.policy import default
from importlib.util import set_loader
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
  '''Connect to db.'''
  db.app = app
  db.__init__(app)

default_img = "https://images.unsplash.com/photo-1599785209796-786432b228bc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y3VwY2FrZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"


class Cupcake(db.Model):
  '''Model class for cupcake'''

  def __repr__(self):
    '''Show info about the cupcake including flavor, size, ratin, and image'''

    c = self
    return f"The flavor of the cupcake {c.flavor}, size: {c.size}, rating: {c.rating}, image url: {c.image_url}"

  __tablename__ = "cupcakes"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  flavor = db.Column(db.Text, nullable = False)
  size = db.Column(db.Text, nullable = False)
  rating = db.Column(db.Float, nullable= False)
  image_url= db.Column(db.Text, default = default_img, nullable= False)
