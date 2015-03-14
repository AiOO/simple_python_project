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
