from rest_framework import generics, permissions
from courses.models import Course, Enrollment
from submissions.models import Assignment, Submission
from .serializers import (
    CourseSerializer, 
    AssignmentSerializer, 
    EnrollmentSerializer, 
    SubmissionSerializer
)

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AssignmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class EnrollmentCreateAPIView(generics.CreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class SubmissionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
