import uuid
from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from login.choices import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    legajo = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Legajo'),
        blank=True)
    apellido = models.CharField(
        max_length=255,
        verbose_name=_('Apellido'))
    nombre = models.CharField(
        max_length=255,
        verbose_name=_('Nombre'))
    documento = models.CharField(
        max_length=255,
        verbose_name=_('Número de documento'),
        unique=True,
        blank=True)
    fecha_nacimiento = models.DateField(
        verbose_name=_('Fecha de Nacimiento'),
        blank=True,
        null=True)
    carrera = models. CharField(
        max_length=255,
        choices=CARRERA,
        default=CARRERA[0][0],
        verbose_name=_("Carrera")
    )

    @property
    def nombre_completo(self):
        return "{0}, {1}".format(
            self.apellido.upper(),
            self.nombre)

    @property
    def edad(self):
        delta = (date.today() - self.fecha_nacimiento)
        return int(delta.days / 365.2425)

    def __str__(self):
        return "{0}, {1} {2}, {3}".format(
            self.legajo,
            self.nombre,
            self.apellido,
            self.carrera)

    def save(self, *args,**kwargs):
        self.validate_unique()
        super(Profile,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfiles")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
