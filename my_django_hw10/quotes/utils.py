import os
from dotenv import load_dotenv  # dotenv_values
from pymongo import MongoClient


# config = dotenv_values(".env")
load_dotenv()
ATLAS_URI = os.getenv("ATLAS_URI")
MONGODB_DB_NAME = os.getenv("DB_NAME")
# print(type(MONGODB_DB_NAME))
# print(MONGODB_DB_NAME)


def get_mongodb():
    client = MongoClient(ATLAS_URI)
    db = client.MONGODB_DB_NAME
    return db
