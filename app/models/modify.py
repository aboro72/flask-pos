from datetime import datetime
from app import db


class TimeModifyReason(db.Model):
    __tablename__ = 'time_modify_reason'
    modify_reason_id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text())
    control_by = db.Column(db.Integer, db.ForeignKey('control.control_id'))
    created_at = db.Column(db.String(64), default=datetime.now())
    modified_user = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    modified_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
