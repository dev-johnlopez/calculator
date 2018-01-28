#!flask/bin/python
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
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

if __name__ == '__main__':
    manager.run()
