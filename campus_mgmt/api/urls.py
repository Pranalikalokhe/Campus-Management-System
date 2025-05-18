from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CourseListAPIView, AssignmentCreateAPIView, EnrollmentCreateAPIView, SubmissionCreateAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('courses/', CourseListAPIView.as_view(), name='api_courses'),
    path('assignments/', AssignmentCreateAPIView.as_view(), name='api_create_assignment'),
    path('enrollments/', EnrollmentCreateAPIView.as_view(), name='api_enroll'),
    path('submissions/', SubmissionCreateAPIView.as_view(), name='api_submit'),
]
