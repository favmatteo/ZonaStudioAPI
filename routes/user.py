from lib.app import app
from schemas.student import Student
from databases.school_address_db import get_all_school_address
from databases.firebase.firebase import firebase


@app.post(
    "/create/student/",
    status_code=201,
    name="Create Student",
    description="Create new student",
)
async def create_student(student: Student):
    firebase.create_user(student.name, student.surname, student.email, student.password)
    return {"status": 201, "message": f"Student '{student.username}' created"}
