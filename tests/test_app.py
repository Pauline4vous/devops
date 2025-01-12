import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, mongo
from flask import session
from unittest.mock import patch, MagicMock

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure test client
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'testsecretkey'
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/testdb'
        cls.client = app.test_client()

    def setUp(self):
        # Mock MongoDB collections
        self.mock_users = MagicMock()
        self.mock_items = MagicMock()

        # Mock the MongoDB instance
        mongo.db = MagicMock(users=self.mock_users, items=self.mock_items)

    def test_home_route(self):
        """Test the home route for status code and template."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Re-Use Gang', response.data)

    def test_register_user_success(self):
        """Test user registration with valid inputs."""
        self.mock_users.find_one.return_value = None  # Mock no existing user
        with self.client:
            response = self.client.post('/register', data={
                'username': 'testuser',
                'email': 'testuser@mail.com',
                'password': 'password123'
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome to the Gang, testuser!', response.data)
            self.assertIn('username', session)

    def test_register_user_failure(self):
        """Test user registration with existing email or username."""
        self.mock_users.find_one.return_value = {'username': 'testuser'}  # Mock existing user
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'testuser@mail.com',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username or email is already in use.', response.data)

    def test_login_success(self):
        """Test successful user login."""
        self.mock_users.find_one.return_value = {
            'email': 'testuser@mail.com',
            'password': '$pbkdf2-sha256$29000$hashedpassword'
        }
        with patch('werkzeug.security.check_password_hash', return_value=True):
            response = self.client.post('/login', data={
                'email': 'testuser@mail.com',
                'password': 'password123'
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome back,', response.data)
            self.assertIn('username', session)

    def test_login_failure(self):
        """Test login with invalid credentials."""
        self.mock_users.find_one.return_value = None  # Mock no matching user
        response = self.client.post('/login', data={
            'email': 'wronguser@mail.com',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid login credentials.', response.data)

    def test_add_item(self):
        """Test adding an item when logged in."""
        with self.client:
            with self.client.session_transaction() as sess:
                sess['username'] = 'testuser'  # Mock logged-in user
            response = self.client.post('/items/add', data={
                'item_name': 'Test Item',
                'item_category': 'Household',
                'item_description': 'A test item',
                'item_location': 'Test Location',
                'item_img': ''
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your item has been added successfully!', response.data)

    def test_404_error(self):
        """Test the 404 error page."""
        response = self.client.get('/nonexistent-page')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Page not found', response.data)

    def tearDown(self):
        mongo.db.users = None
        mongo.db.items = None

if __name__ == '__main__':
    unittest.main()
