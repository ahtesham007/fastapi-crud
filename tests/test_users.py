from app import schemas
from app.config import settings
from jose import jwt

def test_root(client):
    res = client.get('/')
    print(res.json().get('message'))
    assert res.json().get('message') == "Hello World"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        '/users', json={"email": "hell@gmal.com", "password": "1234"})
    new_user = schemas.UserOut(**res.json())
    assert res.status_code == 201
    assert new_user.email == "hell@gmal.com"


def test_login_user(client, test_user):
    res = client.post('/login', data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
 
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id:str = payload.get("user_id")

    assert id == test_user['id']
    assert login_res.token_type == 'bearer '
    assert res.status_code == 200

def test_incorrect_login(client, test_user):
    res = client.post('/login', data={"username": test_user['email'], "password": 'password'})
    assert res.status_code == 403
    assert res.json().get('detail') == 'Invalid Credentials'
