from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from localflavor.ar.forms import ARDNIField
from .choices import *

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(
        max_length=30,
        help_text='Obligatorio.',
        label='Nombre')
    apellido = forms.CharField(
        max_length=30,
        help_text='Obligatorio.',
        label='Apellido')
    documento = ARDNIField(
        help_text='Obligatorio.',
        label='Número de DNI')
    legajo = forms.IntegerField(
        help_text='Obligatorio.',
        max_value=2147483640,
        min_value=0,
        label='Legajo')
    email = forms.EmailField(
        max_length=254,
        help_text='Obligatorio. Ingrese una dirección de E-Mail válida.',
        label='E-Mail')
    fecha_nacimiento = forms.DateField(
        help_text='Obligatorio. Formato: YYYY-MM-DD',
        label='Fecha de Nacimiento')
    carrera = forms.ChoiceField(
        choices=CARRERA,
        help_text='Obligatorio.',
        label='Carrera')

    class Meta:
        model = User
        fields = (
                'username',
                'password1',
                'password2',
                'nombre',
                'apellido',
                'documento',
                'legajo',
                'email',
                'fecha_nacimiento',
                'carrera',)
