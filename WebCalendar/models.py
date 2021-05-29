from flask_sqlalchemy import Model
from WebCalendar import db


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"[{date}] --> {event} at {location}"
