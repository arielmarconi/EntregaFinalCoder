from django import forms 


class BuscarJuegoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    compania = forms.CharField(max_length=20)
    consola = forms.CharField(max_length=20)


class BuscarNombreForm(forms.Form):
    nombre = forms.CharField(max_length=30)