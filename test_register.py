import unittest
from register import User


class TestReg(unittest.TestCase):
    def setUp(self):
        self.user1 = User(
            'Donald Duck', 'Duckie', 'The.zen9', 'donduck@mail.com', 15)

    def tearDown(self):
        return super(TestReg, self).tearDown()
        
    def test_valid_username(self):
        """Test username is not equal to name or less than 4 characters.
        """
        self.assertTrue(self.user1.valid_username(), True)

    def test_valid_password(self):
        """Test a password is valid"""
        self.assertTrue(self.user1.valid_password(), True)

    def test_valid_email(self):
        """Test an email is valid"""
        self.assertEqual(self.user1.valid_email(), True)

    def test_valid_age(self):
        """Test user's age is an integer > 0."""
        self.assertEqual(self.user1.valid_age(), True)

    def test_register_user(self):
        """Test user can register successfully"""
        self.assertEqual(self.user1.register_user(),
            'Duckie registered successfully!')

    def test_login_user(self):
        """ Test user can login successfully """
        self.user1.register_user()
        self.assertEqual(self.user1.login_user('Duckie', 'The.zen9'),
            'You are logged in now.')

    def test_get_all_info(self):
        """Test user can get all their info on the App """
        self.user1.register_user()
        self.assertEqual(self.user1.get_all_info('Duckie', 'The.zen9'), 
'''Name: Donald Duck,\
 Username: Duckie,\
 Email: donduck@mail.com,\
 Age: 15''')
