from fastapi import Request


def get_authorization_header(request: Request):
    authorization_header = request.headers.get("Authorization")
    if authorization_header is None or not authorization_header.startswith("Bearer "):
        return None
    else:
        return authorization_header.split("Bearer ")[1]
