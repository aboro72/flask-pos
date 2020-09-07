from app import db


class Message(db.Model):
    __tablename__ = "messages"
    message_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime())
    is_read = db.Column(db.Boolean, nullable=False, default=False)

    source_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.title, self.source_id
