from lib.app import app
from schemas.student import Student
from databases.school_address_db import get_all_school_address
from databases.firebase.firebase import firebase
import databases.student_db


@app.post(
    "/create/student/",
    status_code=201,
    name="Create Student",
    description="Create new student",
)
async def create_student(student: Student):
    user = firebase.create_user(
        student.name, student.surname, student.email, student.password
    )
    databases.student_db.create_new_student(
        user.uid, student.name, student.surname, student.username, student.age
    )
    return {"status": 201, "message": f"Student '{student.username}' created"}
