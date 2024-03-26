import warnings
from fastapi.testclient import TestClient
from main import app
from databases.firebase.firebase import firebase

warnings.filterwarnings("ignore", message="The 'app' shortcut is now deprecated.")

client = TestClient(app)