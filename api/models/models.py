from email.policy import default
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    score = db.Column(db.Integer, default=0)
    has_cow = db.Column(db.Boolean, default=False)
    answer = db.Column(db.String(100), default="")

    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        self.score = 0
        self.has_cow = False
        self.answer = ""

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

    def __init__(self, id, question):
        super().__init__()
        self.id = id
        self.question = question
        self.has_been_picked = False

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "has_been_picked": self.has_been_picked
        }