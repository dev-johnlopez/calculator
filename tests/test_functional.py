#!flask/bin/python
import unittest
from flask_security import current_user
from base import BaseTestCase

class FlaskTestCase(BaseTestCase):
    # Ensure that the main index routes to the login page when user is not logged in
    def test_main_page_login_redirect(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

    def test_login_logout(self):
        with self.client:
            response = self.client.post('/login',
                                        data={'email': 'ad@min.com', 'password': 'admin'})
            self.assertTrue(current_user.email == 'ad@min.com')
