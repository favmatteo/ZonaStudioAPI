import firebase_admin
from firebase_admin import auth

import os


class Firebase:
    def __init__(self):
        credentials_dict = {
            "type": os.getenv("type"),
            "project_id": os.getenv("project_id"),
            "private_key_id": os.getenv("private_key_id"),
            "private_key": os.getenv("private_key").replace(
                "\\n", "\n"
            ),  # Replace escaped newlines with actual newlines
            "client_email": os.getenv("client_email"),
            "client_id": os.getenv("client_id"),
            "auth_uri": os.getenv("auth_uri"),
            "token_uri": os.getenv("token_uri"),
            "auth_provider_x509_cert_url": os.getenv("auth_provider_x509_cert_url"),
            "client_x509_cert_url": os.getenv("client_x509_cert_url"),
            "universe_domain": os.getenv("universe_domain"),
        }

        try:
            # Create a Firebase credentials object using the dictionary
            cred = firebase_admin.credentials.Certificate(credentials_dict)

            # Initialize the Firebase app with the credentials
            self.app = firebase_admin.initialize_app(cred)
        except Exception as e:
            print("Error initializing Firebase app:", e)

    def create_user(self, name: str, surname: str, email: str, password: str):
        user = auth.create_user(
            email=email,
            email_verified=False,
            phone_number=None,
            password=password,
            display_name=f"{name} {surname}",
            photo_url="http://www.example.com/12345678/photo.png",
            disabled=False,
        )
        return user

    def get_all_users(self):
        return auth.list_users().users

    def get_user_by_id(self, id):
        return auth.get_user(id)

    def get_user_by_email(self, email):
        return auth.get_user_by_email(email)

    def get_user_id_by_email(self, email):
        return self.get_user_by_email(email).uid

    def is_valid_token(self, token):
        try:
            decoded_token = auth.verify_id_token(token)
            return True
        except Exception as e:
            return False

    def get_uid_from_token(self, token):
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
            return uid
        except ValueError as e:
            print("Error verifying token:", e)
            return None

    def is_email_not_used(self, email):
        try:
            auth.get_user_by_email(email)
            return True
        except auth.UserNotFoundError:
            return False

    def delete_user_by_id(self, id):
        auth.delete_user(id)

    def get_app(self):
        return self.app


firebase = Firebase()
