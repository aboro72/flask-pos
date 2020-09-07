from app import db


class Device(db.Model):
    __tablename__ = "devices"
    device_id = db.Column(db.Integer, primary_key=True)
    device_uuid = db.Column(db.String(64), unique=True, nullable=False)
    label = db.Column(db.String(128))
    serial_number = db.Column(db.String(128))
