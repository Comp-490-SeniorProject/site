"""Part 2 of the migration to add a one-to-one relationship between tests and schedules.

The schedule field is currently null. RunPython needs to be used to populate this field with a new
Schedule model instance.
"""

import math
from datetime import timedelta

from django.db import migrations
from django.utils import timezone


def update_test(apps, _):
    test_model = apps.get_model("api", "Test")
    schedule_model = apps.get_model("django_q", "Schedule")

    updated_tests = tuple(test_model.objects.all())
    new_schedules = []

    for test in updated_tests:
        total_runs = math.ceil((timezone.now() - test.created_at) / test.frequency)
        schedule = schedule_model(
            schedule_type="I",  # minutes
            minutes=math.ceil(test.frequency.total_seconds() / 60),
            next_run=test.created_at + (test.frequency * total_runs),
            func="print",
            args=f"'Running test {test.name} for param {test.parameter_id}'",
        )
        new_schedules.append(schedule)

    new_schedules = schedule_model.objects.bulk_create(new_schedules)

    for test, schedule in zip(updated_tests, new_schedules):
        test.schedule = schedule

    test_model.objects.bulk_update(updated_tests, ["schedule"])


def revert_test(apps, _):
    model = apps.get_model("api", "Test")
    updated_tests = tuple(model.objects.prefetch_related("schedule").all())

    type_to_delta = {
        "H": timedelta(hours=1),
        "D": timedelta(days=1),
        "W": timedelta(weeks=1),
        "M": timedelta(days=30),  # For simplicity, assume 1 month = 30 days
        "Q": timedelta(days=90),  # 3 months
        "Y": timedelta(days=365),  # For simplicity, assume 1 year = 365 days
    }

    for test in updated_tests:
        test.created_at = test.schedule.next_run

        if test.schedule.schedule_type in ("O", "C"):
            raise ValueError("Cannot revert tests which have a schedule_type of ONCE or CRON.")
        elif test.schedule.schedule_type == "I":
            test.frequency = timedelta(minutes=test.schedule.minutes)
        else:
            test.frequency = type_to_delta[test.schedule.schedule_type]

    model.objects.bulk_update(updated_tests, ["created_at", "frequency"])


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_test_add_django_q_schedule_1"),
    ]

    operations = [migrations.RunPython(update_test, revert_test)]
