from json import loads, dumps


from utils.mongo import db_config
from models.notes_model import Notes

def update_note(event, context):
    """
        Updating title,status,description of the note as needed.
    """

    body = loads(event["body"])
    
    oid = event["pathParameters"]["oid"]
    update_param = event["pathParameters"]["args"]

    db_config()
    selected_note = Notes.objects(id=oid)
    
    if update_param == "title":
        _title = body["title"]
        selected_note.update(set__title=_title)
        message = "title updated"
        return dumps({"message":message})
    
    elif update_param == "description":
        _description = body["description"]
        selected_note.update(set__description=_description)
        message = "description updated"
        return dumps({"message":message})

    elif update_param == "status":
        _status = body["status"]
        selected_note.update(set__status=_status)
        message = "status updated"
        return dumps({"message":message})

    else:
        return dumps({"message":"Error"})

 
def update_note_whole(event, context):
    """
        Updating note
    """
    body = loads(event["body"])
    
    oid = event["pathParameters"]["oid"]

    _title = body["title"]
    _description = body["description"]
    _status = body["status"]

    db_config()

    selected_note = Notes.objects(id=oid)
    selected_note.update(
        set__title = _title,
        set__description = _description,
        set__status = _status
    )
    return dumps({"message":"Note updated"})
