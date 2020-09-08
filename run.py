import os
from datetime import datetime
from app import create_app, db
from app.models.user import User
from app.models.role import Role
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
       insert some roles and users """

    # Create database
    db.create_all()

    # Create roles
    Role.insert_roles()
    role_admin = Role.query.filter(Role.name == 'Administrator').first()
    role_owner = Role.query.filter(Role.name == 'Owner').first()
    role_manager = Role.query.filter(Role.name == 'Manager').first()

    time = datetime.now().strftime('%d %b, %H:%M:%S')

    admin_email = "admin@admin.de"
    owner_email = "owner@owner.de"
    manager_email = "manager@manager.de"
    user_email = "user@user.de"

    # Create users
    user = User.query.filter(User.email == admin_email).first()
    if not user:
        db.session.add(User(
            uuid="Mitarbeiter 001",
            username="admin",
            firstname="Rainer",
            lastname="Zufall",
            email=admin_email,
            password="admin",
            created_at=time,
            modified_at=time,
            is_active=True,
            role=role_admin,
        ))
    user = User.query.filter(User.email == owner_email).first()
    if not user:
        db.session.add(User(
            uuid="Mitarbeiter 002",
            username="owner",
            firstname="Like a",
            lastname="Boss",
            email=owner_email,
            password="owner",
            created_at=time,
            modified_at=time,
            is_active=True,
            role=role_owner,
        ))
    user = User.query.filter(User.email == manager_email).first()
    if not user:
        db.session.add(User(
            uuid="Mitarbeiter 003",
            username="manager",
            firstname="Max",
            lastname="Mustermann",
            email=manager_email,
            password="manager",
            created_at=time,
            modified_at=time,
            is_active=True,
            role=role_manager,
        ))
    if not User.query.filter(User.email == user_email).first():
        db.session.add(User(
            uuid="Mitarbeiter 004",
            username="user",
            firstname="Milli",
            lastname="Vanilli",
            email=user_email,
            password="user",
            created_at=time,
            modified_at=time,
            is_active=True,
        ))

    # Commit all to the database
    db.session.commit()
