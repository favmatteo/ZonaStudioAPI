from fastapi import HTTPException, Request
from lib.app import app
from schemas.helper import HelperSignup, HelperEmail
from databases.firebase.firebase import firebase
import databases.helper_db
import databases.user_db
from firebase_admin._auth_utils import UserNotFoundError
from lib.utils import get_authorization_header


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


@app.get(
    "/is-helper/",
    status_code=200,
    name="Is a user an Helper",
    description="Check if user is an helper",
    tags=["Helper"],
)
async def is_helper(request: Request):
    token = get_authorization_header(request)
    if token is None or not firebase.is_valid_token(token):
        raise HTTPException(status_code=500, detail="Invalid Token!")
    uid = firebase.get_uid_from_token(token)
    email = firebase.get_user_by_id(uid).email
    if not firebase.is_email_not_used(email):
        raise HTTPException(status_code=404, detail="Email doesn't exists")
    uid = firebase.get_user_id_by_email(email)
    detail = databases.helper_db.is_user_a_helper(uid)
    return {"status": 200, "is_helper": detail}
