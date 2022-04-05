from django import views
from django.urls import path
from .views import movies, moviesForm, userForm, findmovie, find

urlpatterns = [
    path('new-movie/', movies),
    path('new-movie-form/', moviesForm, name="FormularioPelicula"),
    path('new-user-form/', userForm, name="FormularioUsuario"),
    path('findmovie/', findmovie, name="BusquedaPelicula"),
    path('find/',find),
]