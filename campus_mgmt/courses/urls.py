# from django.urls import path
# from . import views
# from .views import CourseListView, enrollment_dashboard
# #from .views import grade_submission
# from .views import CourseListView, AssignmentUploadView, EnrollmentView, GradeSubmissionView


# urlpatterns = [
#     path('', views.CourseListView.as_view(), name='course-list'),
#     path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
   
#     path('my/', views.my_enrollments, name='my-courses'),
#     path('', CourseListView.as_view(), name='course-list'),
#     path('dashboard/', enrollment_dashboard, name='enrollment_dashboard'),
#     path('courses/', CourseListView.as_view(), name='course-list'),
#     path('assignments/upload/', AssignmentUploadView.as_view(), name='assignment-upload'),
#     path('enroll/', EnrollmentView.as_view(), name='enrollment'),
#     path('grade/', GradeSubmissionView.as_view(), name='grade'),
#     # path('grade/<int:submission_id>/', grade_submission, name='grade-submission'),
# ]   



from django.urls import path
from . import views
#from .views import AssignmentUploadView
from .views import enroll_course

urlpatterns = [
    # Web views
    path('', views.CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('my/', views.my_enrollments, name='my-courses'),
    path('dashboard/', views.enrollment_dashboard, name='enrollment_dashboard'),

    # API views
    path('api/courses/', views.CourseListAPIView.as_view(), name='api-course-list'),
    path('api/assignments/upload/', views.AssignmentCreateAPIView.as_view(), name='api-assignment-upload'),
    path('api/enroll/', views.EnrollmentCreateAPIView.as_view(), name='api-enroll'),
    path('enroll/', views.enroll_course, name='enroll-course'),
    path('api/enroll/', enroll_course, name='enroll-course-api'),
    path('api/submissions/', views.SubmissionCreateAPIView.as_view(), name='api-submission'),
    #path('assignments/upload/', AssignmentUploadView.as_view(), name='assignment-upload'),
]
