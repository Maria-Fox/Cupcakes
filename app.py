"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models import Cupcake, db, connect_db

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake'
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

#db connection and creation
connect_db(app)
db.create_all()

# serialize into json readable items for API - converts to instances of a dictionary

def serialize(self):
  '''Seralize given item'''
  return {
    "id": self.id,
    "flavor": self.flavor,
    "size": self.size,
    "rating": self.rating,
    "image_url": self.image_url
  }

@app.route("/")
def homepage():
  '''Return homepage'''
  return  render_template("index.html")

@app.route("/api/cupcakes", methods = ["GET"])
def list_cupcakes():
    '''Get data about all cupcakes, response w JSON'''

    all_cupcakes = Cupcake.query.all()
    serialized_cupcakes = [serialize(cupcake) for cupcake in all_cupcakes]

    # returns json ready data dictionairy of serialized cupcakes
    return jsonify(cupcakes = serialized_cupcakes)


@app.route("/api/cupcakes", methods = ["POST"])
def create_cupcake():
    '''Create cupcake instance commit to database'''

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url = request.json["image_url"]

    new_cupcake = Cupcake(flavor = flavor, size = size, rating = rating, image_url= image_url or None)

    db.session.add(new_cupcake)
    db.session.commit()

    return jsonify(cupcake = serialize(new_cupcake))


@app.route("/api/cupckaes/<int:id>")
def get_cupcake(id):
    '''Get data for given cupcake'''

    cupcake = Cupcake.query.get_or_404(id)
    serialized_cupcake = serialize(cupcake)

    return jsonify(cupcake = serialized_cupcake)


@app.route("/api/cupcakes/<int:id>", methods = ["PATCH"])
def update_cupcake(id):
    '''Update given cupcake data'''

    cupcake = Cupcake.get_or_404(id)

# using .get to allow request to set new input OR previous input if no entry upon request
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image_url = request.json.get("image_url", cupcake.image_url)

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(updated_cupcake = serialize(cupcake))


@app.route("/api/cupcakes/<int:id>", methods = ["DELETE"])
def delete_cupcake(id):
    '''Delete cupcake correspponding w/ given id.'''

    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message = {"Deleted": "cupcake"})












