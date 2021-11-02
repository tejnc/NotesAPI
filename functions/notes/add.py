from json import loads,dumps
from werkzeug.security import generate_password_hash


from utils.mongo import db_config
from models.notes_model import Notes
from models.users_model import Users

def add_note(event, context):
    """
        Connecting database and adding notes to the 
        database.
    """
    body = loads(event[
"body"])
    _title = body["title"]
    _description = body["description"]
    _status = body["status"]

    db_config()

    new_note = Notes(
        title = _title,
        description = _description,
        status = _status
    )


    new_note.save()
    response = {
        "message":"New note added.",
        "status_code": 200
        }
    return dumps(response)
