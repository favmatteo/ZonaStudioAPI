from fastapi import HTTPException
from lib.app import app
from schemas.student import StudentSignup
from databases.firebase.firebase import firebase
import databases.school_address_db
from firebase_admin._auth_utils import UserNotFoundError


@app.get(
    "/get/schoolAddresses/",
    status_code=200,
    name="Get all school addresses",
    description="Get school address like 'Scientifico', 'Classico', 'Informatica', etc",
)
async def get_school_addresses():
    return {
        "detail": "All school addresses",
        "data": databases.school_address_db.get_all_school_address(),
    }
