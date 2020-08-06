""" imports """

# standard packages
import datetime
import os

# external packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# internal packages
from app.config import config
from app.helper.auth import hash_password

# config app

app = Flask(__name__)

# read environment variable
flask_env = os.getenv('FLASK_ENV', None)

# load config
# if environment is not set load production config
if flask_env == 'development':
    app.config.from_object(config.DevelopmentConfig)
elif flask_env == 'testing':
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.ProductionConfig)

db = SQLAlchemy(app)

from app.models.user import User
from app.models.role import Role

db.init_app(app)
db.create_all()


# controller import
from app.controller import (
    mainController,
    userController,
    authController,
)

# register controller
app.register_blueprint(mainController.main)
app.register_blueprint(userController.user)
app.register_blueprint(authController.auth)

# Create Roles
with app.app_context():
    # Create Admin Role
    role_admin = Role(role_name='Admin')
    role = Role.query.filter(Role.role_name == role_admin.role_name).first()
    if not role:
        db.session.add(role_admin)

    # Create Admin User
    user_admin = User(
        user_name="admin",
        user_email="admin@admin.de",
        user_pass=hash_password("admin"),
        user_created_at=datetime.datetime.now(),
        user_modified_at=datetime.datetime.now(),
        role=role_admin
    )
    user = User.query.filter(User.user_email == user_admin.user_email).first()
    if not user:
        db.session.add(user_admin)

    # Save Admin User & Role
    db.session.commit()
