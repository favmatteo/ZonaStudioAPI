from fastapi.testclient import TestClient
from main import app
from databases.firebase.firebase import firebase

client = TestClient(app)


def test_create_user():
    user_data = {
        "name": "Marco",
        "surname": "Ginetti",
        "username": "Mirkello",
        "email": "markogin@gmail.com",
        "password": "stringst",
        "age": 14,
        "school_address": "string",
        "school_class": 2,
    }
    username = user_data.get("username")
    response = client.post("/create/student/", json=user_data)
    assert response.status_code == 201
    assert response.json() == {
        "status": 201,
        "message": f"Student '{username}' created",
    }
    firebase.delete_user_by_email(user_data.get("email"))
