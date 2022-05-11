from django.db import migrations, models

from web.utils.fields import NullEmailField


def set_blank_email_to_null(apps, _):
    user_model = apps.get_model("api", "User")
    user_model.objects.filter(email="").update(email=None)


def set_null_email_to_blank(apps, _):
    user_model = apps.get_model("api", "User")
    user_model.objects.filter(email__isnull=True).update(email="")


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        # The field type must not change before the data migration.
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True,
                max_length=254,
                null=True,
                verbose_name="email address",
            ),
        ),
        migrations.RunPython(set_blank_email_to_null, reverse_code=set_null_email_to_blank),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=NullEmailField(
                blank=True,
                error_messages={"unique": "A user with that email already exists."},
                max_length=254,
                null=True,
                unique=True,
                verbose_name="email address",
            ),
        ),
    ]
