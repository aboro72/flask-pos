from app import db


class Permission:
    ADD_BALANCE = 1
    READ_WRITE_MESSAGE = 2
    IN_OUT_CLOCK = 4
    ADD_USER = 8
    CORRECT_BALANCE = 16
    ADD_TIME = 32
    ADD_MODIFY_DEVICE = 64
    CORRECT_TIME = 128

    # role permission needed
    ADMIN = 256


# Possible Roles will be saved here
class Role(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=True)
    label = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime())
    modified_at = db.Column(db.DateTime())

    users = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        return '<Role %r>' % self.name

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 7

    @staticmethod
    def insert_roles():
        roles = {
            'User': [
                Permission.READ_WRITE_MESSAGE,
                Permission.IN_OUT_CLOCK,
                Permission.READ_WRITE_MESSAGE
            ], 'Moderator': [
                Permission.READ_WRITE_MESSAGE,
                Permission.IN_OUT_CLOCK,
                Permission.READ_WRITE_MESSAGE,
                Permission.ADD_USER,
                Permission.CORRECT_BALANCE,
                Permission.ADD_TIME,
            ], 'Administrator': [
                Permission.READ_WRITE_MESSAGE,
                Permission.IN_OUT_CLOCK,
                Permission.READ_WRITE_MESSAGE,
                Permission.ADD_USER,
                Permission.CORRECT_BALANCE,
                Permission.ADD_TIME,
                Permission.ADD_MODIFY_DEVICE,
                Permission.CORRECT_TIME,
                Permission.ADMIN
            ],
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm
