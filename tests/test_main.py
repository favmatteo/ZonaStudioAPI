from fastapi.testclient import TestClient
from main import app
from databases.firebase.firebase import firebase
import databases.student_db

client = TestClient(app)


def test_create_user():
    user_data = {
        "name": "Test",
        "surname": "Test",
        "username": "TestPassed",
        "email": "test@passed.tt",
        "password": "TestPassed",
        "age": 14,
        "school_address": "Liceo Scentifico",
        "school_class": 2,
    }
    username = user_data.get("username")
    email = user_data.get("email")
    
    response = client.post("/create/student/", json=user_data)
    assert response.status_code == 201
    assert response.json() == {
        "status": 201,
        "message": f"Student '{username}' created",
    }

    id = firebase.get_user_id_by_email(email)
    firebase.delete_user_by_id(id)
    databases.student_db.delete_student(id)
