from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTests(TestCase):
    def test_create_student_user(self):
        user = User.objects.create_user(username="student1", password="pass123", role="Student")
        self.assertEqual(user.username, "student1")
        self.assertEqual(user.role, "Student")

    def test_user_authentication(self):
        user = User.objects.create_user(username="teacher1", password="pass123", role="Teacher")
        login = self.client.login(username="teacher1", password="pass123")
        self.assertTrue(login)

