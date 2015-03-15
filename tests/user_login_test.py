from flask import session, url_for
from pytest import fixture

from spp.model import User


@fixture
def fx_user(fx_session):
    user = User(name='bright')
    fx_session.add(user)
    fx_session.commit()
    return user


def test_web_login_user(fx_app, fx_user):
    with fx_app.test_request_context():
        url = url_for('login_user')
    with fx_app.test_client() as client:
        payload = {
            'username': fx_user.name
        }
        response = client.post(url, data=payload)
        assert response.status_code == 200
        assert 'username' in session
        assert session['username'] == fx_user.name


def test_web_login_user_fail(fx_app):
    with fx_app.test_request_context():
        url = url_for('login_user')
    with fx_app.test_client() as client:
        payload = {}
        response = client.post(url, data=payload)
        assert response.status_code == 400
        assert 'username' not in session


def test_web_login_not_exist_user(fx_app, fx_user):
    username = 'i_am_a_hacker'
    with fx_app.test_request_context():
        url = url_for('login_user')
    with fx_app.test_client() as client:
        payload = {
            'username': username
        }
        response = client.post(url, data=payload)
        assert response.status_code == 401
        if username in session:
            assert session['username'] != username
