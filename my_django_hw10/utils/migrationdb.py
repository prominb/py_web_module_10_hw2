import os
# from pathlib import Path

import django
from dotenv import load_dotenv  #, dotenv_values
from pymongo import MongoClient


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10_quotes.settings")
django.setup()

from quotes.models import Author, Tag, Quote  # noqa


load_dotenv()
MONGO_URI = os.getenv("ATLAS_URI")
MONGO_DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
# print(client)
db = client[MONGO_DB_NAME]
# print(db)

# absolute_path = Path().cwd()
# path_to_env = absolute_path.parent / ".env"
# config = dotenv_values(path_to_env)
# client = MongoClient(config["ATLAS_URI"])
# database = client[config["DB_NAME"]]
# db = client.database
# db = client.pyweb9hw

authors = db.authors.find()

for author in authors:
    # print(author)
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    # print(quote['tags'])
    tags = []
    for tag in quote['tags']:
        # print(tag)
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    # print(tags)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )

        for tag in tags:
            q.tags.add(tag)
