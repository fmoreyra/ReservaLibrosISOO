from django.shortcuts import render
from django.views import generic
from reserva.models import Libro

class LibroDetailView(generic.DetailView):
    model = Libro
