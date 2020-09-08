import os
from datetime import datetime
from app import create_app, db
from app.models.user import User
from app.models.role import Role
from app.models.device import Device
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


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

    time = datetime.now().strftime('%d %b, %H:%M:%S')

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

    # Create users
    admin_username = "admin"
    owner_username = "owner"
    manager_username = "manager"
    user_username = "user"

    user = User.query.filter(User.username == admin_username).first()
    if not user:
        db.session.add(User(
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
        ))
    user = User.query.filter(User.username == owner_username).first()
    if not user:
        db.session.add(User(
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
        ))
    user = User.query.filter(User.username == manager_username).first()
    if not user:
        db.session.add(User(
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
        ))
    if not User.query.filter(User.username == user_username).first():
        db.session.add(User(
            uuid="Mitarbeiter 004",
            username=user_username,
            firstname="Milli",
            lastname="Vanilli",
            email='user@test.de',
            password="user",
            created_at=time,
            modified_at=time,
            is_active=True,
        ))

    # Commit all to the database
    db.session.commit()
