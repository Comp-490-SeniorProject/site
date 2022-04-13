"""Part 2 of the migration to make parameters and tests one-to-one.

Fields are currently null. RunPython needs to be used to populate these fields with their actual
values.
"""

import copy

from django.db import migrations, models


def update_parameter(apps, _):
    """Set parameter_device to parameter_test_original__device."""
    model = apps.get_model("api", "Parameter")

    params = model.objects.filter(pk=models.OuterRef("pk"))
    subquery = models.Subquery(params.values("test_original__device")[:1])
    model.objects.update(device=subquery)


def update_test(apps, _):
    """Set test_parameter to the 1st value of test_parameter_set and create copies for the rest."""
    model = apps.get_model("api", "Test")
    new_tests = []
    updates_tests = []

    for test in model.objects.prefetch_related("parameter_set").all():
        # Use the first parameter for the extant test.
        test.parameter = test.parameter_set.first()
        updates_tests.append(test)

        # Create a copy for each remaining parameter.
        for parameter in test.parameter_set.all()[1:]:
            new_test = copy.deepcopy(test)
            new_tests.append(new_test)

            new_test.id = None
            new_test._state.adding = True
            new_test.parameter_id = parameter.id

    model.objects.bulk_create(new_tests)
    model.objects.bulk_update(updates_tests, ["parameter"])


def revert_test(apps, _):
    """Set test_device to test_parameter__device."""
    model = apps.get_model("api", "Test")

    tests = model.objects.filter(pk=models.OuterRef("pk"))
    subquery = models.Subquery(tests.values("parameter__device")[:1])
    model.objects.update(device=subquery)


def revert_parameter(apps, _):
    """Set parameter_test_original to parameter_test."""
    model = apps.get_model("api", "Parameter")

    params = model.objects.filter(pk=models.OuterRef("pk"))
    subquery = models.Subquery(params.values("test")[:1])
    model.objects.update(test_original=subquery)


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_parameter_test_1to1_1"),
    ]

    operations = [
        # Replace the null values with the actual values.
        migrations.RunPython(update_parameter, revert_parameter),
        migrations.RunPython(update_test, revert_test),
    ]
