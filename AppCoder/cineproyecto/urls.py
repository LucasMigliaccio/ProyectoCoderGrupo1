from re import template
from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from .views import busqueda_actores, buscar, register, edit_user, BlogsCreation, DetailMovies, UpdateMovies, DeleteMovie, CreationmovieForm, Allmovieslist, Allcinemalist, creationcinemaForm, findcinemaget, findmovieget, index, seekercinema, seekermovie 
 
urlpatterns = [
    path('',index, name="Inicio"),
    #path('all-movies-list/', allmovieslist, name = 'Movieslist'),
    path('all-movies-list/', Allmovieslist.as_view(), name = 'Movieslist'),
    path('all-cinema-list/', Allcinemalist.as_view(), name="Cinemalist"),
    #path('creation-movie-form/', creationmoviesForm, name='Peliculas'),
    path(r'^nuevo$', CreationmovieForm.as_view(), name='Peliculas'),
    path('movie-delete/<pk>', DeleteMovie.as_view(), name = "Borrar"),
    path('movie-update/<pk>', UpdateMovies.as_view(), name = "Edit"),
    path('movie-detail/<pk>', DetailMovies.as_view(), name = "Detalles"),
    #path('creation-user-form/', creationuserForm, name="FormularioUsuario"),
    path('creation-cinema-form/',creationcinemaForm, name="FormularioCine"),
    path('creation-blog', BlogsCreation.as_view(),name="CrearBlog"),
    path('seeker-movie/', seekermovie, name="BusquedaPelicula"),
    path('seeker-cinema/', seekercinema, name="Findcinema"),
    path('busqueda_actores/', busqueda_actores, name= 'BusquedaActores'),
    path('find-movie-get/', findmovieget, name = 'Find'),
    path('find-cinema-get/',findcinemaget, name="Findcinema_request"),
    path('buscar/', buscar),
    path('login/', LoginView.as_view(template_name= "login.html"), name= 'login'),
    path('logout/', LogoutView.as_view(template_name= "logout.html"), name= 'logout'),
    path('register/', register, name = 'Register'),
    path('edit_user/', edit_user, name = 'EditUser'),
    #path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout")  
]