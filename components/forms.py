from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Optional, Regexp, Length, Email, NumberRange


class ContactForm(FlaskForm):
    name = StringField(label="",
                       validators=[InputRequired(message="Name is required"),
                                   Length(min=3, max=128, message="Length of name must be 3-128"),
                                   Regexp(regex="^[ a-zA-Z.]+$", message="Characters must be alphabets or period(.)")],
                       render_kw={"placeholder": "Full Name", "required": "", "id": "name", "type": "text"})

    work_email = StringField(label="",
                             validators=[InputRequired(message="Email is required"),
                                         Length(min=3, max=128, message="Length of Email must be 3-128"),
                                         Email(message="Please provide valid email address.")],
                             render_kw={"placeholder": "email", "required": "", "id": "work_email", "type": "email"})

    phone = StringField(label="Phone Number",
                        validators=[Optional(),
                                    Length(min=6, max=20, message="Length of Phone Number must be 6-20"),
                                    Regexp(regex="^[ 0-9+]+$",
                                           message="Characters must be numbers, space or plus sign.")],
                        render_kw={"placeholder": "", "id": "phone", "type": "tel"})

    message = TextAreaField(label="",
                            validators=[InputRequired(message="Message is required"),
                                        Length(min=8, max=2048, message="Length of Message must be 8-2048"),
                                        Regexp(regex="^[ a-zA-Z0-9.,]+$",
                                               message="Characters must be alphabets, numbers, comma(,) or period(.)")],
                            render_kw={"placeholder": "What we can help you with!",
                                       "required": "", "id": "message", "rows": "5"})
