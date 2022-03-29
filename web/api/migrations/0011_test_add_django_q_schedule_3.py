"""Part 3 of the migration to add a one-to-one relationship between tests and schedules.

Fields are now populated, so they can be set back to non-nullable. Furthermore, the old fields are
no longer needed for population, so they can finally be removed.

This has to be a separate migration because combining schema changes and RunPython operations
leads to errors.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_test_add_django_q_schedule_2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="schedule",
            field=models.OneToOneField(
                null=False,
                help_text="The Django Q schedule for the test.",
                on_delete=models.CASCADE,
                to="django_q.schedule",
            ),
        ),
        migrations.RemoveField(
            model_name="test",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="test",
            name="frequency",
        ),
    ]
