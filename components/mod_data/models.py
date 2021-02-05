from flask_mongoengine import Document
from datetime import datetime
from mongoengine import StringField, EmailField, MultiLineStringField, BooleanField, DateTimeField
import pytz
IST = pytz.timezone('Asia/Kolkata')

class LeadData(Document):
    name = StringField(default="From Website")
    email = EmailField()
    mobile = StringField()
    message = MultiLineStringField()

    # other1 meta attributes
    active = BooleanField(default=True)
    time_created = DateTimeField(default=None)
    time_last_modified = DateTimeField(default=None)


    # Write custom validations here
    def clean(self):
        if self.time_created is None:
            self.time_created = datetime.now(IST)
        self.time_last_modified = datetime.now(IST)


class UserData(Document):
    username = StringField(required=True, unique=True)
    password = StringField()
