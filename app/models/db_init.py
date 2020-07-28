import uuid
import hashlib

from app import db, app
from app.models.models import User, Role


def create_users():
    """ Create users """

    # Create all tables
    with app.app_context():
        db.create_all()
        # Adding roles
        admin_role = find_or_create_role('admin', u'Admin')

        # Add users
        user = find_or_create_user(u'Admin', u'admin@admin.com', u'admin', u'Andreas', u'Borowczak', admin_role)

        user = find_or_create_user(u'Member', u'member@example.com', 'Password1', u'one',u'employee')

        # Save to DB
        db.session.commit()


def find_or_create_role(name, label):
    """ Find existing role or create new role """
    role = Role.query.filter(Role.name == name).first()
    if not role:
        role = Role(name=name, label=label)
        db.session.add(role)
    return role


def find_or_create_user(user_name, email, password, firstname, lastname, role=None):
    """ Find existing user or create new user """
    user = User.query.filter(User.email == email).first()
    if not user:
        hashed_password = hash_password(password)
        user = User(email=email,
                    user_name=user_name,
                    password_hash=hashed_password,
                    first_name=firstname,
                    last_name=lastname,
                    )
        if role:
            user.roles.append(role)
        db.session.add(user)
    return user


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
