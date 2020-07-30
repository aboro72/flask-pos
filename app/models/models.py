from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_user import UserMixin

from app import db, login


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow())

    # User authentication
    user_name = db.Column(db.Unicode(255), index=True, unique=True, server_default=u'')
    password_hash = db.Column(db.String(128), nullable=False, server_default='')
    email = db.Column(db.Unicode(255), unique=True, nullable=False, server_default=u'')
    # user fields
    # active = db.Colunm('is active', db.Boolean, nullable=False, server_default='0')
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    # relation
    roles = db.relationship('Role', secondary='users_roles',
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, server_default=u'', unique=True)
    label = db.Column(db.Unicode(255), server_default=u'')


class UsersRoles(db.Model):
    __tablename__ = 'users_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow())

    # device fields

    device_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Device %r>' % self.device_name


@login.user_loader
def load_user(id):
    return User.query.get(int(id))