from tests.conftest import client


def test_list_clinics_returns_200():
    r = client.get("/api/v1/clinics/")
    assert r.status_code == 200


def test_search_clinics_returns_200():
    r = client.get("/api/v1/clinics/search?district=Freetown")
    assert r.status_code == 200


def test_create_clinic_requires_auth():
    r = client.post("/api/v1/clinics/", json={
        "name": "Test Clinic",
        "district": "Western Area",
        "clinic_type": "CHC"
    })
    assert r.status_code == 401


def test_get_nonexistent_clinic_returns_404():
    r = client.get("/api/v1/clinics/99999")
    assert r.status_code == 404
