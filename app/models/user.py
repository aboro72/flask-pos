import datetime

from app import db


# Possible Roles will be saved here
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)

    user_name = db.Column(db.String(64), unique=True, index=True)
    user_email = db.Column(db.String(128), unique=True)
    user_pass = db.Column(db.String(255), nullable=False)

    user_created_at = db.Column(db.DateTime())
    user_modified_at = db.Column(db.DateTime())

    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))

    def __repr__(self):
        return '<User %r>' % self.user_name
