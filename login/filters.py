from django.contrib.auth.models import User
from login.models import Profile
from reserva.models import Libro
import django_filters

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['user__username', 'user__email', 'legajo']

class LibroFilter(django_filters.FilterSet):
    class Meta:
        model = Libro
        fields = ['isbn', 'titulo', 'categoria__nombre', 'disponibilidad']
