from sqlalchemy import func
from pytz import timezone
from . import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(2000))
    link = db.Column(db.String(6))
    date = db.Column(db.DateTime(timezone=True), default=func.now(timezone("Poland")))
