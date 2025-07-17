import pytest

def test_create_employee(client):
    response = client.post("/employees", json={"name": "Alice", "surname": "Smith"})
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data

def test_get_employees(client):
    client.post("/employees", json={"name": "Bob", "surname": "Jones"})
    response = client.get("/employees")
    assert response.status_code == 200
    assert len(response.get_json()) >= 1

def test_create_employee_invalid(client):
    response = client.post("/employees", json={"name": ""})
    assert response.status_code == 400

def test_search_employee(client):
    client.post("/employees", json={"name": "Charlie", "surname": "Brown"})
    response = client.get("/employees/search?q=Charlie")
    assert response.status_code == 200
    results = response.get_json()
    assert any(emp["name"] == "Charlie" for emp in results)
