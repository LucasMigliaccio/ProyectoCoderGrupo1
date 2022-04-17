from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import allcinemalist, allmovieslist, creationcinemaForm, creationmoviesForm, creationuserForm, findcinemaget, findmovieget, index, seekercinema, seekermovie 

urlpatterns = [
    path('',index, name="Inicio"),
    path('all-movies-list/', allmovieslist, name = 'Movieslist'),
    path('all-cinema-list/', allcinemalist, name="Cinemalist"),
    path('creation-movie-form/', creationmoviesForm, name='Peliculas'),
    path('creation-user-form/', creationuserForm, name="FormularioUsuario"),
    path('creation-cinema-form/',creationcinemaForm, name="FormularioCine"),
    path('seeker-movie/', seekermovie, name="BusquedaPelicula"),
    path('seeker-cinema/', seekercinema, name="Findcinema"),
    path('find-movie-get/', findmovieget, name = 'Find'),
    path('find-cinema-get/',findcinemaget, name="Findcinema_request"),
    #path('buscar_actores/', busqueda_actores, name= 'BusquedaActor'),
    #path('buscar/', buscar),
    #path('login/', login_request, name= 'Login'),
    #path('register/', register, name = 'Register'),
    #path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout")  
]