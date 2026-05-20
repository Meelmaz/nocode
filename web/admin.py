"""
admin.py - Configuración del panel de administración de Django

Registra el modelo Profile para que sea visible en el admin de Django.
"""

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Configuración del modelo Profile en el admin."""
    list_display = ['user', 'created_at']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['created_at']
