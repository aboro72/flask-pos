from app import db


class Employee(db.Model):
    __tablename__ = "employees"
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_uuid = db.Column(db.String(64), unique=True, nullable=False)

    lastname = db.Column(db.String(64), unique=True, nullable=False)
    firstname = db.Column(db.String(64), unique=True, nullable=False)

    created_at = db.Column(db.DateTime())
    modified_at = db.Column(db.DateTime())

    users = db.relationship('User', backref='employee', lazy=True)

    def __repr__(self):
        return '<Employee %r>' % (self.lastname + ' ' + self.name)
