from app import db


class Pos(db.Model):
    __tablename__ = "control_devices"
    control_device_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total_amount = db.Column(db.Numeric(10, 2))
    prefilled_amount = db.Column(db.Numeric(10, 2))

    created_at = db.Column(db.DateTime())
    is_modified = db.Column(db.Boolean)
    modified_at = db.Column(db.DateTime())
    modified_reason = db.Column(db.Text(), nullable=False)

    modified_by = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    control_id = db.Column(db.Integer, db.ForeignKey('control.control_id'), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.device_id'), nullable=False)
