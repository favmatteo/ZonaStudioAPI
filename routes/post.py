from fastapi import HTTPException, Request, Header
from lib.app import app
from schemas.helps import FreeHelp
from databases.firebase.firebase import firebase
import databases.post_db
from firebase_admin._auth_utils import UserNotFoundError
from lib.utils import get_authorization_header


@app.post(
    "/create/free-post/",
    status_code=201,
    name="Create new free help",
    description="Create new free help",
    tags=["Post"],
)
async def create_free_help(request: Request, free_help: FreeHelp):
    token = get_authorization_header(request)
    if token is None:
        raise HTTPException(status_code=500, detail="Invalid Token!")
    databases.post_db.create_free_post(
        free_help.title, free_help.description, free_help.id_student
    )


@app.get(
    "/get/all-my-post/",
    status_code=200,
)
async def get_all_my_post(request: Request):
    token = get_authorization_header(request)
    if token is None or not firebase.is_valid_token(token):
        raise HTTPException(status_code=500, detail="Invalid Token!")
    uid = firebase.get_uid_from_token(token)
    return {"status": "200", "posts": databases.post_db.get_all_post_of_a_user(uid)}


@app.get("/get/free-post/{id}", status_code=200)
async def get_free_post(id: int):
    post = databases.post_db.get_free_post(id)
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post doesn't exist!")
