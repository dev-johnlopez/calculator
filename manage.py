#!flask/bin/python
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.web.auth.models.role import Role
import os

from app import app, db

app.config.from_object(os.environ.get('APP_SETTINGS') or 'config.DevelopmentConfig')
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the tests without coverage """
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def add_roles():
    """Adds the system roles to the environment"""
    role = Role()
    role.name = "Admin"
    role.description = "Administrator of the system. Provides access to admin dashboard."
    db.session.add(role)
    role.name = "Back Office"
    role.description = "Access to create public access deals in the system. INTERNAL USE ONLY!"
    db.session.add(role)
    #db.session.add(Role(name="Back Office", description="Provides access to create deals in the system. Internal use only."))
    db.session.commit()

if __name__ == '__main__':
    manager.run()
