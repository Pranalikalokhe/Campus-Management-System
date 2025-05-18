from django.shortcuts import render
from rest_framework import generics, permissions
from courses.models import Course, Enrollment
from submissions.models import Assignment, Submission
from .serializers import CourseSerializer, AssignmentSerializer, EnrollmentSerializer, SubmissionSerializer
from rest_framework.parsers import MultiPartParser, FormParser

# List all courses
class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

# Upload an assignment (teacher only)
class AssignmentCreateAPIView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]  # add role check in view if needed

# Enroll in a course (student)
class EnrollmentCreateAPIView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

# Submit an assignment file (student)
class SubmissionCreateAPIView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
