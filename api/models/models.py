import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    score = db.Column(db.Integer)
    has_cow = db.Column(db.Boolean)
    answer = db.Column(db.String(100))

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255))