from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


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
migrate = Migrate(app, db)


from app import routes
from app.models import models, db_init


db_init.create_users()

