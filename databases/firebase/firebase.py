import firebase_admin
from firebase_admin import auth

import os


class Firebase:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        relative_path = "data.json"
        credentials_path = os.path.join(current_dir, relative_path)
        credentials = firebase_admin.credentials.Certificate(credentials_path)
        self.app = firebase_admin.initialize_app(credentials)

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
    
    def get_user_by_email(self, email):
        return auth.get_user_by_email(email)
    
    def get_user_id_by_email(self, email):
        return self.get_user_by_email(email).uid

    def delete_user_by_id(self, id):
        auth.delete_user(id)

    def get_app(self):
        return self.app


firebase = Firebase()
