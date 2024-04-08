from fastapi import HTTPException, Request, Header
from lib.app import app
from schemas.helps import FreeHelp
from databases.firebase.firebase import firebase
import databases.post_db
from firebase_admin._auth_utils import UserNotFoundError
from lib.utils import get_authorization_header
import databases.tag_db


@app.post(
    "/create/free-post/",
    status_code=201,
    name="Create new free help",
    description="Create new free help",
    tags=["Post"],
)
async def create_free_help(request: Request, free_help: FreeHelp):
    print(free_help)
    token = get_authorization_header(request)
    if token is None:
        raise HTTPException(status_code=500, detail="Invalid Token!")
    databases.post_db.create_free_post(
        free_help.title,
        free_help.description,
        free_help.id_student,
        tags=free_help.tags,
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
    posts = databases.post_db.get_all_post_of_a_user(uid)

    # Raggruppa i tag associati a ciascun post
    posts_with_tags = []
    for post in posts:
        post_id = post[0]
        tags = databases.tag_db.get_tags_for_post(post_id)
        trovato = False
        for post_with_tag in posts_with_tags:
            if post_with_tag[0] == post_id:
                trovato = True
        if not trovato:
            post_list = [el for el in post]
            post_list.pop(-1)
            post_list.append(tags)
            posts_with_tags.append(post_list)

    return {"status": "200", "posts": posts_with_tags}


@app.get("/get/free-post/{id}", status_code=200)
async def get_free_post(id: int):
    post = databases.post_db.get_free_post(id)
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post doesn't exist!")


@app.put("/close/free-post/{id}", status_code=201)
async def close_free_post(id: int):
    databases.post_db.close_free_post(id)
