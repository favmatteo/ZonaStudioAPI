from fastapi import HTTPException
from lib.app import app
from schemas.helper import HelperSignup
from databases.firebase.firebase import firebase
import databases.helper_db
import databases.user_db
from firebase_admin._auth_utils import UserNotFoundError


@app.post(
    "/create/helper/",
    status_code=201,
    name="Create Helper",
    description="Create new Helper",
    tags=["Helper"],
)
async def create_student(helper: HelperSignup):
    if databases.user_db.is_username_not_used(username=helper.username):
        raise HTTPException(status_code=409, detail="Username already used")

    if firebase.is_email_not_used(email=helper.email):
        raise HTTPException(status_code=409, detail="Email already used")

    user = firebase.create_user(
        helper.name, helper.surname, helper.email, helper.password
    )
    databases.helper_db.create_new_helper(
        user.uid,
        helper.name,
        helper.surname,
        helper.username,
        helper.age,
        helper.school_class,
        helper.school_address,
        helper.educational_level,
    )
    return {"detail": f"Helper '{helper.username}' created"}
