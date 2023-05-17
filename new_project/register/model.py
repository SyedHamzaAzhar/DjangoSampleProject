from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings


from django.db import models


class TODO(models.Model):

    
    title = models.CharField(
        max_length=50,
        null=True,
        unique=True
    )
    subject = models.TextField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
      auto_now_add=True,
      null=True
    )

    updated_at = models.DateTimeField(

        null=True
    )


    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)