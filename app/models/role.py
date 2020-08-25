from app import db


# Possible Roles will be saved here
class Role(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    label = db.Column(db.String(64), unique=True)
    permission_val = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime())
    modified_at = db.Column(db.DateTime())

    users = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        return '<Role %r>' % self.name
