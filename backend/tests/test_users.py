import pytest
from jose import jwt
from app import schemas
from app.config import settings


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "email": "test@example.com",
            "password": "password",
        },
    )
    new_user = schemas.UserOut(**response.json())
    assert response.status_code == 201
    assert new_user.email == "test@example.com"


def test_login_user(client, test_user):
    res = client.post(
        "/login",
        data={
            "username": test_user["email"],
            "password": test_user["password"],
        },
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, SECRET_KEY, algorithms=[ALGORITHM])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        (
            "wrongemail.@example.com",
            "password",
            403,
        ),
        (
            "test@example.com",
            "wrongpassword",
            403,
        ),
        (
            "wrongemail@example.com",
            "wrongpassword",
            403,
        ),
        (
            None,
            "password",
            422,
        ),
        (
            "test@example.com",
            None,
            422,
        ),
    ],
)
def test_invalid_login(client, test_user, email, password, status_code):
    res = client.post(
        "/login",
        data={
            "username": email,
            "password": password,
        },
    )
    assert res.status_code == status_code
