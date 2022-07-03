from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config.config import DATABASE_CONNECTION_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def create_database():
    app.app_context().push()
    db.init_app(app)
    db.create_all()

@app.route('/')
def hello():
    return 'Hello!'
