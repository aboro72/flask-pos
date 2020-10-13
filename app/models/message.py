from datetime import datetime
from app import db


class NewsMessage(db.Model):
    __tablename__ = "news"
    news_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime())
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text)


class PrivateMessage(db.Model):
    __tablename__ = "privatemessages"
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
    title = db.Column(db.String(128), nullable=False) # Message Title
    body = db.Column(db.Text)  # The Message
    bc = db.Column(db.String(16))  # Background Color e.g. #000000
    fc = db.Column(db.String(16))  # Foreground Color e.g. #FFFFFF
    duration = db.Column(db.Integer, default=1)  # 0 - 59 minutes
    hour = db.Column(db.Integer, default=0)  # -1 for infinite
    minute = db.Column(db.Integer, default=0)  # -1 for infinite
    day = db.Column(db.Integer, default=0)  # only need if not repeatable
    month = db.Column(db.Integer, default=0)  # only need if not repeatable
    year = db.Column(db.Integer, default=0)  # only need if not repeatable
    is_repeatable = db.Column(db.Boolean, default=False)  # True or False :)
    start_datetime = db.Column(db.DateTime(), default=datetime.utcnow())  # computed date
    end_datetime = db.Column(db.DateTime())  # computed date
