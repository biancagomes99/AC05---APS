# config.py


class BaseConfig(object):
    SECRET_KEY = 'admin'
    DEBUG = True
    DB_NAME = 'docker'
    DB_USER = 'docker'
    DB_PASS = '123'
    DB_SERVICE = '172.17.0.2'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
