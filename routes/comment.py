from fastapi import HTTPException, Request, Header
import databases.user_db
from lib.app import app
from schemas.comment import Comment
from databases.firebase.firebase import firebase
import databases.comment_db
import databases.helper_db
from firebase_admin._auth_utils import UserNotFoundError
from lib.utils import get_authorization_header


@app.post(
    "/create/comment-on-free-post/",
    status_code=201,
)
async def create_comment_on_free_post(request: Request, comment: Comment):
    token = get_authorization_header(request)
    if token is None or not firebase.is_valid_token(token):
        raise HTTPException(status_code=500, detail="Invalid Token!")
    # determina se l'utente è student o helper
    uid = firebase.get_uid_from_token(token)
    is_helper = databases.helper_db.is_user_a_helper(uid)
    if is_helper:
        databases.comment_db.create_comment_on_freepost(
            text=comment.text, id_free_post=comment.id_free_post, id_helper=uid
        )
    else:
        databases.comment_db.create_comment_on_freepost(
            text=comment.text, id_free_post=comment.id_free_post, id_student=uid
        )


@app.get("/get/comment-on-free-post/{id_post}", status_code=200)
async def get_comment_on_free_post(id_post: int):
    comment = databases.comment_db.get_comment_on_freepost(id_post)
    if comment:
        for i, c in enumerate(comment):
            c = [el for el in c]
            username = "".join(databases.user_db.get_nickname_by_uid(c[2]))
            c.append(username)
            comment[i] = c
        return {"status": 200, "comments": comment}
    else:
        raise HTTPException(status_code=404, detail="Comments not found!")
