from django.db import models
from accounts.models import User
from accounts.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name

class Enrollment(models.Model):
     student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
     course = models.ForeignKey(Course, on_delete=models.CASCADE)
     enrolled_on = models.DateTimeField(auto_now_add=True)

     class Meta:
         unique_together = ('student', 'course')

     def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"


