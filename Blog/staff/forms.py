from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
    email = forms.EmailField(label="modificar email")
    password1 = forms.CharField(label="contrasenia", widget=forms.PasswordInput)
    password1 = forms.CharField(label="repita contrasenia", widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}

