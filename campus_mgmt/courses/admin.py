from django.contrib import admin
from .models import Course, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'created_at']
    search_fields = ['name']
    list_filter = ['teacher']
    inlines = [EnrollmentInline]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrolled_on']
    list_filter = ['course', 'student']
    search_fields = ['student__username', 'course__name']
