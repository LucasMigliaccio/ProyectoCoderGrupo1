from tkinter import CASCADE, Widget
from django.db import models
from stat import FILE_ATTRIBUTE_DIRECTORY
from django.forms import CharField, PasswordInput
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.

# class Users(models.Model):
#     name = models.CharField("Nombre",max_length=30)
#     surname = models.CharField("Apellido",max_length=30)
#     user_name = models.CharField("Nombre_de_usuario",unique=True,max_length=30)
#     password = models.CharField("Contraseña", max_length=30)
#     mail = models.EmailField("Email")
#     birth_date = models.DateField("Fecha_de_Nacimiento")
#     other_info = models.CharField("Otros_datos",max_length=30)
    
class Cinemas(models.Model):
    name = models.CharField("Nombre",max_length=30)
    address = models.CharField("Dirección",max_length=30)
    num_of_seats = models.IntegerField("Capacidad")
    mail = models.EmailField("Mail")
    phone = models.CharField("Telefono",max_length=20)
    other_info = models.CharField("Otros datos",max_length=30)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Cines"
        ordering = ["name"]

class Actors(models.Model):
    name = models.CharField("Nombre",max_length=30)
    surname = models.CharField("Apellido",max_length=30)
    nac = models.CharField("Nacionalidad",max_length=30)
    birth_date = models.DateField("Nacimiento")

    def __str__(self) -> str:
        return f"{self.surname}, {self.name}"

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actores"
        ordering = ["surname"]

class Directors(models.Model):
    name = models.CharField("Nombre",max_length=30)
    surname = models.CharField("Apellido",max_length=30)
    nac = models.CharField("Nacionalidad",max_length=30)
    birth_date = models.DateField("Nacimiento")

    def __str__(self) -> str:
        return f"{self.surname}, {self.name}"

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ["surname"]
    
class Movies(models.Model):
    name = models.CharField("Título",max_length=30)
    # dir = models.CharField("Director",max_length=30)
    # act = models.CharField("ActorPrincipal",max_length=30)
    date = models.DateField("Fecha de Lanzamiento")
    act = models.ManyToManyField(Actors, verbose_name="Actores")
    dir = models.ManyToManyField(Directors, verbose_name="Director")
    link = models.URLField(max_length=200, blank=True, verbose_name="Trailer")

    def __str__(self) -> str:
        year = self.date.year
        return f"{self.name} ({year})" 

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        unique_together = ["name","date",]
        ordering = ["name"]

class Blogs(models.Model):
    title = models.CharField("Título",max_length=30)
    subtitle = models.CharField("Subtítulo",max_length=60)
    body = models.TextField("Contenido",max_length=300)
    date = models.DateField("Creación")
    img = models.ImageField(verbose_name="Imagen", upload_to='img/', height_field=None, width_field=None, max_length=100, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    aprove = models.BooleanField(default="False")

    def __str__(self) -> str:
        return f"{self.title} ({self.date})" 

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Blogs"
        ordering = ["-date"]

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='avatars', null=True, blank=True)
    
    def __str__(self) -> str:
        return f"Avatar de {self.user}" 