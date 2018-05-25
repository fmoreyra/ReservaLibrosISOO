from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.utils import timezone
class Categoria(models.Model):
    nombre = models.CharField(
        max_length=255,
        verbose_name=_("Nombre"))

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")


class Nacionalidad(models.Model):
    nacionalidad = models.CharField(
        max_length=255,
        verbose_name=_("Nacionalidad"))

    def __str__(self):
        return self.nacionalidad

    class Meta:
        verbose_name = _("Nacionalidad")
        verbose_name_plural = _("Nacionalidades")


class Autor(models.Model):
    apellido = models.CharField(
        max_length=255,
        verbose_name=_('Apellido'))
    nombre = models.CharField(
        max_length=255,
        verbose_name=_('Nombre'))
    nacionalidad = models.ForeignKey(
        Nacionalidad,
        verbose_name=_("Nacionalidad"),
        on_delete=models.CASCADE
        )

    @property
    def nombre_completo(self):
        return "{0}, {1}".format(
            self.apellido.upper(),
            self.nombre)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")


class Libro(models.Model):
    isbn = models.CharField(
        max_length=255,
        verbose_name=_("ISBN"),
        unique=True,
        null=True,
        blank=True)
    titulo = models.CharField(
        max_length=255,
        verbose_name=_("Título"))
    edicion = models.PositiveSmallIntegerField(
        verbose_name=_("Edición"))
    autor = models.ForeignKey(
        Autor,
        verbose_name=_("Autor"),
        on_delete=models.CASCADE)
    categoria = models.ForeignKey(
        Categoria,
        verbose_name=_("Categoría"),
        on_delete=models.CASCADE)
    resumen = models.TextField(
        max_length=2000,
        verbose_name=_("Resumen"),
        null=True,
        blank=True)
    disponibilidad = models.BooleanField(
        default=True)

    def __str__(self):
        return self.isbn + ', ' + self.titulo + ', ' + str(self.edicion) + '° edición'

    class Meta:
        verbose_name = _("Libro")
        verbose_name_plural = _("Libros")


class Reserva(models.Model):
    usuario = models.ForeignKey(
        User,
        verbose_name=_("Usuario"),
        on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro,
        verbose_name=_("Libro"),
        on_delete=models.CASCADE)
    fecha_despacho = models.DateField()
    fecha_devolucion = models.DateField(
        default= timezone.now
    )
    devuelto = models.NullBooleanField(
        null=True,
        default=False)
    entregado = models.NullBooleanField(
        null=True,
        default=False)

    def __str__(self):
        return self.usuario.profile.__str__() + '; ' + self.libro.__str__()

    class Meta:
        verbose_name = _("Reserva")
        verbose_name_plural = _("Reservas")
