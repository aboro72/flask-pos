import logging
import os
from datetime import datetime, timedelta
from flask import session, app as flask_app
from flask_migrate import Migrate

from app import create_app, db, csrf
from app.models.control import Control
from app.models.device import Device
from app.models.message import SystemNotification
from app.models.modify import TimeModifyReason
from app.models.role import Role
from app.models.user import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if app.config['LOG_DATABASE']:
    logging.basicConfig(filename='db.log')
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

migrate = Migrate(app, db)


@app.before_request
def make_session_permanent():
    session.permanent = True
    flask_app.permanent_session_lifetime = timedelta(minutes=app.config['SESSION_LIFETIME'])


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, csrf=csrf)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def createdb():
    """Create the database and
       insert some devices, roles and users """

    # time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    time = datetime.now()
    # Create database
    db.create_all()

    # Create devices
    device1_serial = 'SN - 0001'
    device2_serial = 'SN - 0002'

    device = Device.query.filter(Device.serial_number == device1_serial).first()
    if not device:
        db.session.add(Device(
            device_uuid="Device 01",
            label="Flipper",
            serial_number=device1_serial,
            created_at=time,
            modified_at=time,
            manufacturer='Activision',
            ordered_from='Amazon'
        ))
    device = Device.query.filter(Device.serial_number == device2_serial).first()
    if not device:
        db.session.add(Device(
            device_uuid="Device 02",
            label="Einarmiger Bandit",
            serial_number=device2_serial,
            created_at=time,
            modified_at=time,
            manufacturer='Activision',
            ordered_from='Amazon'
        ))

    # Create roles
    Role.insert_roles()
    role_admin = Role.query.filter(Role.name == 'Administrator').first()
    role_owner = Role.query.filter(Role.name == 'Owner').first()
    role_manager = Role.query.filter(Role.name == 'Manager').first()
    role_user = Role.query.filter(Role.name == 'User').first()

    # Create users
    admin_username = "admin"
    owner_username = "owner"
    manager_username = "manager"
    std_username = "user"

    admin_user = None
    user = User.query.filter(User.username == admin_username).first()
    if not user:
        admin_user = User(
            uuid="Mitarbeiter 001",
            username=admin_username,
            firstname="Rainer",
            lastname="Zufall",
            email='admin@test.de',
            password="admin",
            created_at=time,
            modified_at=time,
            is_active=True,
            role=role_admin,
        )
        db.session.add(admin_user)
    user = User.query.filter(User.username == owner_username).first()
    if not user:
        owner_user = User(
            uuid="Mitarbeiter 002",
            username=owner_username,
            firstname="Like a",
            lastname="Boss",
            email='owner@test.de',
            password="owner",
            created_at=time,
            modified_at=time,
            is_active=True,
            role=role_owner,
        )
        db.session.add(owner_user)
    user = User.query.filter(User.username == manager_username).first()
    if not user:
        user_manager = User(
            uuid="Mitarbeiter 003",
            username=manager_username,
            firstname="Max",
            lastname="Mustermann",
            email='manager@test.de',
            password="manager",
            created_at=time,
            modified_at=time,
            is_active=True,
            role=role_manager,
        )
        db.session.add(user_manager)
    user = User.query.filter(User.username == std_username).first()
    if not user:

        user_user = User(
            uuid="Mitarbeiter 004",
            username=std_username,
            firstname="Milli",
            lastname="Vanilli",
            email='user@test.de',
            password="user",
            created_at=time,
            modified_at=time,
            is_active=True,
            role=role_user,
        )
        db.session.add(user_user)
    db.session.commit()

    control_event = Control(
        created_at=time,
        is_modified=True,
        time_start=time,
        time_end=time,
        modified_at=time,
        user_id=1
    )
    db.session.add(control_event)
    modify_reason = TimeModifyReason(
        reason="Test EVENT",
        created_at=time,
        control=control_event,
        user_modified=admin_user,
        user_modifier=admin_user,
    )

    db.session.add(modify_reason)
    note = SystemNotification(
        title="Achtung Tagesabschluss um 23:59",
        body="Bitte alle Kassen abrechnen",
        is_repeatable=True,
        duration=59,
        hour=-1,
        minute=0,
        bc='#FF0000',
        fc='#FFFFFF',
    )

    db.session.add(note)
    # Commit all to the database
    db.session.commit()
