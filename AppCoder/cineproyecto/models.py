from django.db import models
from stat import FILE_ATTRIBUTE_DIRECTORY
from django.forms import CharField

# Create your models here.

class Movies(models.Model):
    name = models.CharField("Título",max_length=30)
    dir = models.CharField("Director",max_length=30)
    act = models.CharField("ActorPrincipal",max_length=30)
    date = models.DateField("FechaLanzamiento")
