from json import loads, dumps

from utils.mongo import db_config
from models.users_model import Users


def update_user(event,context):
    """
        update user name, address, gender, phone number
        as needed by the user
    """

    body = loads(event["body"])

    """"
        pathParameters are returned in dict, so need 
        to parse.
    """
    oid = event["pathParameters"]["oid"]
    update_param = event["pathParameters"]["args"]

   

    db_config()
    selected_note = Users.objects(id=oid)

    if update_param == "name" :
        _name = body["name"]
        selected_note.update(set__name=_name)
        message = "name updated"
        return dumps({"message":message})

    elif update_param == "gender" :
        _gender = body["gender"]
        selected_note.update(set__gender=_gender)
        message = "gender updated"
        return dumps({"message":message})

    elif update_param == "phone" :
        _phone = body["phone_number"]
        selected_note.update(set__phone_number=_phone)
        message = "phone number updated"
        return dumps({"message":message})

    elif update_param == "address":
        _province = body["province"]
        _district = body["district"]
        _town = body["town"]
        selected_note.update(set__address = {
            "province": _province,
            "district": _district,
            "town": _town

        })
        message = "address updated"
        return dumps({"message":message})
    
    else:
        return dumps({"message":"error args"})