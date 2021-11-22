from django.conf import settings
from django.db import models


class Device(models.Model):

    name = models.TextField(help_text="A user-friendly string that identifies the device.")
    description = models.TextField(blank=True, help_text="A description of the device.")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="The user which owns the device.",
    )
