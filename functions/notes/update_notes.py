from json import dumps, loads

from models.notes_model import Notes
from utils.mongo import db_config


def update_note(event, context):
    """
    Updating title,status,description of the note as needed.
    """

    body = loads(event["body"])
    _keys = body.keys()
    oid = event["pathParameters"]["oid"]

    db_config()
    selected_note = Notes.objects(id=oid)

    if "title" in _keys:
        _title = body["title"]
        selected_note.update(set__title=_title)

    if "description" in _keys:
        _description = body["description"]
        selected_note.update(set__description=_description)

    if "status" in _keys:
        _status = body["status"]
        selected_note.update(set__status=_status)

    return dumps({"message": "updated"})
