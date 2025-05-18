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

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

@login_required
def enroll_in_course(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user
            enrollment.save()
            return redirect('my-courses')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enroll.html', {'form': form})

@login_required
def my_enrollments(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

@login_required
@role_required(['student'])
def enroll_in_course(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user
            enrollment.save()
            # 📧 Send confirmation email
            send_mail(
                'Enrollment Confirmation',
                f'Hi {request.user.username}, you have successfully enrolled in {enrollment.course.title}.',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=True,
            )
            messages.success(request, f'Enrolled successfully. Confirmation sent to {request.user.email}.')
            return redirect('course-list')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enroll.html', {'form': form})

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