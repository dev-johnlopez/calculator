#!flask/bin/python
from migrate.versioning import api
from config import BaseConfig
#from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
db.create_all()
if not os.path.exists(BaseConfig.SQLALCHEMY_MIGRATE_REPO):
    api.create(BaseConfig.SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(BaseConfig.SQLALCHEMY_DATABASE_URI, BaseConfig.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(BaseConfig.SQLALCHEMY_DATABASE_URI, BaseConfig.SQLALCHEMY_MIGRATE_REPO, api.version(BaseConfig.SQLALCHEMY_MIGRATE_REPO))
