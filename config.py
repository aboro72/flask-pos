# imports
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


    # SESSION_COOKIE_SECURE = True

    # staging server
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URL') or \
        'sqlite:///data.sqlite'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TODO implement email
    MAIL_SERVER = 'mail.gmx.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASK_POS_MAIL_SUBJECT_PREFIX = '[FLASK_POS]'
    FLASK_POS_MAIL_SENDER = 'Flask-pos Admin <flasktest@gmx.de>'
    FLASK_POS_ADMIN = os.environ.get('FLASK_POS_ADMIN')

    # TODO implement pagination
    PAGINATION_USER = 5
    PAGINATION_DEVICE = 5

    # WSS Config NOT IMPLEMENTED
    HELP_DESK_FORM = 'https://hd.sleibo.de/assets/form/form.js'
    HELP_DESK_CHAT = 'https://hd.sleibo.de/assets/chat/chat.min.js'

    # session lifetime in seconds
    PERMANENT_SESSION_LIFETIME = 600

    """ security """
    # session cookies only allowed from the same site
    SESSION_COOKIE_SAMESITE = 'Strict'

    # only sent session-cookie if https is used
    SESSION_COOKIE_SECURE = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    # debug messages
    DEBUG = True

    # development database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    # development database logging
    LOG_DATABASE = True

    # CSRF Protection in WTF-Forms
    WTF_CSRF_ENABLED = False


class TestingConfig(Config):
    # test message
    TESTING = True

    # testing database
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

    # CSRF Protection in WTF-Forms
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):

    # production database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
