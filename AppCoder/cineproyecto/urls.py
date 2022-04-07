from django import views
from django.urls import path
from .views import movies, moviesForm, userForm, findmovie, find,cinemaForm, index

urlpatterns = [
    path('',index, name="Inicio"),
    path('new-movie/', movies),
    path('new-movie-form/', moviesForm, name='Peliculas'),
    path('new-user-form/', userForm, name="FormularioUsuario"),
    path('new-cinema-form/',cinemaForm, name="FormularioCine"),
    path('findmovie/', findmovie, name="BusquedaPelicula"),
    path('find/',find),
    
]