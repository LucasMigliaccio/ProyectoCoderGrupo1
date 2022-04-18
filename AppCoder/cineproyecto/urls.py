from re import template
from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from .views import allcinemalist, allmovieslist, creationcinemaForm, creationmoviesForm, creationuserForm, findcinemaget, findmovieget, index, seekercinema, seekermovie, buscar, busqueda_actores,register

urlpatterns = [
    path('',index, name="Inicio"),
    path('all-movies-list/', allmovieslist, name = 'Movieslist'),
    path('all-cinema-list/', allcinemalist, name="Cinemalist"),
    path('creation-movie-form/', creationmoviesForm, name='Peliculas'),
    path('creation-user-form/', creationuserForm, name="FormularioUsuario"),
    path('creation-cinema-form/',creationcinemaForm, name="FormularioCine"),
    path('seeker-movie/', seekermovie, name="BusquedaPelicula"),
    path('seeker-cinema/', seekercinema, name="Findcinema"),
    path('busqueda_actores/', busqueda_actores, name= 'BusquedaActores'),
    path('find-movie-get/', findmovieget, name = 'Find'),
    path('find-cinema-get/',findcinemaget, name="Findcinema_request"),
    path('buscar/', buscar),
    path('login/', LoginView.as_view(template_name= "login.html"), name= 'login'),
    path('logout/', LogoutView.as_view(template_name= "logout.html"), name= 'logout'),
    path('register/', register, name = 'Register'),
    #path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout")  
]