from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from login.models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('get_legajo', 'username', 'email', 'get_nombre', 'get_apellido','get_documento', 'get_carrera', 'is_staff')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def get_legajo(self, instance):
        return instance.profile.legajo
    get_legajo.short_description = 'Legajo'

    def get_apellido(self, instance):
        return instance.profile.apellido
    get_apellido.short_description = 'Apellido'

    def get_nombre(self, instance):
        return instance.profile.nombre
    get_nombre.short_description = 'Nombre'

    def get_documento(self, instance):
        return instance.profile.documento
    get_documento.short_description = 'Documento'

    def get_carrera(self, instance):
        return instance.profile.carrera
    get_carrera.short_description = 'Carrera'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
