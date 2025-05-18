from django.test import TestCase
from accounts.forms import UserRegisterForm

class UserRegisterFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'newuser',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'role': 'student',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'username': 'newuser',
            'password1': 'pass',
            'password2': 'pass',
            'role': 'student',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
