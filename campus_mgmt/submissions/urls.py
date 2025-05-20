from django.urls import path
from . import views
from .views import ajax_load_assignments,submission_review


urlpatterns = [
    path('upload/', views.assignment_upload, name='assignment-upload'),
    path('review/', views.submission_review, name='submission-review'),
    path('results/', views.result_view, name='result-view'),
    path('create_assignment/', views.create_assignment, name='create-assignment'),
    path('ajax/load-assignments/', ajax_load_assignments, name='ajax-load-assignments'),
    path('my_submissions/', views.my_submissions, name='my-submissions'),
    
]
