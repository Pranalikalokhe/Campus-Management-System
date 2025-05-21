from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from .forms import EnrollmentForm
from django.core.mail import send_mail
from accounts.decorators import role_required
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, permissions
from api.serializers import CourseSerializer, AssignmentSerializer, EnrollmentSerializer, SubmissionSerializer

# ----------------------------
# Web Views
# ----------------------------

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Course, Enrollment
@login_required
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def enroll_course(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save()
            messages.success(request, "Enrolled successfully!")
            return redirect("course_detail", pk=enrollment.pk)
    else:
        form = EnrollmentForm()
    return render(request, "course_detail.html", {"form": form})

# @login_required
# def my_enrollments(request):
#     enrollments = Enrollment.objects.filter(student=request.user)
#     return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

@login_required
def my_enrollments(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

@login_required
def enrollment_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/enrollment_dashboard.html', {'enrollments': enrollments})


# ----------------------------
# API Views (Generic Class Based)
# ----------------------------

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssignmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class EnrollmentCreateAPIView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        student = self.request.user
        course = serializer.validated_data['course']

        if Enrollment.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError({"detail": "You are already enrolled in this course."})

        serializer.save(student=student)

class SubmissionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
