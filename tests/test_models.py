import unittest
from app.models.user import User
from app.models.role import Role, Permission


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)


class RoleModelTestCase(unittest.TestCase):
    def test_permission_is_correct(self):
        role1 = Role(name='Administrator', permissions=Permission.USER + Permission.MANAGER + Permission.OWNER
                                                                                            + Permission.ADMIN)
        role2 = Role(name='Owner', permissions=Permission.USER + Permission.MANAGER + Permission.OWNER)
        role3 = Role(name='Manager', permissions=Permission.USER + Permission.MANAGER)
        role4 = Role(name='User', permissions=Permission.USER)
        self.assertTrue(role1.permissions == 15)
        self.assertTrue(role2.permissions == 7)
        self.assertTrue(role3.permissions == 3)
        self.assertTrue(role4.permissions == 1)
        self.assertTrue(role1.name == 'Administrator')
