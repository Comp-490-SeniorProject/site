from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core import exceptions
from django.db import models

from web.utils import json

__all__ = ("ChoiceArrayField", "NullEmailField")


class ChoiceArrayField(ArrayField):
    """
    A PostgreSQL ArrayField that supports the choices property.

    Ref. https://gist.github.com/danni/f55c4ce19598b2b345ef#gistcomment-3408902.
    """

    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)

    def to_python(self, value):
        res = super().to_python(value)
        if isinstance(res, list):
            value = [self.base_field.to_python(val) for val in res]
        return value

    def validate(self, value, model_instance):
        if not self.editable:
            # Skip validation for non-editable fields.
            return

        if self.choices is not None and value not in self.empty_values:
            if set(value).issubset({option_key for option_key, _ in self.choices}):
                return
            raise exceptions.ValidationError(
                self.error_messages["invalid_choice"],
                code="invalid_choice",
                params={"value": value},
            )

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages["null"], code="null")

        if not self.blank and value in self.empty_values:
            raise exceptions.ValidationError(self.error_messages["blank"], code="blank")


class OrjsonField(models.JSONField):
    """A JSONField which uses orjson for encoding/decoding."""

    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs["encoder"] = json.OrjsonEncoder
        kwargs["decoder"] = json.OrjsonDecoder
        super().__init__(verbose_name, name, **kwargs)


class NullEmailField(models.EmailField):
    """A `django.db.models.EmailField` which stores empty strings as NULL."""

    def from_db_value(self, value, *_):
        return "" if value is None else value

    def to_python(self, value):
        if isinstance(value, str):
            return value
        elif value is None:
            return ""

        return str(value)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return None if value.strip() == "" else value
