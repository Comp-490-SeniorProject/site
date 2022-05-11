from django.db import migrations, models


def set_type_to_is_manual(apps, _):
    model = apps.get_model("api", "Parameter")
    # Remaining records are auto by default.
    model.objects.filter(is_manual=True).update(type="man")


def set_is_manual_to_type(apps, _):
    model = apps.get_model("api", "Parameter")
    # Remaining records are not manual by default.
    # Set semi to manual to be safe.
    model.objects.exclude(type="auto").update(is_manual=True)


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_unique_user_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="parameter",
            name="type",
            field=models.CharField(
                choices=[("auto", "Automatic"), ("man", "Manual"), ("semi", "Semi-automatic")],
                default="auto",
                help_text="Determines how the parameter is tested and how its data is collected.",
                max_length=4,
            ),
            preserve_default=False,
        ),
        migrations.RunPython(set_type_to_is_manual, reverse_code=set_is_manual_to_type),
        migrations.RemoveField(
            model_name="parameter",
            name="is_manual",
        ),
    ]
