from datetime import datetime
from app import db


class Device(db.Model):
    __tablename__ = "devices"
    device_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_uuid = db.Column(db.String(64), unique=True, nullable=False)
    label = db.Column(db.String(128))
    serial_number = db.Column(db.String(128), unique=True)
    ordered_from = db.Column(db.String(128))
    manufacturer = db.Column(db.String(128))
    created_at = db.Column(db.String(64), default=datetime.utcnow())
    modified_at = db.Column(db.String(64), default=datetime.utcnow())
