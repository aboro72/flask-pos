from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

from flask_login import UserMixin, AnonymousUserMixin

from app.models.role import Permission, Role


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # User relevant fields
    uuid = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True)
    lastname = db.Column(db.String(64), nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    # Time Control
    created_at = db.Column(db.DateTime(), default=datetime.now())
    modified_at = db.Column(db.DateTime(), default=datetime.now())

    # Boolean variables
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    clock_time = db.Column(db.DateTime(), default=datetime.now())
    is_clocked = db.Column(db.Boolean, default=False)

    # Foreign keys
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)

    # Relationship to other Tables
    source = db.relationship('PrivateMessage', backref='msg_source_id', lazy=True, foreign_keys='PrivateMessage.source_id')
    target = db.relationship('PrivateMessage', backref='msg_target_id', lazy=True, foreign_keys='PrivateMessage.target_id')
    control = db.relationship('Control', backref='user', lazy=True, foreign_keys='Control.user_id')
    user_modified = db.relationship('TimeModifyReason', backref='user_modified', lazy=True,
                                    foreign_keys='TimeModifyReason '
                                                 '.modified_user')
    user_modifier = db.relationship('TimeModifyReason', backref='user_modifier', lazy=True,
                                    foreign_keys='TimeModifyReason'
                                                 '.modified_by')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

        if self.role is None:
            if self.email == current_app.config['FLASK_POS_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
        if self.role is None:
            self.role = Role.query.filter_by(default=True).first()

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def is_manager(self):
        return self.can(Permission.MANAGER)

    def is_owner(self):
        return self.can(Permission.OWNER)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.user_id


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
