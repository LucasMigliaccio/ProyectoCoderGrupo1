from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import DetailMovies, UpdateMovies, DeleteMovie, CreationmovieForm, Allmovieslist, Allcinemalist, creationcinemaForm, creationuserForm, findcinemaget, findmovieget, index, seekercinema, seekermovie 

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
    path('creation-user-form/', creationuserForm, name="FormularioUsuario"),
    path('creation-cinema-form/',creationcinemaForm, name="FormularioCine"),
    path('seeker-movie/', seekermovie, name="BusquedaPelicula"),
    path('seeker-cinema/', seekercinema, name="Findcinema"),
    path('find-movie-get/', findmovieget, name = 'Find'),
    path('find-cinema-get/',findcinemaget, name="Findcinema_request"),
    #path('delete-movie/', deletemovie, name="Eliminar"), BORRAR
    #path('buscar_actores/', busqueda_actores, name= 'BusquedaActor'),
    #path('buscar/', buscar),
    #path('login/', login_request, name= 'Login'),
    #path('register/', register, name = 'Register'),
    #path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout")  
]