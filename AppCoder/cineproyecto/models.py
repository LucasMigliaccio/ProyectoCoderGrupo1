from tkinter import Widget
from django.db import models
from stat import FILE_ATTRIBUTE_DIRECTORY
from django.forms import CharField, PasswordInput
# Create your models here.


class Users(models.Model):
    name = models.CharField("Nombre",max_length=30)
    surname = models.CharField("Apellido",max_length=30)
    user_name = models.CharField("Nombre_de_usuario",unique=True,max_length=30)
    password = models.CharField("Contraseña", max_length=30)
    mail = models.EmailField("Email")
    birth_date = models.DateField("Fecha_de_Nacimiento")
    other_info = models.CharField("Otros_datos",max_length=30)
    
class Cinemas(models.Model):
    name = models.CharField("Nombre",max_length=30)
    address = models.CharField("Dirección",max_length=30)
    num_of_seats = models.IntegerField("Capacidad")
    mail = models.EmailField("Mail")
    phone = models.CharField("Telefono",max_length=20)
    other_info = models.CharField("Otros datos",max_length=30)

class Actors(models.Model):
    name = models.CharField("Nombre",max_length=30)
    surname = models.CharField("Apellido",max_length=30)
    nac = models.CharField("Nacionalidad",max_length=30)
    birth_date = models.DateField("Nacimiento")

    def __str__(self) -> str:
        return f"{self.surname}, {self.name}"

class Directors(models.Model):
    name = models.CharField("Nombre",max_length=30)
    surname = models.CharField("Apellido",max_length=30)
    nac = models.CharField("Nacionalidad",max_length=30)
    birth_date = models.DateField("Nacimiento")

    def __str__(self) -> str:
        return f"{self.surname}, {self.name}"
    
class Movies(models.Model):
    name = models.CharField("Título",max_length=30)
    dir = models.CharField("Director",max_length=30)
    act = models.CharField("ActorPrincipal",max_length=30)
    date = models.DateField("FechaLanzamiento")
    actor = models.ManyToManyField(Actors)
    director = models.ManyToManyField(Directors)

    def __str__(self) -> str:
        return f"{self.name}-{self.dir}" 


