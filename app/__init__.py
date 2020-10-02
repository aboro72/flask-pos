""" Create and config the app """

# external packages
from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


# internal packages
from flask_wtf import CSRFProtect

from config import config

# declare packages
mail = Mail()
moment = Moment()
bootstrap = Bootstrap()
login_manager = LoginManager()
csrf = CSRFProtect()

# disable auto flush for SQLAlchemy to prevent
# automatic persist entities
db = SQLAlchemy(session_options={"autoflush": False})


# App factory
def create_app(config_name):

    # register app
    app = Flask(__name__)

    # load config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # init addons
    db.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # import models
    from app.models.pos import Pos
    from app.models.user import User
    from app.models.role import Role
    from app.models.device import Device
    from app.models.control import Control
    from app.models.modify import TimeModifyReason
    from app.models.message import NewsMessage, PrivateMessage, SystemNotification

    # import blueprints
    from app.blueprints import (
        pos as pos_controller,
        main as main_controller,
        auth as auth_controller,
        admin as admin_controller,
        clockIn as clockIn_controller,
    )

    # register blueprints
    app.register_blueprint(main_controller.main, url_prefix='')
    app.register_blueprint(auth_controller.auth, url_prefix='/auth')
    app.register_blueprint(admin_controller.admin, url_prefix='/admin')
    app.register_blueprint(pos_controller.pos, url_prefix='/pos')
    app.register_blueprint(clockIn_controller.clock_in, url_prefix='/clock/')

    return app


