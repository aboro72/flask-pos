from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

from flask_login import UserMixin, AnonymousUserMixin

from app.models.role import Permission, Role


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime())
    modified_at = db.Column(db.DateTime())

    is_active = (db.Column(db.Boolean, nullable=False, default=False))

    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)

    source = db.relationship('Message', backref='msg_source_id', lazy=True, foreign_keys='Message.source_id')
    target = db.relationship('Message', backref='msg_target_id', lazy=True, foreign_keys='Message.target_id')
    control = db.relationship('Control', backref='control_user_id', lazy=True, foreign_keys='Control.user_id')
    modifier_control = db.relationship('Control', backref='control_modify_id', lazy=True,
                                       foreign_keys='Control.modified_by')

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
        return '<User %r>' % self.name

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
