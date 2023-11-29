from django.core.exceptions import ValidationError


def only_alphabets(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")