from flask import url_for
from pytest import fixture, raises
from sqlalchemy.exc import IntegrityError

from spp.model import User


@fixture
def fx_user(fx_session):
    user = User(name='bright')
    fx_session.add(user)
    fx_session.commit()
    return user


def test_create_user(fx_session):
    username = 'bright'
    fx_session.add(User(name=username))
    fx_session.commit()
    user = fx_session.query(User).filter(User.name == username).first()
    assert user
    assert user.id
    assert user.name
    assert user.created_at
    assert user.name == username


def test_fail_create_user(fx_session):
    fx_session.add(User())
    with raises(IntegrityError):
        fx_session.commit()


def test_create_duplicated_user(fx_user, fx_session):
    fx_session.add(User(name=fx_user.name))
    with raises(IntegrityError):
        fx_session.commit()


def test_web_create_user(fx_app, fx_session):
    username = 'bright'
    with fx_app.test_request_context():
        url = url_for('create_user')
    with fx_app.test_client() as client:
        payload = {
            'username': username
        }
        response = client.post(url, data=payload)
        assert response.status_code == 201
    user = fx_session.query(User).filter(User.name == username).first()
    assert user


def test_web_fail_create_user(fx_app, fx_session):
    username = 'bright'
    with fx_app.test_request_context():
        url = url_for('create_user')
    with fx_app.test_client() as client:
        payload = {}
        response = client.post(url, data=payload)
        assert response.status_code == 400



def test_web_create_duplicated_user(fx_app, fx_session, fx_user):
    with fx_app.test_request_context():
        url = url_for('create_user')
    with fx_app.test_client() as client:
        payload = {
            'username': fx_user.name
        }
        response = client.post(url, data=payload)
        assert response.status_code == 202
