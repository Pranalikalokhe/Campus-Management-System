from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User

class AccountsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='student1', password='pass1234', role='student')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'student1', 'password': 'pass1234'})
        self.assertRedirects(response, reverse('dashboard'))

    def test_dashboard_view_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/accounts/login/?next=/accounts/admin_dashboard/')
