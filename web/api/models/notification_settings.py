from django.db import models

from web.utils import fields

from . import Test


class NotificationDest(models.TextChoices):
    EMAIL = "EM"
    WEB = "WE"


class NotificationSettings(models.Model):
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, help_text="The test for which to notify."
    )
    condition = models.TextField(
        help_text="An expression to evaluate to determine whether to notify."
    )
    message = models.TextField(blank=True, help_text="The message to display in the notification.")
    destination = fields.ChoiceArrayField(
        models.CharField(
            max_length=2,
            choices=NotificationDest.choices,
            default=(NotificationDest.WEB,),
            help_text="Where to send the notification.",
        )
    )