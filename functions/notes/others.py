import datetime
from json import loads, dumps

from models.notes_model import Notes
from utils.mongo import db_config



def delete_note(event,context):
    _id = event["pathParameters"]["oid"]

    db_config()

    selected_note = Notes.objects(id=_id)
    selected_note.delete()
    return dumps({"message":"Note deleted successfully."})

def like_note(event,context):
    _id = event["pathParameters"]["oid"]
    
    db_config()
    selected_note = Notes.objects.get(id=_id)

    like_count = selected_note["likes"]
    like_count = like_count + 1
    selected_note.update(
        set__likes = like_count
    )
    return dumps({"message":"like added"})

def comment_note(event,context):
    _id = event["pathParameters"]["oid"]

    body = loads(event["body"])
    _comments_stated = body["comments_stated"]
    _comments_by = body["comments_by"]
    _comments_date = datetime.datetime.utcnow()

    db_config()
    selected_note = Notes.objects.get(id=_id)
    selected_note.update(push__comments = [
        _comments_stated,
        _comments_by,
        _comments_date,
    ])
    

    return dumps({"message":"Comment added"})