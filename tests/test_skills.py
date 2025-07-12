import pytest


def test_create_skill(client):
    response = client.post("/skills", json={"name": "Python"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Python"
    assert "id" in data

def test_get_all_skills(client):
    # Create 2 skills
    client.post("/skills", json={"name": "Java"})
    client.post("/skills", json={"name": "C++"})

    response = client.get("/skills")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 2

def test_get_skill_by_id(client):
    # Create a skill
    response = client.post("/skills", json={"name": "Go"})
    skill_id = response.get_json()["id"]

    # Get it
    response = client.get(f"/skills/{skill_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Go"

def test_update_skill(client):
    # Create a skill
    response = client.post("/skills", json={"name": "Rust"})
    skill_id = response.get_json()["id"]

    # Update it
    response = client.put(f"/skills/{skill_id}", json={"name": "RustLang"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "RustLang"

def test_delete_skill(client):
    # Create a skill
    response = client.post("/skills", json={"name": "Scala"})
    skill_id = response.get_json()["id"]

    # Delete it
    response = client.delete(f"/skills/{skill_id}")
    assert response.status_code == 204

    # Try to get it
    response = client.get(f"/skills/{skill_id}")
    assert response.status_code == 404

def test_get_nonexistent_skill(client):
    response = client.get("/skills/99999")
    assert response.status_code == 404

def test_create_skill_with_invalid_data(client):
    response = client.post("/skills", json={})  # missing 'name'
    assert response.status_code in (400, 422)  # depends on your error handling

def test_update_skill_with_invalid_id(client):
    response = client.put("/skills/99999", json={"name": "NewName"})
    assert response.status_code == 404
