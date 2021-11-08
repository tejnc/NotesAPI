from json import dumps, loads

from models.users_model import Users
from utils.mongo import db_config


def update_user(event, context):
    """
    update user name, address, gender, phone number
    as needed by the user
    """

    body = loads(event["body"])
    _keys = body.keys()

    """
        pathParameters are returned in dict, so no need
        to parse.
    """
    oid = event["pathParameters"]["oid"]

    db_config()
    selected_note = Users.objects(id=oid)

    if "name" in _keys:
        _name = body["name"]
        selected_note.update(set__name=_name)

    if "gender" in _keys:
        _gender = body["gender"]
        selected_note.update(set__gender=_gender)

    if "phone_number" in _keys:
        _phone = body["phone_number"]
        selected_note.update(set__phone_number=_phone)

    return dumps({"message": "Updated"})
