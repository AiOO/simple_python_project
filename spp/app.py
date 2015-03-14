from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

from .model import User
from .db import db


app = Flask(__name__)
db.init_app(app)


@app.route('/users/', methods=['POST'])
def create_user():
    username = request.form.get('username')
    db.session.add(User(name=username))
    db.session.commit()
    return '', 201

