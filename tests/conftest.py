from pytest import fixture, yield_fixture

from spp.app import app
from spp.db import db


@fixture
def fx_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'localhost'
    return app


@yield_fixture
def fx_session(fx_app):
    with fx_app.app_context():
        db.create_all()
        yield db.session
        db.drop_all()
