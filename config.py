import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # no debug messages
    DEBUG = False

    # no test messages
    TESTING = False

    # SECRET_KEY = "\x88|\x0c\x19q\xa5\\(\x8d9\x82!/\xfc\xa4\x8d\xdbe\xc7\x9a\x04s\x04\xe0"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # only sent session-cookie if https is used
    SESSION_COOKIE_SECURE = True

    # if we need db-login in config
    # DB_NAME = "game-room-production"
    # DB_USER = "GameRoomAdminProduction"
    # DB_PASS = "LikeABoss"

    # if we need a upload folder
    # UPLOAD_FOLDER = "/home/gameManager/flask-pos/app/files/upload"
    # POSSIBLE_EXTENSIONS = set(['txt', 'jpg', 'png'])

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    # debug messages
    DEBUG = True

    # DB_NAME = "game-room-development"
    # DB_USER = "GameRoomAdminDevelopment"
    # DB_PASS = "LikeADev"
    # FOLDER = "/home/ae4life/tutorial/flask"


class TestingConfig(Config):
    # test messages
    TESTING = True

    # DB_NAME = "game-room-testing"
    # DB_USER = "GameRoomAdminTesting"
    # DB_PASS = "LikeATester"
