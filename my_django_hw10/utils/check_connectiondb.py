from pathlib import Path, PurePath

# from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient


# Перетворення відносного шляху в абсолютний
relative_path = Path("check_connectiondb.py")
absolute_path = relative_path.absolute()
# print(absolute_path.parent.parent.parent)
path_to_env = absolute_path.parent.parent.parent / ".env"
# print(path_to_env)
# print("Exists:", path_to_env.exists())
if path_to_env:
    config = dotenv_values(path_to_env)
    # print(type(config))
    # print(config["ATLAS_URI"])
    mongodb_client = MongoClient(config["ATLAS_URI"])
    database = mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")