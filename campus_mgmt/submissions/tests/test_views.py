from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User

class SubmissionViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='student1', password='pass1234', role='student')

    def test_submission_upload_redirect_if_not_logged(self):
        response = self.client.get(reverse('assignment-upload'))
        self.assertRedirects(response, '/accounts/login/?next=/submissions/upload/')