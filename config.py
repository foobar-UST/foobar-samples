import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

# Intialize admin sdk
_cred = credentials.Certificate('./serviceAccount.json')
admin = firebase_admin.initialize_app(_cred)
db = firestore.client()