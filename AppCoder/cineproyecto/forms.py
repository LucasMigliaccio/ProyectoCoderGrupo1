from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MoviesForm(forms.Form):

    Nombre = forms.CharField(max_length=30)
    Director = forms.CharField(max_length=30)
    Actor = forms.CharField(max_length=30)    
    Fecha = forms.DateField()

class UserForm(forms.Form):

    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    mail = forms.EmailField()
    birth_date = forms.DateField()
    other_info = forms.CharField(max_length=30)

class CinemaForm(forms.Form):
    name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
    num_of_seats = forms.IntegerField()
    mail = forms.EmailField()
    phone = forms.IntegerField()
    other_info = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label=" Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2"]
        help_texts= {k: "" for k in fields}

