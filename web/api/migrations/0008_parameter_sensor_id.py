import itertools

from django.db import migrations, models

counter = itertools.count()


def set_sensor_id(apps, _):
    """Set the sensor_id of each non-manual Parameter to a unique value."""
    model = apps.get_model("api", "Parameter")

    params = tuple(model.objects.filter(~models.Q(type="man")))
    for param in params:
        param.sensor_id = next(counter)

    model.objects.bulk_update(params, ["sensor_id"])


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_parameter_test_1to1_3"),
    ]

    operations = [
        migrations.AddField(
            model_name="parameter",
            name="sensor_id",
            field=models.PositiveSmallIntegerField(
                help_text="The ID of the sensor which corresponds to this parameter.", null=True
            ),
        ),
        migrations.RunPython(set_sensor_id, migrations.RunPython.noop),
        migrations.AddConstraint(
            model_name="parameter",
            constraint=models.CheckConstraint(
                check=models.Q(type="man") | models.Q(sensor_id__isnull=False),
                name="auto_sensor_not_null",
            ),
        ),
        migrations.AddConstraint(
            model_name="parameter",
            constraint=models.UniqueConstraint(
                condition=models.Q(sensor_id__isnull=False),
                fields=("sensor_id", "device"),
                name="unique_device_sensor",
            ),
        ),
    ]
