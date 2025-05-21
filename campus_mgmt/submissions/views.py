# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.http import JsonResponse

# from .models import Assignment, Submission, Result
# from .forms import SubmissionForm, AssignmentForm
# from accounts.decorators import role_required

# @login_required
# def assignment_upload(request):
#     if request.method == 'POST':
#         form = SubmissionForm(request.POST, request.FILES)
#         if form.is_valid():
#             submission = form.save(commit=False)
#             submission.student = request.user
#             submission.save()
#             return redirect('my-submissions')
#         else:
#             print("Form errors:", form.errors)
#     else:
#         form = SubmissionForm()
#     return render(request, 'submissions/upload.html', {'form': form})

# @login_required
# def my_submissions(request):
#     submissions = Submission.objects.filter(student=request.user)
#     return render(request, 'submissions/my_submissions.html', {'submissions': submissions})

# @login_required
# @role_required(['teacher'])
# def review_submissions(request):
#     submissions = Submission.objects.filter(assignment__course__teacher=request.user)

#     if request.method == 'POST':
#         submission_id = request.POST.get('submission_id')
#         grade = request.POST.get('grade')

#         submission = get_object_or_404(Submission, id=submission_id)
#         submission.grade = grade
#         submission.save()

#         messages.success(request, f"{submission.student.username} has been notified via email.")
#         return redirect('submission-review')

#     return render(request, 'submissions/review.html', {'submissions': submissions})

# @login_required
# def result_view(request):
#     results = Result.objects.filter(student=request.user)
#     return render(request, 'submissions/results.html', {'results': results})

# @login_required
# @role_required(['teacher'])
# def create_assignment(request):
#     if request.method == 'POST':
#         form = AssignmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = AssignmentForm()
#     return render(request, 'submissions/create_assignment.html', {'form': form})

# @login_required
# def ajax_load_assignments(request):
#     course_id = request.GET.get('course_id')
#     assignments = Assignment.objects.filter(course_id=course_id).values('id', 'title')
#     return JsonResponse(list(assignments), safe=False)

# @login_required
# def grade_submission(request, submission_id):
#     submission = get_object_or_404(Submission, id=submission_id)

#     if request.method == 'POST':
#         grade = request.POST.get('grade')
#         if grade:
#             submission.grade = grade
#             submission.save()
#             messages.success(request, "Grade saved and email sent to student successfully!")
#             return redirect('grade_submission', submission_id=submission.id)

#     return render(request, 'submissions/grade_submission.html', {'submission': submission})

# @login_required
# def student_results(request):
#     submissions = Submission.objects.filter(student=request.user)
#     return render(request, 'submissions/results.html', {'submissions': submissions})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from .models import Assignment, Submission, Result
from .forms import SubmissionForm, AssignmentForm
from accounts.decorators import role_required

@login_required
def assignment_upload(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.student = request.user
            submission.save()
            return redirect('my-submissions')
        else:
            print("Form errors:", form.errors)
    else:
        form = SubmissionForm()
    return render(request, 'submissions/upload.html', {'form': form})

@login_required
def my_submissions(request):
    submissions = Submission.objects.filter(student=request.user)
    return render(request, 'submissions/my_submissions.html', {'submissions': submissions})

@login_required
@role_required(['teacher'])
def review_submissions(request):
    submissions = Submission.objects.filter(assignment__course__teacher=request.user)

    if request.method == 'POST':
        submission_id = request.POST.get('submission_id')
        grade = request.POST.get('grade')

        submission = get_object_or_404(Submission, id=submission_id)
        submission.grade = grade
        submission.save()

        messages.success(request, f"{submission.student.username} has been notified via email.")
        return redirect('submission-review')

    return render(request, 'submissions/review.html', {'submissions': submissions})

@login_required
def result_view(request):
     results = Result.objects.filter(student=request.user)
     return render(request, 'submissions/results.html', {'results': results})
 



@login_required
@role_required(['teacher'])
def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AssignmentForm()
    return render(request, 'submissions/create_assignment.html', {'form': form})

@login_required
def ajax_load_assignments(request):
    course_id = request.GET.get('course_id')
    assignments = Assignment.objects.filter(course_id=course_id).values('id', 'title')
    return JsonResponse(list(assignments), safe=False)

@login_required
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)

    if request.method == 'POST':
        grade = request.POST.get('grade')
        if grade:
            submission.grade = grade
            submission.save()
            messages.success(request, "Grade saved and email sent to student successfully!")
            return redirect('grade_submission', submission_id=submission.id)

    return render(request, 'submissions/grade_submission.html', {'submission': submission})

@login_required
def student_results(request):
    submissions = Submission.objects.filter(student=request.user)
    return render(request, 'submissions/results.html', {'submissions': submissions})
