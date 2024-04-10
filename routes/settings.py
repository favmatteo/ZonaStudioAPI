from fastapi import HTTPException, Request
from lib.app import app
from databases.firebase.firebase import firebase
import databases.user_db
from firebase_admin._auth_utils import UserNotFoundError
import os
import json
from lib.utils import get_authorization_header


# Lista dei domini consentiti
allowed_domains = [os.getenv("ALLOWED_DOMAIN"), "192.168.1.123"]


@app.get(
    "/get/firebase-settings/",
    status_code=200,
    name="Get Firebase Settings",
    description="Get Firebase Settings used in frontend",
    tags=["Settings"],
)
async def get_firebase_settings(request: Request):
    # Controlla se l'header Referer è presente nella richiesta
    referer = request.headers.get("Referer")
    if not referer:
        raise HTTPException(status_code=403, detail="Access forbidden")

    # Controlla se il dominio del Referer è tra quelli consentiti
    valid_referer = any(domain in referer for domain in allowed_domains)
    if not valid_referer:
        raise HTTPException(status_code=403, detail="Access forbidden")

    try:
        data = {
            "apiKey": os.getenv("apiKey"),
            "authDomain": os.getenv("authDomain"),
            "projectId": os.getenv("projectId"),
            "storageBucket": os.getenv("storageBucket"),
            "messagingSenderId": os.getenv("messagingSenderId"),
            "appId": os.getenv("appId"),
            "measurementId": os.getenv("measurementId"),
        }
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
