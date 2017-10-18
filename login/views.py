from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from login.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            import pdb
            pdb.set_trace()
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
