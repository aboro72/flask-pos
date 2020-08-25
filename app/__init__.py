""" imports """

# standard packages
import datetime
import os

# external packages
from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# internal packages
from app.config import config
# from app.services.auth import hash_password

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
migrate = Migrate(app, db)
mail = Mail(app)

from app.models.user import User
from app.models.role import Role
from app.models.employee import Employee
from app.models.message import Message
from app.models.device import Device
from app.models.control import Control
from app.models.pos import Pos


db.create_all()


# blueprints import
from app.blueprints import (
    main as main_controller,
    user as user_controller,
    auth as auth_controller,
    control as control_controller,
    device as device_controller,
    pos as pos_controller
)

# register blueprints
app.register_blueprint(main_controller.main, url_prefix='')
app.register_blueprint(user_controller.user, url_prefix='/user')
app.register_blueprint(auth_controller.auth, url_prefix='/auth')
app.register_blueprint(control_controller.control, url_prefix='/control')
app.register_blueprint(device_controller.device, url_prefix='/device')
app.register_blueprint(pos_controller.pos, url_prefix='/pos')

# Create Roles
with app.app_context():
    time = datetime.datetime.now()
    # Create Admin Role
    role_admin = Role(
        name='Admin',
        label='Administrator',
        permission_val=16,
        created_at=time,
        modified_at=time,
    )
    role = Role.query.filter(Role.name == role_admin.name).first()
    if not role:
        db.session.add(role_admin)
        # Create Employee

    employee_admin = Employee(
        employee_uuid="Mitarbeiter-ID 001",
        lastname="Mustermann",
        firstname="Max",
        created_at=time,
        modified_at=time,
    )
    employee = Employee.query.filter(Employee.employee_uuid == employee_admin.employee_uuid).first()
    if not employee:
        db.session.add(employee_admin)
    # Create Admin User
    user_admin = User(
        name="admin",
        email="admin@admin.de",
        password="admin",
        created_at=time,
        modified_at=time,
        is_active=True,
        role=role_admin,
        employee=employee_admin,
    )
    user = User.query.filter(User.email == user_admin.email).first()
    if not user:
        db.session.add(user_admin)

    # Save Admin User & Role
    db.session.commit()
