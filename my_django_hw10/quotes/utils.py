import os
from dotenv import load_dotenv  #, dotenv_values
from pymongo import MongoClient


# config = dotenv_values(".env")
load_dotenv()
MONGO_URI = os.getenv("ATLAS_URI")
MONGO_DB_NAME = os.getenv("DB_NAME")


def get_mongodb():
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    return db
