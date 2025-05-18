from django.test import TestCase
from courses.models import Course
from accounts.models import User

class CourseModelTest(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher1', password='pass1234', role='teacher')
        self.course = Course.objects.create(title='Test Course', description='Test Desc', teacher=self.teacher)

    def test_course_creation(self):
        self.assertEqual(self.course.title, 'Test Course')
        self.assertEqual(self.course.teacher.username, 'teacher1')