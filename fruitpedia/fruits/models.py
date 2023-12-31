from django.db import models
from django.core.validators import *
from fruitpedia.fruits.validators import only_alphabets


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    CHOICES_CATEGORY = [(str(category.name), str(category.name)) for category in Category.objects.all()]

    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), MaxLengthValidator(30), only_alphabets])

    image_url = models.URLField()

    category = models.CharField(max_length=255, choices=CHOICES_CATEGORY)

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
