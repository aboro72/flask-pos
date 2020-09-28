from app import db


class Control(db.Model):
    __tablename__ = "control"
    control_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    modified_at = db.Column(db.DateTime())
    time_start = db.Column(db.DateTime())
    time_end = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    is_modified = db.Column(db.Boolean)
    modify_reason = db.relationship('TimeModifyReason', backref='control', lazy=True,
                                    foreign_keys='TimeModifyReason.control_by')
