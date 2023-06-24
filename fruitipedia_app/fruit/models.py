from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.validators.validators import validate_name_only_letters


# Create your models here.
class FruitModel(models.Model):
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 2

    name = models.CharField(
        verbose_name='Name',
        null=False,
        blank=False,
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
            validate_name_only_letters,
        )
    )

    image = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name='Description',
        null=False,
        blank=False,

    )

    nutrition = models.TextField(
        verbose_name='Nutrition',
        null=False,
        blank=False,
    )