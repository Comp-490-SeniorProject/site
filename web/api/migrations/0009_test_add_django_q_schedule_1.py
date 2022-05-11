"""Part 1 of the migration to add a one-to-one relationship between tests and schedules.

Test.frequency and Test.created_at will eventually be deleted. While the latter has a default value,
the former does not. To make this set of migrations reversible, that field has to be temporarily
made nullable so that it can be populated during reversal. This also applies to the new schedule
field.

This has to be a separate migration because combining schema changes and RunPython operations
leads to errors.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_q", "0014_schedule_cluster"),
        ("api", "0008_parameter_sensor_id"),
    ]

    operations = [
        # Allow null to enable this migration to be reversed.
        # created_at has a default, so it doesn't need null to be allowed.
        migrations.AlterField(
            model_name="test",
            name="frequency",
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name="test",
            name="schedule",
            field=models.OneToOneField(
                null=True,
                help_text="The Django Q schedule for the test.",
                on_delete=models.CASCADE,
                to="django_q.schedule",
            ),
        ),
    ]
