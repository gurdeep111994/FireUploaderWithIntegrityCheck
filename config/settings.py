from dotenv import load_dotenv
import os

load_dotenv()

FIREBASE_CREDENTIALS_PATH = "./credentials/firebase_adminsdk.json"
STORAGE_BUCKET = os.getenv('STORAGE_BUCKET')