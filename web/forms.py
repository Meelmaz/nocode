"""
forms.py - Formularios de la aplicación web

Define los formularios de Login y Registro con validaciones personalizadas.
Utiliza los formularios de autenticación de Django como base.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """
    Formulario de inicio de sesión personalizado.
    Hereda de AuthenticationForm de Django para mantener la seguridad.
    """
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
            'id': 'login-username',
            'autocomplete': 'username',
        }),
        label='Usuario'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'login-password',
            'autocomplete': 'current-password',
        }),
        label='Contraseña'
    )


class RegisterForm(UserCreationForm):
    """
    Formulario de registro de usuarios personalizado.
    Hereda de UserCreationForm para incluir validaciones de contraseña.
    Añade campo de email obligatorio.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com',
            'id': 'register-email',
            'autocomplete': 'email',
        }),
        label='Correo electrónico'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario',
                'id': 'register-username',
                'autocomplete': 'username',
            }),
        }
        labels = {
            'username': 'Usuario',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar widgets de contraseñas
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'register-password1',
            'autocomplete': 'new-password',
        })
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'id': 'register-password2',
            'autocomplete': 'new-password',
        })
        self.fields['password2'].label = 'Confirmar contraseña'

    def clean_email(self):
        """Validar que el email no esté ya registrado."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
