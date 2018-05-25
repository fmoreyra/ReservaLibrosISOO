from django.contrib import admin
from reserva.models import *
admin.site.disable_action('delete_selected')

admin.site.register(Categoria)
admin.site.register(Nacionalidad)
admin.site.register(Autor)
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = [
        'isbn',
        'titulo',
        'autor',
        'categoria',
        'disponibilidad']
    search_fields = [
        'isbn',
        'titulo',
        'autor__nombre',
        'autor__apellido',
        'categoria__nombre',
        'disponibilidad']


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = [
        'usuario',
        'libro',
        'fecha_despacho',
        'fecha_devolucion',
        'entregado',
        'devuelto']
    search_fields = [
        'usuario__profile__nombre',
        'usuario__profile__apellido',
        'usuario__profile__documento',
        'usuario__profile__legajo',
        'usuario__profile__carrera',
        'libro__isbn',
        'libro__titulo',
        'libro__autor__nombre',
        'libro__autor__apellido',
        'libro__categoria__nombre',
        'libro__autor__nombre',
        'libro__disponibilidad',]
    actions = ['marcar_como_devuelto','marcar_como_entregado']

    def marcar_como_devuelto(self, request, queryset):
        for e in queryset.all(): e.libro.disponibilidad='True';e.libro.save()
        queryset.update(devuelto=True)

    def marcar_como_entregado(self, request, queryset):
        for e in queryset.all(): e.entregado='True';e.save()
        queryset.update(entregado=True)
