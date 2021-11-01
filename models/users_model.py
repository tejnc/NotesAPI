import datetime
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, DictField, EmailField, ListField, StringField


class Users(Document):
    name = StringField(required=True)
    gender = StringField(choices=("male","female","other"))
    phone_number = StringField()
    address = DictField()
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    created = DateTimeField(default=datetime.datetime.utcnow)