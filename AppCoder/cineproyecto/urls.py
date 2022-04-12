from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import movies, moviesForm, register, userForm, findmovie, find,cinemaForm, index, busqueda_actores, buscar, login_request

urlpatterns = [
    path('',index, name="Inicio"),
    path('new-movie/', movies),
    path('new-movie-form/', moviesForm, name='Peliculas'),
    path('new-user-form/', userForm, name="FormularioUsuario"),
    path('new-cinema-form/',cinemaForm, name="FormularioCine"),
    path('findmovie/', findmovie, name="BusquedaPelicula"),
    path('find/',find),
    path('buscar_actores/', busqueda_actores, name= 'BusquedaActor'),
    path('buscar/', buscar),
    path('login/', login_request, name= 'Login'),
    path('register/', register, name = 'Register'),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    

    
]