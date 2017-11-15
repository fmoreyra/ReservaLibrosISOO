from django.shortcuts import render
from django.views import generic
from reserva.models import Libro, Reserva
from reserva.forms import CreateReservaForm
from django.shortcuts import render, redirect
import pdb

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
            fecha_devolucion = form.cleaned_data.get('fecha_devolucion')
            reserva = Reserva(libro=libro, usuario=usuario, fecha_devolucion=fecha_devolucion)
            reserva.save()
            return redirect('home')
    else:
        form = CreateReservaForm()
    data = {
        'form': form
    }
    return render(request, 'reserva_form.html', data)
