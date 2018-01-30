#!flask/bin/python
import unittest
from flask import Flask
from flask_testing import TestCase
from flask_security import login_required, current_user, logout_user
from app import app, db
from app.web.models.user import User

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        #db.drop_all()
        db.create_all()
        db.session.add(User(email="ad@min.com", password="admin",active=True))
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def login(self, email, password):
        return self.client.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
