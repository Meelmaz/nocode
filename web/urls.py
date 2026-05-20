"""
urls.py - URLs de la aplicación web

Define las rutas URL de la aplicación:
- / → Landing page
- /login/ → Inicio de sesión
- /register/ → Registro
- /logout/ → Cerrar sesión
- /dashboard/ → Panel privado
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),           # Página de inicio
    path('login/', views.login_view, name='login'),     # Login
    path('register/', views.register_view, name='register'),  # Registro
    path('logout/', views.logout_view, name='logout'),  # Cerrar sesión
    path('dashboard/', views.dashboard, name='dashboard'),  # Panel privado
]
