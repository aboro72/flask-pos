from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime())
    modified_at = db.Column(db.DateTime())

    is_active = (db.Column(db.Boolean, nullable=False, default=False))

    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)

    source = db.relationship('Message', backref='msg_source_id', lazy=True, foreign_keys='Message.source_id')
    target = db.relationship('Message', backref='msg_target_id', lazy=True, foreign_keys='Message.target_id')
    control = db.relationship('Control', backref='control_user_id', lazy=True, foreign_keys='Control.user_id')
    modifier_control = db.relationship('Control', backref='control_modify_id', lazy=True,
                                       foreign_keys='Control.modified_by')

    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)