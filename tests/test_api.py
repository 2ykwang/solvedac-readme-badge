from fastapi.testclient import TestClient
from app import create_app

client = TestClient(create_app())

def test_badge_without_user():
    resp = client.get("/api/v1/badge")
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("image/svg+xml")
    assert "사용자를 불러오지 못했습니다" in resp.text


def test_index_page():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "<html" in resp.text.lower()
