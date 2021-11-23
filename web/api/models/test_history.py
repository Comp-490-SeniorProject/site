from django.db import models

from . import Test


class TestHistory(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = "SC"
        CANCELLED = "CA"
        RUNNING = "RU"
        SUCCEEDED = "SU"
        FAILED = "FA"

    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, help_text="The test to which this history pertains."
    )
    started_at = models.DateTimeField(
        null=True, help_text="The date and time when test execution started."
    )
    ended_at = models.DateTimeField(
        null=True, help_text="The date and time when test execution ended."
    )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.SCHEDULED,
        help_text="The current status of this test instance's execution.",
    )
