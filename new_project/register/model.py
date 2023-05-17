from django.db import models


class TODO(models.Models):

    
    ttile = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )
    subject = models.EmailField(
        null=True,
        blank=True
    )
    created_at = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )