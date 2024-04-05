from fastapi import HTTPException
from lib.app import app
from schemas.helps import FreeHelp
from databases.firebase.firebase import firebase
import databases.user_db
from firebase_admin._auth_utils import UserNotFoundError

@app.post(
    "/create/free-post/",
    status_code=201,
    name="Create new free help",
    description="Create new free help",
    tags=["Help"],
)
async def create_free_help(free_help: FreeHelp):
    print(free_help)