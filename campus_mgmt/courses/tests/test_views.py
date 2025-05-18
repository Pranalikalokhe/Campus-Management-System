from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User

class CourseViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='student1', password='pass1234', role='student')

    def test_course_list_view_redirect_if_not_logged(self):
        response = self.client.get(reverse('course-list'))
        self.assertRedirects(response, '/accounts/login/?next=/courses/')