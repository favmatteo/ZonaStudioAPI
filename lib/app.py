from fastapi import FastAPI
import mysql.connector


class Api:
    def __init__(self):
        self.app = FastAPI()

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
        self.cursor = self.conn.cursor()

    def execute(self, query: str):
        self.cursor.execute(query)

    def get_content(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()




api = Api()
app = api.get_app()

database = Database("ZonaStudio")
