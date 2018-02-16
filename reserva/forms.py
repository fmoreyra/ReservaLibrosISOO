from django import forms
from django.contrib.auth.models import User
from reserva.models import Libro, Reserva
from functools import partial
import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class CreateReservaForm(forms.Form):
    libro = forms.ModelChoiceField(
        queryset=Libro.objects.filter(disponibilidad=True))
    fecha_encargo = forms.DateField(
        widget=DateInput())
    fecha_devolucion = forms.DateField(
        widget=DateInput())

    def clean(self):
       cleaned_data = self.cleaned_data
       usuario = cleaned_data.get("usuario")
       libro = cleaned_data.get("libro")
       fecha_devolucion = cleaned_data.get('fecha_devolucion')
       fecha_encargo = cleaned_data.get('fecha_encargo')

       if fecha_devolucion < fecha_encargo:
           raise ValidationError(_('La fecha de encargo debe ser anterior a la fecha de devolución'))
       if fecha_devolucion < datetime.date.today():
           raise ValidationError(_('La fecha de devolución es inválida, no puede ponerse una fecha del pasado'))
       if fecha_encargo < datetime.date.today():
           raise ValidationError(_('La fecha de encargo es inválida, no puede ponerse una fecha del pasado'))
       if fecha_devolucion > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(_('No se pueden reservar libros por un tiempo mayor a un mes.'))


       if Reserva.objects.filter(usuario=usuario, libro=libro).count() > 0:
           del cleaned_data["usuario"]
           del cleaned_data["libro"]
           raise forms.ValidationError(_("Ya existe un libro asignado al usuario seleccionado"))
       else:
           libro = Libro.objects.filter(pk=libro.pk)[0]
           libro.disponibilidad=False
           libro.save()
       return cleaned_data
