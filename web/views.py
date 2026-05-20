"""
views.py - Vistas de la aplicación web

Define todas las vistas del proyecto:
- landing: Página de inicio pública
- login_view: Inicio de sesión
- register_view: Registro de usuarios
- logout_view: Cerrar sesión
- dashboard: Panel privado (requiere login)
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm


def landing(request):
    """
    Vista de la página de inicio (landing page).
    Si el usuario ya está autenticado, redirige al dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')


def login_view(request):
    """
    Vista de inicio de sesión.
    Procesa el formulario de login y autentica al usuario.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register_view(request):
    """
    Vista de registro de usuarios.
    Crea un nuevo usuario y lo autentica automáticamente.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Cuenta creada exitosamente! Bienvenido, {user.username}.')
            return redirect('dashboard')
        else:
            # Mostrar errores del formulario
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    """
    Vista de cierre de sesión.
    Cierra la sesión del usuario y redirige al inicio.
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('landing')


@login_required
def dashboard(request):
    """
    Vista del panel privado (dashboard).
    Requiere que el usuario esté autenticado (@login_required).
    Muestra todo el contenido educativo sobre IA y Redes Neuronales.
    """
    return render(request, 'dashboard.html')
