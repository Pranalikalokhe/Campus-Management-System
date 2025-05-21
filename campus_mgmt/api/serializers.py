# from rest_framework import serializers
# from courses.models import Course
# from submissions.models import Assignment, Submission
# from courses.models import Enrollment

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['id', 'title', 'description', 'teacher']

# class AssignmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assignment
#         fields = ['id', 'course', 'title', 'description', 'due_date']

# class EnrollmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Enrollment
#         fields = ['id', 'student', 'course', 'enrolled_on']

# class SubmissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Submission
#         fields = ['id', 'assignment', 'student', 'file', 'grade']
#         read_only_fields = ['grade', 'student']
from rest_framework import serializers
from courses.models import Course, Enrollment
from submissions.models import Assignment, Submission

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # Use 'name' instead of 'title' here to match your model
        fields = ['id', 'name', 'description', 'teacher']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'course', 'title', 'description', 'due_date']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_on']
        read_only_fields = ['student']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'student', 'file', 'grade']
        read_only_fields = ['grade', 'student']
