from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from submissions.models import Submission

User = get_user_model()

@receiver(post_save, sender=User)
def assign_default_role(sender, instance, created, **kwargs):
    if created and not instance.role:
        instance.role = 'student'
        instance.save()

@receiver(post_save, sender=Submission)
def notify_student_on_grade(sender, instance, **kwargs):
    if instance.grade:
        send_mail(
            '📢 Your Submission Has Been Graded',
            f'Hi {instance.student.username},\n\nYour submission for \"{instance.assignment.title}\" has been graded.\nYour Grade: {instance.grade}\n\nRegards,\nCampus Management System',
            settings.DEFAULT_FROM_EMAIL,
            [instance.student.email],
            fail_silently=True,
        )
