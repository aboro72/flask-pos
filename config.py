""" imports """
import os

# save the application path
basedir = os.path.abspath(os.path.dirname(__file__))

""" Config file

    This Config file is for different purposes:

        production
        testing
        development

"""


class Config:
    # the secret key to encode the requests
    SECRET_KEY = \
        os.environ.get('SECRET_KEY') or \
        "b'>\x888\x9b@\x1dWN\\X\x00P0\xa0x\xb9'"

    # only sent session-cookie if https is used
    # SESSION_COOKIE_SECURE = True

    # staging server
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URL') or \
        'sqlite:///data.sqlite'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email
    MAIL_SERVER = 'mail.gmx.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASK_POS_MAIL_SUBJECT_PREFIX = '[FLASK_POS]'
    FLASK_POS_MAIL_SENDER = 'Flask-pos Admin <flasktest@gmx.de>'
    FLASK_POS_ADMIN = os.environ.get('FLASK_POS_ADMIN')

    PAGINATION_USER = 5
    PAGINATION_DEVICE = 5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # debug message

    DEBUG = True

    # session lifetime in seconds
    PERMANENT_SESSION_LIFETIME = 600

    SESSION_COOKIE_SAMESITE = 'Strict'
    # database file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    WTF_CSRF_ENABLED = False

    # db
    LOG_DATABASE = True


class TestingConfig(Config):
    # test message
    TESTING = True

    # database file
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    # database file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    SESSION_COOKIE_SECURE = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
