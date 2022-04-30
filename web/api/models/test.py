import pgtrigger
from django.db import models
from django_q.models import Schedule

from web.utils.triggers import ProtectColumn

from .parameter import Parameter


@pgtrigger.register(ProtectColumn(name="api_test_protect_parameter_update", column="parameter"))
class Test(models.Model):

    name = models.TextField(help_text="A user-friendly string that names the test.")
    description = models.TextField(blank=True, help_text="A description of the test.")
    parameter = models.OneToOneField(
        Parameter, on_delete=models.CASCADE, help_text="The parameter to test."
    )
    schedule = models.OneToOneField(
        Schedule, on_delete=models.CASCADE, help_text="The Django Q schedule for the test."
    )

    def delete(self, *args, **kwargs):
        """Delete the Schedule when the Test is deleted."""
        super().delete(*args, **kwargs)
        self.schedule.delete()
