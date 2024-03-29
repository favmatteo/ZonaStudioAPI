from fastapi import HTTPException
from lib.app import app
from schemas.student import StudentSignup
from databases.firebase.firebase import firebase
import databases.student_db
from firebase_admin._auth_utils import UserNotFoundError


@app.post(
    "/create/student/",
    status_code=201,
    name="Create Student",
    description="Create new student",
)
async def create_student(student: StudentSignup):
    if databases.student_db.is_username_not_used(username=student.username):
        raise HTTPException(status_code=409, detail="Username already used")

    if firebase.is_email_not_used(email=student.email):
        raise HTTPException(status_code=409, detail="Email already used")

    user = firebase.create_user(
        student.name, student.surname, student.email, student.password
    )
    databases.student_db.create_new_student(
        user.uid,
        student.name,
        student.surname,
        student.username,
        student.age,
        student.school_class,
        student.school_address,
    )
    return {"detail": f"Student '{student.username}' created"}


@app.delete(
    "/delete/student/{id}",
    status_code=200,
    name="Delete Student",
    description="Delete student",
)
async def delete_student(id: str):
    try:
        firebase.delete_user_by_id(id)
        databases.student_db.delete_student_by_id(id)
        return {"detail": f"Student deleted"}
    except UserNotFoundError as err:
        raise HTTPException(status_code=404, detail="User not found")


@app.put(
    "/update/student/{id}",
    status_code=200,
    name="Update a specific student",
    description="Update specific characteristics student",
)
async def update_student(id: str, field: str, value):
    databases.student_db.update_student_info(id, field, value)
