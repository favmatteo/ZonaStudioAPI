from fastapi import FastAPI
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware


class Api:
    def __init__(self):
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Consente richieste da qualsiasi origine
            allow_credentials=True,
            allow_methods=[
                "GET",
                "POST",
                "PUT",
                "DELETE",
            ],  # Puoi specificare i metodi consentiti
            allow_headers=["*"],  # Consente tutti gli header nelle richieste
        )

    def get_app(self):
        return self.app


class Database:
    def __init__(
        self,
        database: str,
        host: str = "localhost",
        user: str = "admin",
        password: str = "admin",
    ):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )
        self.cursor = self.conn.cursor(buffered=True)

    def execute(self, query: str):
        self.cursor.execute(query)
        self.conn.commit()

    def get_content(self):
        return self.cursor.fetchall()

    def fetch_one(self):
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()


api = Api()
app = api.get_app()

database = Database("ZonaStudio")
