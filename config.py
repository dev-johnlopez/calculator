# Define the application directory
import os

class BaseConfig(object):
    DEBUG = False
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Secret key for signing cookies
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "fjap1lk2jnfjflKL16SDFAsdaAOhj2po1jPLFJ"
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = "asdjn1poJLAI451hjsFJOQWNXsabxui"
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_CONFIRMABLE = False

    #Mail config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'johnny.lopez617@gmail.com'
    MAIL_PASSWORD = 'Saintviator1??'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    #Flask - Security
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['email']
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    SECURITY_SEND_PASSWORD_RESET_EMAIL = False
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False
    SECURITY_CONFIRM_EMAIL_WITHIN = 100000
    SECURITY_RESET_PASSWORD_WITHIN = 100000
    SECURITY_LOGIN_WITHIN = 1
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
