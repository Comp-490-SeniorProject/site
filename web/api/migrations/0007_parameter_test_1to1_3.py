"""Part 3 of the migration to make parameters and tests one-to-one.

Fields are now populated, so they can be set back to non-nullable. Furthermore, the old fields are
no longer needed for population, so they can finally be removed.

This has to be a separate migration because combining schema changes and RunPython operations
leads to errors.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_parameter_test_1to1_2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parameter",
            name="device",
            field=models.ForeignKey(
                help_text="The device which tests this parameter.",
                on_delete=models.CASCADE,
                related_name="parameters",
                to="api.device",
                null=False,
            ),
        ),
        migrations.AlterField(
            model_name="test",
            name="parameter",
            field=models.OneToOneField(
                help_text="The parameter to test.",
                on_delete=models.CASCADE,
                to="api.parameter",
                null=False,
            ),
        ),
        migrations.RemoveField(
            model_name="parameter",
            name="test_original",
        ),
        migrations.RemoveField(
            model_name="test",
            name="device",
        ),
    ]
