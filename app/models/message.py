from datetime import datetime
from app import db


class Message(db.Model):
    __tablename__ = "messages"
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime())
    is_read = db.Column(db.Boolean, nullable=False, default=False)

    source_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        return '<Message {} {}>'.format(self.title, self.source_id)


class SystemNotification(db.Model):
    __tablename__ = "notifications"
    notification_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text)
    bc = db.Column(db.String(16))
    fc = db.Column(db.String(16))
    is_repeatable = db.Column(db.Boolean, default=False)
    start_datetime = db.Column(db.DateTime(), default=datetime.utcnow())
    end_datetime = db.Column(db.DateTime())
