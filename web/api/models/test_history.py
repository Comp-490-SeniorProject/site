from django.db import models

from . import Test


class TestStatus(models.TextChoices):
    SCHEDULED = "SC"
    CANCELLED = "CA"
    RUNNING = "RU"
    SUCCEEDED = "SU"
    FAILED = "FA"


class TestHistory(models.Model):

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
        choices=TestStatus.choices,
        default=TestStatus.SCHEDULED,
        help_text="The current status of this test instance's execution.",
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="scheduled_timestamps_null",
                check=models.Q(
                    status__exact=TestStatus.SCHEDULED,
                    started_at__isnull=True,
                    ended_at__isnull=True,
                ),
            ),
            models.CheckConstraint(
                name="running_started_at_not_null_ended_at_null",
                check=models.Q(
                    status__exact=TestStatus.RUNNING,
                    started_at__isnull=False,
                    ended_at__isnull=True,
                ),
            ),
            models.CheckConstraint(
                name="succeeded_timestamps_not_null",
                check=models.Q(
                    status__exact=TestStatus.SUCCEEDED,
                    started_at__isnull=False,
                    ended_at__isnull=False,
                ),
            ),
            models.CheckConstraint(
                name="cancelled_ended_at_not_null",
                check=models.Q(status__exact=TestStatus.CANCELLED, ended_at__isnull=False),
            ),
        ]
