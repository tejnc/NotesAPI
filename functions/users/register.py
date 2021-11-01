from json import loads, dumps
from werkzeug.security import generate_password_hash

from utils.mongo import db_config
from models.users_model import Users

def add_user(event, context):
    """
        registering user 
    """
    body = loads(event["body"])
    _name = body["name"]
    _gender = body["gender"]
    _phone_number = body["phone_number"]
    _province = body["province"]
    _district = body["district"]
    _town = body["town"]
    _email = body["email"]
    _password = body["password"]

    _hashed_password = generate_password_hash(_password)

    db_config()

    new_user = Users(
        name = _name,
        gender = _gender,
        phone_number = _phone_number,
        address = {
            "province":_province,
            "district":_district,
            "town":_town
        },
        email = _email,
        password = _hashed_password
    )
    new_user.save()

    return dumps({"message":"User added successfully."})