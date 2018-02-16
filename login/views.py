from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from login.forms import SignUpForm
from django.contrib.auth.models import User
from .filters import ProfileFilter, LibroFilter
from django.http import JsonResponse
from login.models import Profile
from reserva.models import Libro
from django.views import generic

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Ingresar lo contenido x el form a partir de esta línea
            user.profile.apellido = form.cleaned_data.get('apellido')
            user.profile.nombre = form.cleaned_data.get('nombre')
            user.profile.documento = form.cleaned_data.get('documento')
            user.profile.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            user.profile.carrera = form.cleaned_data.get('carrera')
            user.profile.legajo = form.cleaned_data.get('legajo')
            user.email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user.save()
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def validate_legajo(request):
    legajo = request.GET.get('legajo', None)
    data = {
        'is_taken': Profile.objects.filter(legajo__iexact=legajo).exists()
    }
    return JsonResponse(data)

def validate_documento(request):
    documento = request.GET.get('documento', None)
    data = {
        'is_taken': Profile.objects.filter(documento__iexact=documento).exists()
    }
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)

class ProfileDetailView(generic.DetailView):
    model = Profile

def profile_search(request):
    profile_list = Profile.objects.all()
    profile_filter = ProfileFilter(request.GET, queryset=profile_list)
    return render(request, 'profile_list.html', {'filter': profile_filter})

def libro_search(request):
    libro_list = Libro.objects.all()
    libro_filter = LibroFilter(request.GET, queryset=libro_list)
    return render(request,  'libro_list.html', {'filter': libro_filter})
