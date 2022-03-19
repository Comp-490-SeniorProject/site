import pgtrigger
from django.db import models
from django.utils import timezone

from web.utils.triggers import ProtectColumn

from .parameter import Parameter


@pgtrigger.register(ProtectColumn(name="api_test_protect_parameter_update", column="parameter"))
class Test(models.Model):

    name = models.TextField(help_text="A user-friendly string that names the test.")
    description = models.TextField(blank=True, help_text="A description of the test.")
    created_at = models.DateTimeField(
        default=timezone.now, help_text="The date and time of the creation of this test."
    )
    frequency = models.DurationField(help_text="The frequency of execution for the test.")
    parameter = models.OneToOneField(
        Parameter, on_delete=models.CASCADE, help_text="The parameter to test."
    )
