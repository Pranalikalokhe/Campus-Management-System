# from django.urls import path
# from . import views
# from .views import ajax_load_assignments, review_submissions


# urlpatterns = [
#     path('upload/', views.assignment_upload, name='assignment-upload'),
#     path('review/', review_submissions, name='submission-review'),

#     path('results/', views.result_view, name='result-view'),
#     path('create_assignment/', views.create_assignment, name='create-assignment'),
#     path('ajax/load-assignments/', ajax_load_assignments, name='ajax-load-assignments'),
#     path('my_submissions/', views.my_submissions, name='my-submissions'),
#     path('review-submissions/', views.review_submissions, name='review_submissions'),
#     path('student-results/', views.student_results, name='student_results'),
#     path('grade/<int:submission_id>/', views.grade_submission, name='grade_submission'),
    
# ]
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

