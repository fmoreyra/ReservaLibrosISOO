from django.shortcuts import render
from django.views import generic
from reserva.models import Libro, Reserva
from reserva.forms import CreateReservaForm
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
import datetime
from django.http import HttpResponseRedirect


class LibroDetailView(generic.DetailView):
    model = Libro

class ReservaCreateView(generic.edit.CreateView):
    model = Reserva
    fields = '__all__'

def CreateReserva(request):
    if request.method == 'POST':
        form = CreateReservaForm(request.POST)

        if form.is_valid():
            libro = form.cleaned_data.get('libro')
            usuario = request.user.profile.user
            fecha_despacho = form.cleaned_data.get('fecha_despacho')
            fecha_devolucion = form.cleaned_data.get('fecha_devolucion')

            reserva = Reserva(
                libro=libro,
                usuario=usuario,
                fecha_despacho=fecha_despacho,
                fecha_devolucion=fecha_devolucion)
            reserva.save()
            return redirect('home')
    else:
        form = CreateReservaForm()
    data = {
        'form': form
    }
    return render(request, 'reserva_form.html', data)

def ReservaQuery(request):

    usuario = request.user
    reservaQuery = Reserva.objects.all()
    if usuario.is_authenticated():
        reservaQuery = Reserva.objects.filter(usuario = usuario)
    data = {
        'reservaQuery': reservaQuery
    }
    return render(request, 'home.html', data)

def AdminQuery(request):
    reservaEncargoToday = Reserva.objects.filter(fecha_despacho=datetime.date.today())
    reservaDevolucionFalseUnknown = Reserva.objects.exclude(devuelto=True)
    data = {
        'reservaEncargoToday': reservaEncargoToday,
        'reservaDevolucionFalseUnknown': reservaDevolucionFalseUnknown,
    }
    return render(request, 'admin_view.html', data)

class DeleteReserva(DeleteView):
    model = Reserva
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.libro.disponibilidad = True
       self.object.libro.save()
       self.object.delete()
       return HttpResponseRedirect(self.get_success_url())
