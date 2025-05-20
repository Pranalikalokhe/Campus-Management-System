# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView
# from django.contrib.auth.decorators import login_required
# from .models import Course, Enrollment
# from .forms import EnrollmentForm
# from django.contrib.auth.decorators import login_required 
# from django.core.mail import send_mail
# from accounts.decorators import role_required
# from django.contrib import messages
# from django.conf import settings
# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.db import IntegrityError
# from .models import Enrollment
# from api.serializers import AssignmentSerializer

# #from assignments.models import Submission
# # Add this at the top
# #from .forms import GradeForm    # Form to enter grades

# class CourseListView(ListView):
#     model = Course
#     template_name = 'courses/course_list.html'
#     context_object_name = 'courses'
#     paginate_by = 5
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) | Q(description__icontains=query)
#             )
#         return queryset
# class CourseDetailView(DetailView):
#     model = Course
#     template_name = 'courses/course_detail.html'
#     context_object_name = 'course'

# @login_required
# def enroll_in_course(request):
#     if request.method == 'POST':
#         form = EnrollmentForm(request.POST)
#         if form.is_valid():
#             enrollment = form.save(commit=False)
#             enrollment.student = request.user
#             enrollment.save()
#             return redirect('my-courses')
#     else:
#         form = EnrollmentForm()
#     return render(request, 'courses/enroll.html', {'form': form})

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# #from .serializers import AssignmentSerializer
# #from .models import Assignment

# class AssignmentUploadView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = AssignmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(uploaded_by=request.user)  # assumes uploaded_by is in model
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @login_required
# def my_enrollments(request):
#     enrollments = Enrollment.objects.filter(student=request.user)
#     return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

# @login_required
# @role_required(['student'])
# def enroll_in_course(request):
#     if request.method == 'POST':
#         form = EnrollmentForm(request.POST)
#         if form.is_valid():
#             course = form.cleaned_data['course']

#             # Check if already enrolled
#             already_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
#             if already_enrolled:
#                 messages.warning(request, "You are already enrolled in this course.")
#                 return redirect('course-list')

#             # Save new enrollment
#             enrollment = form.save(commit=False)
#             enrollment.student = request.user
#             enrollment.save()

#             # Send confirmation email
#             send_mail(
#                 'Enrollment Confirmation',
#                 f'Hi {request.user.username}, you have successfully enrolled in {course.name}.',
#                 settings.DEFAULT_FROM_EMAIL,
#                 [request.user.email],
#                 fail_silently=True,
#             )

#             messages.success(request, f'Enrolled successfully! Confirmation sent to {request.user.email}.')
#             return redirect('course-list')
#     else:
#         form = EnrollmentForm()
#     return render(request, 'courses/enroll.html', {'form': form})

# class CourseListView(ListView):
#     model = Course
#     template_name = 'courses/course_list.html'
#     context_object_name = 'courses'
#     paginate_by = 5

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) | Q(description__icontains=query)
#             )

#         return queryset
    
# @login_required
# def enrollment_dashboard(request):
#     # Fetch all enrollments of the logged-in user (student)
#     enrollments = Enrollment.objects.filter(student=request.user)

#     context = {
#         'enrollments': enrollments,
#     }
#     return render(request, 'courses/enrollment_dashboard.html', context) 

# # @login_required
# # @role_required(['teacher'])  # Only teachers can grade
# # def grade_submission(request, submission_id):
# #     submission = get_object_or_404(Submission, id=submission_id)

# #     if request.method == 'POST':
# #         form = GradeForm(request.POST, instance=submission)
# #         if form.is_valid():
# #             form.save()

# #             # Show success message
# #             messages.success(request, "Grade saved successfully.")

# #             # Redirect to list of submissions or teacher dashboard
# #             return redirect('teacher-submissions')  # adjust this name based on your URL
# #     else:
# #         form = GradeForm(instance=submission)

# #     return render(request, 'courses/grade_submission.html', {'form': form, 'submission': submission})

# Updated `courses/views.py` (API integration included)

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from .forms import EnrollmentForm
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from accounts.decorators import role_required
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q
from django.db import IntegrityError

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

@login_required
@role_required(['student'])
def enroll_in_course(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            if Enrollment.objects.filter(student=request.user, course=course).exists():
                messages.warning(request, "You are already enrolled in this course.")
                return redirect('course-list')

            enrollment = form.save(commit=False)
            enrollment.student = request.user
            enrollment.save()

            send_mail(
                'Enrollment Confirmation',
                f'Hi {request.user.username}, you have successfully enrolled in {course.name}.',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=True,
            )
            messages.success(request, f'Enrolled successfully! Confirmation sent to {request.user.email}.')
            return redirect('course-list')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enroll.html', {'form': form})

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
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class SubmissionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
