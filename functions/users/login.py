from json import dumps, loads

from werkzeug.security import check_password_hash

from models.users_model import Users
from utils.mongo import db_config


def login(event, context):
    body = loads(event["body"])
    _email = body["email"]
    _password = body["password"]

    db_config()
    global logged_user
    logged_user = Users.objects.get(email=_email)

    if _email == logged_user["email"] and check_password_hash(
        logged_user["password"], _password
    ):
        # print(type(jwt.encode({"id":logged_user["id"]},"thisisnotakey",algorithm="HS256")))

        return dumps({"message": "User logged in successfully."})
    else:
        return dumps({"message": "Invalid email or password"})


def check_login():
    return logged_user
