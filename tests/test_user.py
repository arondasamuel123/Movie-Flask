import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_password = User(password='123456')
        
    def test_password_setter(self):
        self.assertTrue(self.new_password.pass_secure is not None)
        
    def test_no_access_password(self):
        self.assertRaises(AttributeError)
        
    def test_password_verification(self):
        self.assertTrue(self.new_password.verify_password('123456'))
        
        