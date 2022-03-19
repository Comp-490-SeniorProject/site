"""Part 1 of the migration to make parameters and tests one-to-one.

Parameter.test and Test.device will eventually be deleted. To make this set of migrations
reversible, these fields have to be temporarily made nullable so that they can be populated.

This has to be a separate migration because combining schema changes and RunPython operations
leads to errors.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_test_priority"),
    ]

    operations = [
        # Allow null to enable this migration to be reversed.
        migrations.AlterField(
            model_name="parameter",
            name="test",
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                to="api.test",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="test",
            name="device",
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                to="api.device",
                null=True,
            ),
        ),
        # Rename to prevent conflict with new field's related name.
        migrations.RenameField(
            model_name="parameter",
            old_name="test",
            new_name="test_original",
        ),
        # Temporarily allow null.
        migrations.AddField(
            model_name="parameter",
            name="device",
            field=models.ForeignKey(
                help_text="The device which tests this parameter.",
                on_delete=models.CASCADE,
                related_name="parameters",
                to="api.device",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="parameter",
            field=models.OneToOneField(
                help_text="The parameter to test.",
                on_delete=models.CASCADE,
                to="api.parameter",
                null=True,
            ),
        ),
    ]
