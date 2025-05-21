from django.shortcuts import render, redirect
from .models import Assignment, Submission
from .forms import SubmissionForm, AssignmentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from accounts.decorators import role_required 
from django.http import JsonResponse
from .models import Assignment

 
@login_required
def assignment_upload(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        print("POST request received")
        if form.is_valid():
            print("Form is valid")
            submission = form.save(commit=False)
            submission.student = request.user
            submission.save()
            print("Saved Submission:", submission)
            return redirect('my-submissions')
        else:
            print("Form errors:", form.errors)  # This will print form validation errors
    else:
        form = SubmissionForm()
    return render(request, 'submissions/upload.html', {'form': form})


@login_required
def my_submissions(request):
    submissions = Submission.objects.filter(student=request.user)
    return render(request, 'submissions/my_submissions.html', {'submissions': submissions})

@login_required
def submission_review(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')
    submissions = Submission.objects.all()
    return render(request, 'submissions/review.html', {'submissions': submissions})

@login_required
def result_view(request):
    from .models import Result
    results = Result.objects.filter(student=request.user)
    return render(request, 'submissions/results.html', {'results': results})

@login_required
def create_assignment(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AssignmentForm()
    return render(request, 'submissions/create_assignment.html', {'form': form})

@login_required
@role_required(['teacher'])
def submission_review(request):
    # Only get submissions related to the teacher's courses
    submissions = Submission.objects.filter(assignment__course__teacher=request.user)

    if request.method == 'POST':
        submission_id = request.POST.get('submission_id')
        grade = request.POST.get('grade')
        submission = Submission.objects.get(id=submission_id)
        submission.grade = grade
        submission.save()
        messages.success(request, f"{submission.student.username} has been notified via email.")
        return redirect('submission-review')

    return render(request, 'submissions/review.html', {'submissions': submissions})

@login_required
def ajax_load_assignments(request):
     course_id = request.GET.get('course_id')
     assignments = Assignment.objects.filter(course_id=course_id).values('id', 'title')
     return JsonResponse(list(assignments), safe=False)

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from submissions.models import Submission
from django.contrib.auth.decorators import login_required

@login_required
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)

    if request.method == 'POST':
        grade = request.POST.get('grade')
        if grade:
            submission.grade = grade
            submission.save()  # This triggers the signal and email

            # ✅ Add message for success
            messages.success(request, "Grade saved and email sent to student successfully!")

            # ✅ Redirect to same page so alert shows after reload
            return redirect('grade_submission', submission_id=submission.id)

    return render(request, 'submissions/grade_submission.html', {'submission': submission})
