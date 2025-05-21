
from django.urls import path
from .views import (
    ajax_load_assignments,
    review_submissions,
    assignment_upload,
    my_submissions,
    result_view,
    create_assignment,
    grade_submission,
    student_results,
)

urlpatterns = [
    path('upload/', assignment_upload, name='assignment-upload'),
    path('my-submissions/', my_submissions, name='my-submissions'),
    path('review/', review_submissions, name='review_submissions'),
    path('results/', result_view, name='result-view'),
    path('create-assignment/', create_assignment, name='create-assignment'),
    path('ajax/load-assignments/', ajax_load_assignments, name='ajax-load-assignments'),
    path('grade/<int:submission_id>/', grade_submission, name='grade_submission'),
    path('student-results/', student_results, name='student-results'),
]

