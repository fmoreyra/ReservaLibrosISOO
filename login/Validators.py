from django.core.exceptions import ValidationError


def alphanumeric(value):
    if value.isdigit():
        raise ValidationError("Verifique que no sea ingresado ningún número")