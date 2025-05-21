from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Submission

@receiver(post_save, sender=Submission)
def notify_student_on_grade(sender, instance, created, **kwargs):
    # Only notify if submission was updated (not created) and grade is assigned
    if not created and instance.grade is not None:
        subject = 'Your submission has been graded'
        message = (
            f'Hello {instance.student.get_full_name()},\n\n'
            f'Your submission for "{instance.assignment.title}" has been graded.\n'
            f'Your grade: {instance.grade}\n\n'
            'Thank you.'
        )
        recipient_list = [instance.student.email]
        send_mail(subject, message, None, recipient_list)
