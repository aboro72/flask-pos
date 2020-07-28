from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models.db_init import create_users, find_or_create_role, find_or_create_user

# -- Init FLASK & Config ---
app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy()
db.init_app(app)
create_users()
migrate = Migrate(app, db)


from app import routes, models


