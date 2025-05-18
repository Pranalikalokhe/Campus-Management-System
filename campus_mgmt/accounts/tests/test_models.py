from django.test import TestCase
from accounts.models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234', role='student')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.role, 'student')
        self.assertTrue(self.user.check_password('pass1234'))
