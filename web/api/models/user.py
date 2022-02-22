from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from web.utils.fields import NullEmailField


class User(AbstractUser):
    email = NullEmailField(
        _("email address"),
        null=True,
        blank=True,
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
