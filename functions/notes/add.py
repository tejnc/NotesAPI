from json import dumps, loads

from functions.users.login import check_login
from models.notes_model import Notes
from utils.mongo import db_config


def add_note(event, context):
    """
    Connecting database and adding notes to the
    database.
    """
    body = loads(event["body"])
    _title = body["title"]
    _description = body["description"]
    _status = body["status"]

    db_config()
    oid = event["pathParameters"]["oid"]
    logged_user = check_login()

    if oid == logged_user["id"]:
        new_note = Notes(title=_title, description=_description, status=_status)

        new_note.save()
        response = {"message": "New note added.", "status_code": 200}
        return dumps(response)
