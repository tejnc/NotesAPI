import datetime

from mongoengine.document import Document
from mongoengine.fields import (
    DateTimeField,
    DictField,
    EmailField,
    ListField,
    ReferenceField,
    StringField,
)

from models.notes_model import Notes


class Users(Document):
    name = StringField(required=True)
    gender = StringField(choices=("male", "female", "other"))
    phone_number = StringField()
    address = DictField()
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    notes_created = ListField(ReferenceField(Notes))
