from django.urls import path
from . import views
from .views import CourseListView

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('enroll/', views.enroll_in_course, name='enroll-course'),
    path('my/', views.my_enrollments, name='my-courses'),
    path('', CourseListView.as_view(), name='course-list'),
]
