import logging
import os
from datetime import datetime
from flask_migrate import Migrate

from app import create_app, db, csrf
from app.models.control import Control
from app.models.device import Device
from app.models.message import SystemNotification, NewsMessage
from app.models.modify import TimeModifyReason
from app.models.role import Role
from app.models.user import User
from app.models.pos import Pos

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if app.config['LOG_DATABASE']:
    logging.basicConfig(filename='db.log')
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

migrate = Migrate(app, db)


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
       insert some entry's """

    # variables

    time = datetime.now()

    user_user = None
    admin_user = None
    owner_user = None
    manager_user = None

    admin_username = "admin"
    owner_username = "owner"
    manager_username = "manager"
    std_username = "user"

    device1 = None
    device2 = None

    device1_serial = 'SN - 0001'
    device2_serial = 'SN - 0002'

    # Create database
    db.create_all()

    # Create roles
    Role.insert_roles()

    # add roles to variables
    role_admin = Role.query.filter(Role.name == 'Administrator').first()
    role_owner = Role.query.filter(Role.name == 'Owner').first()
    role_manager = Role.query.filter(Role.name == 'Manager').first()
    role_user = Role.query.filter(Role.name == 'User').first()

    # create Device Entities
    device = Device.query.filter(Device.serial_number == device1_serial).first()
    if not device:
        device1 = Device(
            device_uuid="Device 01",
            label="Flipper",
            serial_number=device1_serial,
            created_at=time,
            modified_at=time,
            manufacturer='Activision',
            ordered_from='Amazon',
            tuev_expired_date=time,
        )
    device = Device.query.filter(Device.serial_number == device2_serial).first()
    if not device:
        device2 = Device(
            device_uuid="Device 02",
            label="Einarmiger Bandit",
            serial_number=device2_serial,
            created_at=time,
            modified_at=time,
            manufacturer='Activision',
            ordered_from='Amazon',
            tuev_expired_date=time,
        )

    # create User Entities
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
    user = User.query.filter(User.username == manager_username).first()
    if not user:
        manager_user = User(
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
    control_event = Control(
        created_at=time,
        is_modified=True,
        time_start=time,
        time_end=time,
        modified_at=time,
        user_id=1
    )
    modify_reason = TimeModifyReason(
        reason="Test EVENT",
        created_at=time,
        control=control_event,
        user_modified=admin_user,
        user_modifier=admin_user,
    )
    system_news = SystemNotification(
        title="Achtung Tagesabschluss um 23:59",
        body="Bitte alle Kassen abrechnen",
        is_repeatable=True,
        duration=59,
        hour=-1,
        minute=0,
        bc='#FF0000',
        fc='#FFFFFF',
    )
    index_news = NewsMessage(
        created_at=time,
        title="Flask-Pos hat jetzt Nachrichten",
        body="Und auch mit Inhalt",
    )
    index_news1 = NewsMessage(
        created_at=time,
        title="Noch eine Nachricht",
        body="Das hört ja gar nicht mehr auf",
    )
    index_news2 = NewsMessage(
        created_at=time,
        title="Noch eine Nachricht",
        body="Diesmal eine mehrzeilige Nachricht...<br>Das wird ja immer besser..."
             "<br>Das hört ja gar nicht mehr auf"
    )
    cash_bill = Pos(
        prefilled_amount=20000,
        created_at=time,
        is_modified=False,
        billed_by=1,
        control_id=1,
        device_id=1
    )

    # add entities
    db.session.add(user_user)
    db.session.add(admin_user)
    db.session.add(owner_user)
    db.session.add(manager_user)
    db.session.add(device1)
    db.session.add(device2)
    db.session.add(control_event)
    db.session.add(modify_reason)
    db.session.add(system_news)
    db.session.add(index_news)
    db.session.add(index_news1)
    db.session.add(index_news2)
    db.session.add(cash_bill)

    # Commit all to the database
    db.session.commit()
