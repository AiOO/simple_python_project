from flask import Flask, abort, request, session
from flask.ext.sqlalchemy import SQLAlchemy

from .model import User
from .db import db


app = Flask(__name__)
app.secret_key = 'This is very very secret key.'
db.init_app(app)


@app.route('/users/', methods=['POST'])
def create_user():
    username = request.form.get('username')
    if not username:
        abort(400)
    user = db.session.query(User) \
                     .filter(User.name == username) \
                     .first()
    if user:
        return '', 202
    db.session.add(User(name=username))
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        abort(500)
    return '', 201


@app.route('/login/', methods=['POST'])
def login_user():
    username = request.form.get('username')
    if not username:
        abort(400)
    user = db.session.query(User) \
                     .filter(User.name == username) \
                     .first()
    if not user:
        abort(401)
    session['username'] = user.name
    return ''
