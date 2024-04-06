from fastapi import HTTPException, Request
from lib.app import app
from schemas.token import TokenData
from databases.firebase.firebase import firebase
import databases.student_db
import databases.user_db
from firebase_admin._auth_utils import UserNotFoundError
import os
import json


@app.get(
    "/get/firebase-settings/",
    status_code=200,
    name="Get Firebase Settings",
    description="Get Firebase Settings used in frontend",
    tags=["Settings"],
)
async def get_firebase_settings(request: Request):
    allowed_ip_addresses = {"127.0.0.1", "::1"}
    client_host = request.client.host
    if client_host not in allowed_ip_addresses:
        raise HTTPException(status_code=403, detail="Access forbidden")

    try:
        current_dir = os.path.dirname(__file__)
        relative_path = "../databases/firebase/application.json"
        application_data_path = os.path.join(current_dir, relative_path)
        with open(application_data_path, "r") as file:
            file_content = file.read()
            data = json.loads(file_content)
        return {"detail": data}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Generic Error! Please contact the admin!"
        )


@app.post(
    "/is-token-valid/",
    status_code=200,
    tags=["Settings"],
)
async def is_token_valid(token: TokenData):
    if firebase.is_valid_token(token.token):
        return {"status": 200}
    else:
        raise HTTPException(status_code=500, detail="Invalid Token!")


@app.get(
    "/get-uid-from-token/",
    status_code=200,
    tags=["Settings"],
)
async def get_uid_from_token(token: str):
    if not firebase.is_valid_token(token):
        raise HTTPException(status_code=500, detail="Invalid Token!")
    else:
        return {"status": 200, "uid": firebase.get_uid_from_token(token)}
