from django.db import models
from django.core.validators import *
from frutipedia.fruits.validators import only_alphabets

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), MaxLengthValidator(30), only_alphabets])

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
