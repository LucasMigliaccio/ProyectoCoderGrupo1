from datetime import date
from mailbox import Mailbox
from tkinter import Widget
from tkinter.tix import Select
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Movies, Actors, Directors, Cinemas

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

class ActorForm(forms.ModelForm):
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

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinemas
        fields = ("name","address","num_of_seats","mail","phone","other_info")
        widgets = {
            'date': forms.DateInput(
                attrs={
                    "type":"date"
                }
            )
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label=" Repetir Contraseña", widget=forms.PasswordInput) 

    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2","first_name","last_name"]
        help_texts= {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    img = forms.ImageField(label="Avatar")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    class Meta:
        model= User
        fields = ["email", "password1", "password2","first_name","last_name"]
        help_texts= {k: "" for k in fields}

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)