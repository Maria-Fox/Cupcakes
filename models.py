"""Models for Cupcake app."""
from email.policy import default
from importlib.util import set_loader
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
  '''Connect to db.'''
  db.app = app
  db.__init__(app)

default_img = "https://tinyurl.com/demo-cupcake"


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
