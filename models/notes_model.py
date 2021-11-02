from mongoengine.document import Document,EmbeddedDocument
from mongoengine.fields import DateTimeField, EmbeddedDocumentField, IntField, ListField, ReferenceField, StringField

from models.users_model import Users

class Notes(Document):
    title = StringField(min_length=4,max_length=300)
    description = StringField(min_length=10)
    likes = IntField(default=0)
    comments = ListField(required=False)
    status = StringField(default="pending", choices=("completed","incomplete","pending"))
    created_by = ReferenceField(Users)

