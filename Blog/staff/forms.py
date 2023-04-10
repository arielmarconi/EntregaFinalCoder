from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.utils import timezone
# from django.db import models
# from django.contrib.auth import get_user_model
# User = get_user_model()


class BuscarJuegoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    compania = forms.CharField(max_length=20)
    consola = forms.CharField(max_length=20)


class BuscarNombreForm(forms.Form):
    nombre = forms.CharField(max_length=30)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomUserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Repita contrasenia", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}

