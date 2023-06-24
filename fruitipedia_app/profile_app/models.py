from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.validators.validators import validate_name_first_character


# Create your models here.
class ProfileModel(models.Model):
    MAX_FIRST_NAME_LENGTH = 25
    MIN_FIRST_NAME_LENGTH = 2

    MAX_LAST_NAME_LENGTH = 35
    MIN_LAST_NAME_LENGTH = 1

    MAX_EMAIL_LENGTH = 40

    MAX_PASSWORD_LENGTH = 20
    MIN_PASSWORD_LENGTH = 8

    DEFAULT_AGE_VALUE = 18

    first_name = models.CharField(
        verbose_name='First Name',
        null=False,
        blank=False,
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            validate_name_first_character,
        )
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        null=False,
        blank=False,
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
            validate_name_first_character,
        )
    )

    email = models.EmailField(
        verbose_name='Email',
        null=False,
        blank=False,
        max_length=MAX_EMAIL_LENGTH,
    )

    password = models.CharField(
        verbose_name='Password',
        max_length=MAX_PASSWORD_LENGTH,
        validators=(
            MinLengthValidator(MIN_PASSWORD_LENGTH),
        )
    )

    image = models.URLField(
        verbose_name='Image URL',
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        verbose_name='Age',
        null=True,
        blank=True,
        default=DEFAULT_AGE_VALUE
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
