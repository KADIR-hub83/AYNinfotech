from components import db as db
from datetime import datetime


class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_src = db.Column(db.Text)
    alt_text = db.Column(db.String(255))
    title = db.Column(db.String(1024))
    dashboard_title = db.Column(db.String(255))
    description = db.Column(db.String(512))
    content = db.Column(db.Text)
    url_endpoint = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    published_date = db.Column(db.String(30))
    create_time_stamp = db.Column(db.DateTime, default=datetime.utcnow())
    write_time_stamp = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Blog: %r>' % self.id