from django.core.exceptions import ValidationError


def name_contains_only_letters(value):
    if not value.isalpha():
        raise ValidationError('This field can only contain letters.')