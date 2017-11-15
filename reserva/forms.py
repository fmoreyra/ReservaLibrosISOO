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
    fecha_devolucion = forms.DateField(
        widget=DateInput())

    def clean(self):
       cleaned_data = self.cleaned_data
       usuario = cleaned_data.get("usuario")
       libro = cleaned_data.get("libro")
       fecha_devolucion = cleaned_data.get('fecha_devolucion')

       if fecha_devolucion < datetime.date.today():
           raise ValidationError(_('La fecha es inválida, no puede ponerse una fecha del pasado'))
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
