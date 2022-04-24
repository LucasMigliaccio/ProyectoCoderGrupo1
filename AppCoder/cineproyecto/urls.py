from re import template
from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

#IMPORTADOR DE PATH PARA IMAGENES
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------------

from .views import DeleteDirectors, DetailDirectors, UpdateDirectors, DeleteDirectors, CreationDirectorForm, about, CreationActorForm, DeleteActors, UpdateActors, DetailActors, Alldirectorslist, Allactorslist, Allbloglist, busqueda_actores, buscar, register, edit_user, BlogsCreation, DetailMovies, UpdateMovies, DeleteMovie, CreationmovieForm, Allmovieslist, Allcinemalist, creationcinemaForm, findcinemaget, findmovieget, index, seekercinema, seekermovie 
 
urlpatterns = [
    path('',index, name="Inicio"),
    #path('all-movies-list/', allmovieslist, name = 'Movieslist'),
    path('all-movies-list/', Allmovieslist.as_view(), name = 'Movieslist'),
    path('all-actors-list/', Allactorslist.as_view(), name = 'Actorslist'),
    path('all-director-list/', Alldirectorslist.as_view(), name = 'Directorslist'),
    path('all-cinema-list/', Allcinemalist.as_view(), name="Cinemalist"),
    path('pages/', Allbloglist.as_view(), name="AllPages"),
    # path('all-blog-recent/', last_3_blogs, name="RecentBlogs"),
    #path('creation-movie-form/', creationmoviesForm, name='Peliculas'),
    path('movies', CreationmovieForm.as_view(), name='Peliculas'),
    path('movie-delete/<pk>', DeleteMovie.as_view(), name = "Borrar"),
    path('movie-update/<pk>', UpdateMovies.as_view(), name = "Edit"),
    path('movie-detail/<pk>', DetailMovies.as_view(), name = "Detalles"),
    path('actors', CreationActorForm.as_view(), name='Actores'),
    path('actor-delete/<pk>', DeleteActors.as_view(), name = "BorrarAct"),
    path('actor-update/<pk>', UpdateActors.as_view(), name = "EditAct"),
    path('actor-detail/<pk>', DetailActors.as_view(), name = "DetallesAct"),
    path('directors', CreationDirectorForm.as_view(), name='Directores'),
    path('director-delete/<pk>', DeleteDirectors.as_view(), name = "BorrarDir"),
    path('director-update/<pk>', UpdateDirectors.as_view(), name = "EditDir"),
    path('director-detail/<pk>', DetailDirectors.as_view(), name = "DetallesDir"),
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
     path('about/', about, name = 'About'),
    #path("logout/", LogoutView.as_view(template_name="logout.html"), name="Logout")  
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)