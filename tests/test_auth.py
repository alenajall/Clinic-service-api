from tests.conftest import client


def test_register_user():
    r = client.post("/api/v1/auth/register", json={
        "full_name": "Test User",
        "email": "test@example.com",
        "password": "testpass123",
        "role": "patient"
    })
    assert r.status_code == 201
    assert r.json()["email"] == "test@example.com"
    assert "hashed_password" not in r.json()


def test_login_user():
    client.post("/api/v1/auth/register", json={
        "full_name": "Login User",
        "email": "login@example.com",
        "password": "testpass123",
        "role": "patient"
    })
    r = client.post("/api/v1/auth/login", data={
        "username": "login@example.com",
        "password": "testpass123"
    })
    assert r.status_code == 200
    assert "access_token" in r.json()


def test_login_wrong_password():
    r = client.post("/api/v1/auth/login", data={
        "username": "login@example.com",
        "password": "wrongpassword"
    })
    assert r.status_code == 401
