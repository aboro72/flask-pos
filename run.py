import os, datetime
from app import create_app, db
from app.models.user import User
from app.models.role import Role
from app.models.employee import Employee
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
    db.create_all()
    # Create Roles
    Role.insert_roles()
    role_admin = Role.query.filter(Role.name == 'Administrator').first()
    role_manager = Role.query.filter(Role.name == 'Manager').first()
    time = datetime.datetime.now()
    # Create Employees

    employee_admin = Employee(
        employee_uuid="Mitarbeiter-ID 001",
        lastname="Mustermann",
        firstname="Max",
        created_at=time,
        modified_at=time,
    )
    employee_manager = Employee(
        employee_uuid="Mitarbeiter-ID 002",
        lastname="Zufall",
        firstname="Rainer",
        created_at=time,
        modified_at=time,
    )
    employee = Employee.query.filter(Employee.employee_uuid == employee_admin.employee_uuid).first()
    if not employee:
        db.session.add(employee_admin)
    employee = Employee.query.filter(Employee.employee_uuid == employee_manager.employee_uuid).first()
    if not employee:
        db.session.add(employee_manager)
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
    user_manager = User(
        name="manager",
        email="manager@manager.de",
        password="manager",
        created_at=time,
        modified_at=time,
        is_active=True,
        role=role_manager,
        employee=employee_manager,
    )
    user = User.query.filter(User.email == user_admin.email).first()
    if not user:
        db.session.add(user_admin)
    user = User.query.filter(User.email == user_manager.email).first()
    if not user:
        db.session.add(user_manager)

    # Save Admin User & Role
    db.session.commit()
