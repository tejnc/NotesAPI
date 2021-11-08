import os

from mongoengine import connect


def get_db_connection():
    url = "mongodb+srv://test:{}@cluster0.x25kn.mongodb.net/{}?retryWrites=true&w=majority".format(
        os.environ["DB_PASS"], os.environ["DB"]
    )
    return url


def db_config():
    try:
        uri: str = get_db_connection()
        connect(host=uri)
    except KeyError:
        connect("mongoenginetest", host="mongomock://localhost")
