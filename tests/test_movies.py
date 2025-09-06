import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

# Recreate tables fresh for tests (SQLite file DB; for isolation you can switch to sqlite:///:memory:)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_and_get_movie():
    # Create
    payload = {
        "title": "Inception",
        "director": "Christopher Nolan",
        "releaseYear": 2010,
        "genre": "Sci-Fi",
        "rating": 9.0
    }
    r = client.post("/movies", json=payload)
    assert r.status_code == 201, r.text
    body = r.json()
    assert body["id"] >= 1
    assert body["title"] == "Inception"

    # Get by ID
    movie_id = body["id"]
    r2 = client.get(f"/movies/{movie_id}")
    assert r2.status_code == 200
    body2 = r2.json()
    assert body2["title"] == "Inception"
    assert body2["releaseYear"] == 2010

def test_update_movie():
    # Create new
    r = client.post("/movies", json={"title": "Matrix", "rating": 8.5})
    assert r.status_code == 201
    movie_id = r.json()["id"]

    # Update
    r2 = client.put(f"/movies/{movie_id}", json={"rating": 9.2, "genre": "Action"})
    assert r2.status_code == 200
    body = r2.json()
    assert body["rating"] == 9.2
    assert body["genre"] == "Action"

def test_delete_movie():
    # Create new
    r = client.post("/movies", json={"title": "Temp Movie"})
    assert r.status_code == 201
    movie_id = r.json()["id"]

    # Delete
    r2 = client.delete(f"/movies/{movie_id}")
    assert r2.status_code == 204

    # Verify 404
    r3 = client.get(f"/movies/{movie_id}")
    assert r3.status_code == 404
