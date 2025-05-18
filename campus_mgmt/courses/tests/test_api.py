from rest_framework.test import APITestCase
from django.urls import reverse
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class CourseAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiuser', password='pass1234', role='student')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_course_list_api(self):
        url = reverse('api_courses')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
