from pydantic import BaseModel
import pytest


class AccessTokenRequest(BaseModel):
    access_token: str

class User(BaseModel):
    id: int
    first_name: str
    last_name: str


def test_access_token_required():
    request = {
        "access_token": "token123"
    }
    AccessTokenRequest(**request)


def test_users_get_response():
    response = [
        {"id": 664, "first_name": "Ivan", "last_name": "Ivanov"},
        {"id": 887, "first_name": "Svetlana", "last_name": "Smirnova"}
    ]
    users = [User(**user) for user in response]

def test_user_lastname_format():
    user = {
        "id": 664,
        "first_name": "Ivan",
        "last_name": "Smirnov"
    }
    with pytest.raises(ValueError):
        User(**user)

def test_access_token_required():
    request = {}
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)

def test_users_get_max_users():
    response = [{"id": i, "first_name": "User", "last_name": str(i)} for i in range(1000)
]
    users = [User(**user) for user in response]
    assert len(users) == 1000
    assert users[-1].id == 999
    assert users[-1].first_name == "User"
    assert users[-1].last_name == "999"

def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)

def test_users_get_one_user():
    response = [{"id": 664, "first_name": "Ivan", "last_name": "Ivanov"}]
    users = [User(**user) for user in response]
    assert len(users) == 1
    assert users[0].id == 664
    assert users[0].first_name == "Ivan"
    assert users[0].last_name == "Ivanov"

def test_users_get_success():
    response = [
        {"id": 664, "first_name": "Ivan", "last_name": "Ivanov"},
        {"id": 887, "first_name": "Svetlana", "last_name": "Smirnova"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 2
    assert users[0].id == 664
    assert users[0].first_name == "Ivan"
    assert users[0].last_name == "Ivanov"


def test_users_get_no_users():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0


def test_user_format():
    user = {
        "id": "invalid_id_format",
        "first_name": "Ivan",
        "last_name": "Ivanov"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_name_format():
    user = {
        "id": 664,
        "first_name": "Petr",
        "last_name": "Ivanov"
    }
    with pytest.raises(ValueError):
        User(**user)

def test_users_get_invalid_response():
    response = [{"invalid_attr": "value"}]
    with pytest.raises(ValueError):
        users = [User(**user) for user in response]

def test_user_lastname_format():
    user = {
        "id": 664,
        "first_name": "Ivan",
        "last_name": "Smirnov"
    }
    with pytest.raises(ValueError):
        User(**user)









