class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "\x88|\x0c\x19q\xa5\\(\x8d9\x82!/\xfc\xa4\x8d\xdbe\xc7\x9a\x04s\x04\xe0"

    # if we need the db credentials in the config
    DB_NAME = "game-room-production"
    DB_USER = "GameRoomAdminProduction"
    DB_PASS = "LikeABoss"

    SESSION_COOKIE_SECURE = True

    # this is for uploads only
    # UPLOAD_FOLDER = "/home/gameManager/flask-pos/app/files/upload"
    # POSSIBLE_EXTENSIONS = set(['txt', 'jpg', 'png'])


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    # if we need the db credentials in the config
    DB_NAME = "game-room-development"
    DB_USER = "GameRoomAdminDevelopment"
    DB_PASS = "LikeADev"

    # this is for uploads only
    # UPLOAD_FOLDER = "/home/dev/flask-pos/app/files/upload"


class TestingConfig(Config):
    TESTING = True

    # if we need the db credentials in the config
    DB_NAME = "game-room-testing"
    DB_USER = "GameRoomAdminTesting"
    DB_PASS = "LikeATester"
