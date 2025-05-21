from django.db import models
from courses.models import Course
from accounts.models import User

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.name})"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    file = models.FileField(upload_to='submissions/')
    submitted_on = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=5, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    average_grade = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} - {self.course.name}: {self.average_grade}"
    
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Submission)
def send_grading_notification(sender, instance, created, **kwargs):
    if not created and instance.grade:  # Only send when grade is updated
        subject = f"Assignment Graded: {instance.assignment.title}"
        message = f"Hello {instance.student.username},\n\nYour assignment '{instance.assignment.title}' has been graded. You received: {instance.grade}\n\nCheck for feedback if available.\n\nRegards,\nCampus Mgmt Team"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.student.email])
    