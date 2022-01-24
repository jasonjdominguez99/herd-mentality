from email.policy import default
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    score = db.Column(db.Integer, default=0)
    has_cow = db.Column(db.Boolean, default=False)
    answer = db.Column(db.String(100), default="")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "score": self.score,
            "has_cow": self.has_cow,
            "answer": self.answer
        }

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255))
    has_been_picked = db.column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "has_been_picked": self.has_been_picked
        }