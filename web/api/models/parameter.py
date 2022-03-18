from django.db import models
from django.utils.translation import gettext_lazy as _

from .test import Test


class ParameterType(models.TextChoices):
    AUTO = "auto", _("Automatic")
    MANUAL = "man", _("Manual")
    SEMI = "semi", _("Semi-automatic")


class Parameter(models.Model):

    name = models.TextField(help_text="A user-friendly string that names the parameter.")
    description = models.TextField(blank=True, help_text="A description of the parameter.")
    unit = models.TextField(help_text="The name of the unit of measurement for the parameter.")
    type = models.CharField(
        max_length=4,
        choices=ParameterType.choices,
        help_text="Determines how the parameter is tested and how its data is collected.",
    )
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, help_text="The test which sets this parameter."
    )
