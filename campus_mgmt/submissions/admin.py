from django.contrib import admin
from .models import Assignment, Submission, Result

class SubmissionInline(admin.TabularInline):
    model = Submission
    extra = 1

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'due_date']
    search_fields = ['title', 'course__name']
    list_filter = ['course']
    inlines = [SubmissionInline]


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'submitted_on', 'grade']
    list_filter = ['assignment', 'grade']
    search_fields = ['assignment__title', 'student__username']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'average_grade']
    list_filter = ['course']
    search_fields = ['student__username', 'course__name', 'created_on']
