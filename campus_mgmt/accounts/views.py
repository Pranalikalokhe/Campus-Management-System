from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from courses.models import Course
from submissions.models import Result  # ✅ Make sure you have imported your Result model

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):
    user = request.user
    if user.role == 'student':
        recent_results = Result.objects.filter(student=user).order_by('-id')[:5]
        return render(request, 'accounts/student_dashboard.html', {'recent_results': recent_results})
    elif user.role == 'teacher':
        courses = Course.objects.filter(teacher=user)
        return render(request, 'accounts/teacher_dashboard.html', {'courses': courses})
    elif user.role == 'admin':
        return render(request, 'accounts/admin_dashboard.html')
    else:
        return redirect('login')
