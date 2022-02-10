from django.db import models

from .test import Test


class Parameter(models.Model):

    name = models.TextField(help_text="A user-friendly string that names the parameter.")
    description = models.TextField(blank=True, help_text="A description of the parameter.")
    unit = models.TextField(help_text="The name of the unit of measurement for the parameter.")
    is_manual = models.BooleanField(
        default=False,
        help_text="Whether the parameter has to be set manually by a user after a test run.",
    )
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, help_text="The test which sets this parameter."
    )
