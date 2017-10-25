from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import extras
from django.contrib.auth.models import User
from localflavor.ar.forms import ARDNIField
from .choices import *

years = ( '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963',
        '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
        '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
        '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
        '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
        '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
        '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
        '2012', '2013', '2014', '2015', '2016', '2017')


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
        widget=extras.SelectDateWidget(years=years),
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
