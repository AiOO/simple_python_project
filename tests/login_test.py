from flask import url_for
from spp.model import User


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
