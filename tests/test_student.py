from main import app
from databases.firebase.firebase import firebase
import databases.student_db
from tests.main_test import client


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
        "detail": f"Student '{username}' created",
    }

    id = firebase.get_user_id_by_email(email)
    firebase.delete_user_by_id(id)
    databases.student_db.delete_student_by_id(id)


def test_create_user_with_wrong_mail():
    user_data = {
        "name": "Test",
        "surname": "Test",
        "username": "TestPassed",
        "email": "notanemail",
        "password": "TestPassed",
        "age": 14,
        "school_address": "Liceo Scentifico",
        "school_class": 2,
    }
    response = client.post("/create/student/", json=user_data)
    assert response.status_code == 422


def test_create_user_with_wrong_age():
    user_data = {
        "name": "Test",
        "surname": "Test",
        "username": "TestPassed",
        "email": "email@email.it",
        "password": "TestPassed",
        "age": 2,
        "school_address": "Liceo Scentifico",
        "school_class": 2,
    }
    response = client.post("/create/student/", json=user_data)
    assert response.status_code == 422


def test_create_user_with_wrong_class():
    user_data = {
        "name": "Test",
        "surname": "Test",
        "username": "TestPassed",
        "email": "email@email.it",
        "password": "TestPassed",
        "age": 2,
        "school_address": "Liceo Scentifico",
        "school_class": 9,
    }
    response = client.post("/create/student/", json=user_data)
    assert response.status_code == 422


def test_create_user_with_not_all_field():
    user_data = {
        "name": "Test",
        "surname": "Test",
        "username": "TestPassed",
        "email": "email@email.it",
    }
    response = client.post("/create/student/", json=user_data)
    assert response.status_code == 422


def test_delete_user_that_should_pass():
    user_data = {
        "name": "Giovanni",
        "surname": "Verga",
        "username": "Giova",
        "email": "giova@passed.tt",
        "password": "TestPassed",
        "age": 50,
        "school_address": "Liceo Scentifico",
        "school_class": 2,
    }
    email = user_data.get("email")

    response = client.post("/create/student/", json=user_data)
    id = firebase.get_user_id_by_email(email)
    response = client.delete(f"/delete/student/{id}")
    assert response.status_code == 200
    assert response.json() == {
        "detail": f"Student deleted",
    }
