from flask_login import UserMixin
from components import db as db
from datetime import datetime
import enum
import pytz
IST = pytz.timezone('Asia/Kolkata')


class TaskStatus(enum.Enum):
    open = ['Open', 'rgb(255, 99, 132)']
    in_progress = ['In Progress', 'rgb(255, 159, 64)']
    converted = ['Opportunity', 'rgb(255, 205, 86)']
    closed = ['Closed', 'rgb(75, 192, 192)']
# "rgb(54, 162, 235)"
# "rgb(153, 102, 255)",
# "rgb(201, 203, 207)"

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(255))
    create_time_stamp = db.Column(db.DateTime, default=datetime.now(IST))

    write_time_stamp = db.Column(db.DateTime, default=datetime.now(IST))

    def __repr__(self):
        return '<User: %r>' % self.first_name


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    country = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(150))
    company = db.Column(db.String(150))
    job_title = db.Column(db.String(100))
    product = db.Column(db.String(100))
    no_of_employees = db.Column(db.String(10))
    comments = db.Column(db.Text)
    sales_comments = db.Column(db.Text)
    type = db.Column(db.String(20))
    archive = db.Column(db.Boolean, default=False)
    sales_person = db.Column(db.String(150))
    product_service = db.Column(db.String(150))
    project_cost = db.Column(db.String(150))
    sales_person = db.Column(db.String(150))
    create_time_stamp = db.Column(db.DateTime, default=datetime.now(IST))
    sale_status = db.Column(
        db.Enum(TaskStatus),
        default=TaskStatus.open,
        nullable=False
    )

    def __repr__(self):
        return '<User: %r>' % self.name