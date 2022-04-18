from mailbox import Mailbox
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MoviesForm(forms.Form):

    Nombre = forms.CharField(max_length=30)
    Director = forms.CharField(max_length=30)
    Actor = forms.CharField(max_length=30)    
    Fecha = forms.DateField()

class UserForm(forms.Form):

    Nombre = forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)
    Usuario = forms.CharField(max_length=30)
    Contraseña = forms.CharField(widget=forms.PasswordInput)
    Mail = forms.EmailField()
    Cumpleaños = forms.DateField()
    Informacion = forms.CharField(max_length=30)

class CinemaForm(forms.Form):
    Nombre = forms.CharField(max_length=30)
    Direccion = forms.CharField(max_length=30)
    Asientos = forms.IntegerField()
    Mail= forms.EmailField()
    Telefono = forms.IntegerField()
    Informacion = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label=" Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2"]
        help_texts= {k: "" for k in fields}

