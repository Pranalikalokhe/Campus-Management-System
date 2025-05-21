from rest_framework import serializers
from courses.models import Course, Enrollment
from submissions.models import Assignment, Submission

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.id')

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_on']

class SubmissionSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.id')

    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'student', 'content', 'submitted_on']
