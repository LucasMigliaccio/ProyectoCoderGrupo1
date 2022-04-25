from datetime import date
from mailbox import Mailbox
from tkinter import Widget
from tkinter.tix import Select
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Movies, Actors, Directors

class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ("name","act","dir","date","link")
        widgets = {
            'date': forms.DateInput(
                attrs={
                    "type":"date"
                }
            )
        }

class ActorsForm(forms.ModelForm):
    class Meta:
        model = Actors
        fields = ["name","surname","nac","birth_date"]
        widgets = {
                'birth_date': forms.DateInput(
                    attrs={
                        "type":"date"
                    }
                )
            }
    def clean_name(self):
        name = self.cleaned_data["name"]
        if(name[0] != name[0].upper()):
            return name.capitalize()
        else:
            return name
    def clean_surname(self):
        surname = self.cleaned_data["surname"]
        if(surname[0] != surname[0].upper()):
            return surname.capitalize()
        else:
            return surname

class DirectorsForm(forms.ModelForm):
    class Meta:
        model = Directors
        fields = ["name","surname","nac","birth_date"]
        widgets = {
                'birth_date': forms.DateInput(
                    attrs={
                        "type":"date"
                    }
                )
            }
    def clean_name(self):
        name = self.cleaned_data["name"]
        if(name[0] != name[0].upper()):
            return name.capitalize()
        else:
            return name
    def clean_surname(self):
        surname = self.cleaned_data["surname"]
        if(surname[0] != surname[0].upper()):
            return surname.capitalize()
        else:
            return surname
                  
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

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if(first_name[0] != first_name[0].upper()):
            return first_name.capitalize()
        else:
            return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if(last_name[0] != last_name[0].upper()):
            return last_name.capitalize()
        else:
            return last_name
    

    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2","first_name","last_name"]
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