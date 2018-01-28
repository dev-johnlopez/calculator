#!flask/bin/python
import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, db
from app.web.models.property import Property
from app.web.models.unit import Unit
from app.web.models.user import User

class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite_test://"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User(email="ad@min.com", password="admin"))
        db.session.commit()
        with self.client:
            response = self.client.post('login', { email: 'ad@min.com', password: 'admin' })
        property = Property()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_main_page_login_redirect(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

if __name__ == '__main__':
    unittest.main()
