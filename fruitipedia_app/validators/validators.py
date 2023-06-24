from django.core.exceptions import ValidationError


def validate_name_first_character(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_name_only_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
