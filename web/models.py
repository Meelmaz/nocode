"""
models.py - Modelos de la aplicación web

Define el modelo Profile para extender la información del usuario de Django.
Se utiliza una señal (signal) para crear automáticamente un perfil
cuando se registra un nuevo usuario.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Modelo que extiende el usuario de Django con campos adicionales.
    Se relaciona con User mediante OneToOneField.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True, default='', verbose_name='Biografía')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f'Perfil de {self.user.username}'


# ==========================================
# Señales para crear perfil automáticamente
# ==========================================

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Crea un perfil automáticamente cuando se crea un nuevo usuario."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Guarda el perfil cuando se guarda el usuario."""
    instance.profile.save()
