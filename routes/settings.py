from fastapi import HTTPException, Request
from lib.app import app
from databases.firebase.firebase import firebase
import databases.user_db
from firebase_admin._auth_utils import UserNotFoundError
import os
import json
from lib.utils import get_authorization_header


@app.get(
    "/get/firebase-settings/",
    status_code=200,
    name="Get Firebase Settings",
    description="Get Firebase Settings used in frontend",
    tags=["Settings"],
)
async def get_firebase_settings(request: Request):
    allowed_ip_addresses = {"127.0.0.1", "::1", "localhost"}
    client_host = request.client.host
    if client_host not in allowed_ip_addresses and False:
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


@app.get(
    "/is-token-valid/",
    status_code=200,
    tags=["Settings"],
)
async def is_token_valid(request: Request):
    if get_authorization_header(request) == None:
        raise HTTPException(status_code=500, detail="Invalid Token!")
    else:
        return {"status": 200}


@app.get(
    "/get-uid-by-token/",
    status_code=200,
    tags=["Settings"],
)
async def get_uid_by_token(request: Request):
    token = get_authorization_header(request)
    if token == None:
        raise HTTPException(status_code=500, detail="Invalid Token!")
    else:
        return {"status": "200", "uid": firebase.get_uid_from_token(token)}


@app.get(
    "/get-name-by-token/",
    status_code=200,
    tags=["Settings"],
)
async def get_name_by_token(request: Request):
    token = get_authorization_header(request)
    if token == None:
        raise HTTPException(status_code=500, detail="Invalid Token!")
    else:
        name = databases.user_db.get_name_by_uid(firebase.get_uid_from_token(token))
        if name == None:
            raise HTTPException(
                status_code=500, detail="User with this token doesn't exists!"
            )
        else:
            return {"status": 200, "name": name}
