from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_auth_token_and_assign_role(sender, instance=None, created=False, **kwargs):
    if created:
        # Create auth token
        Token.objects.create(user=instance)

        # Assign default role if not set
        # If your User model has a 'role' field:
        if not getattr(instance, 'role', None):
            instance.role = 'student'  # or whatever your default role is
            instance.save()


