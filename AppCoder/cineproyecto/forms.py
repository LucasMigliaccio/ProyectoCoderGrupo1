from mailbox import Mailbox
from tkinter.tix import Select
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Movies, Actors, Directors

class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ["name","act","dir","date","link"]

class ActorsForm(forms.ModelForm):
    class Meta:
        model = Actors
        fields = ["name","surname","nac","birth_date"]

class DirectorsForm(forms.ModelForm):
    class Meta:
        model = Directors
        fields = ["name","surname","nac","birth_date"]
                  
# -- Eliminamos Form User -- 
# class UserForm(forms.Form):

#     Nombre = forms.CharField(max_length=30)
#     Apellido = forms.CharField(max_length=30)
#     Usuario = forms.CharField(max_length=30)
#     Contraseña = forms.CharField(widget=forms.PasswordInput)
#     Mail = forms.EmailField()
#     Cumpleaños = forms.DateField()
#     Informacion = forms.CharField(max_length=30)

class CinemaForm(forms.Form):
    Nombre = forms.CharField(max_length=30)
    Direccion = forms.CharField(max_length=30)
    Asientos = forms.IntegerField()
    Mail= forms.EmailField()
    Telefono = forms.IntegerField()
    Informacion = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label=" Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2"]
        help_texts= {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    img = forms.ImageField(label="Avatar")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields = ["email", "password1", "password2"]
        help_texts= {k: "" for k in fields}