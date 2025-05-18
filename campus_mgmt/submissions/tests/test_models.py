from django.test import TestCase
from submissions.models import Assignment, Submission
from courses.models import Course
from accounts.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

class SubmissionModelTest(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher1', password='pass1234', role='teacher')
        self.student = User.objects.create_user(username='student1', password='pass1234', role='student')
        self.course = Course.objects.create(title='Course', description='Desc', teacher=self.teacher)
        self.assignment = Assignment.objects.create(title='Assignment', course=self.course, description='Test', due_date='2025-12-31')
        self.file = SimpleUploadedFile('test.txt', b'Hello World')
        self.submission = Submission.objects.create(assignment=self.assignment, student=self.student, file=self.file)

    def test_submission_creation(self):
        self.assertEqual(self.submission.student.username, 'student1')
        self.assertEqual(self.submission.assignment.title, 'Assignment')