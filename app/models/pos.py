from app import db


class Pos(db.Model):
    __tablename__ = "control_devices"
    control_device_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # bill (Decimal is not possible in Postgres and SQLite
    # total_amount = db.Column(db.Numeric(10, 2))
    # prefilled_amount = db.Column(db.Numeric(10, 2))
    total_amount = db.Column(db.Integer)
    prefilled_amount = db.Column(db.Integer)

    # times
    created_at = db.Column(db.DateTime())
    billed_at = db.Column(db.DateTime())
    modified_at = db.Column(db.DateTime())
    is_modified = db.Column(db.Boolean, default=False)
    modified_reason = db.Column(db.Text())

    # foreign keys
    modified_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    billed_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    control_id = db.Column(db.Integer, db.ForeignKey('control.control_id'), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.device_id'), nullable=False)
