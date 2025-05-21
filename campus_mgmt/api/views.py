from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
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

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EnrollmentCreateAPIView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]  # <-- Add this


class SubmissionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

# extra JSON view
from django.http import JsonResponse

def course_detail_api(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        data = {
            "id": course.id,
            "name": course.name,
            "description": course.description,
            "teacher": course.teacher.username,
        }
        return JsonResponse(data)
    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found"}, status=404)
