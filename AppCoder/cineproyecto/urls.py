from re import template
from django import views
from django.urls import path, re_path
from django.contrib.auth.views import LogoutView, LoginView

#IMPORTADOR DE PATH PARA IMAGENES
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------------

from .views import CreateMessage, CreateThread, ListThreads, ThreadView, aproveblog, finddirectorget, BlogsDelete, BlogsAprove, BlogsDetail, DeleteDirectors, DetailDirectors, UpdateDirectors, DeleteDirectors, CreationDirectorForm, about, CreationActorForm, DeleteActors, UpdateActors, DetailActors, Alldirectorslist, Allactorslist, Allbloglist, register, edit_user, BlogsCreation, DetailMovies, UpdateMovies, DeleteMovie, CreationmovieForm, Allmovieslist, Allcinemalist, findcinemaget, findmovieget, index, seekercinema, seekermovie, findactorget, seekeractor, CreationCinemasForm, DeleteCinemas, UpdateCinemas, DetailCinemas, seekerdirector

UUID_CANAL_REGEX= r'channel/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'

urlpatterns = [
    #URL de inicio
    path('',index, name="Inicio"),
    #URL destinadas a mostrar listados de modelos (listviews)
    path('all-movies-list/', Allmovieslist.as_view(), name = 'Movieslist'),
    path('all-actors-list/', Allactorslist.as_view(), name = 'Actorslist'),
    path('all-director-list/', Alldirectorslist.as_view(), name = 'Directorslist'),
    path('all-cinema-list/', Allcinemalist.as_view(), name="Cinemalist"),
    path('pages/', Allbloglist.as_view(), name="AllPages"),   
    #URLs CRUD Movies
    path('movies', CreationmovieForm.as_view(), name='Movies'),
    path('movie-delete/<pk>', DeleteMovie.as_view(), name = "MovieDelete"),
    path('movie-update/<pk>', UpdateMovies.as_view(), name = "MovieEdit"),
    path('movie-detail/<pk>', DetailMovies.as_view(), name = "MovieDetail"),
    #URLs CRUD Actors
    path('actors', CreationActorForm.as_view(), name='Actors'),
    path('actor-delete/<pk>', DeleteActors.as_view(), name = "ActorDelete"),
    path('actor-update/<pk>', UpdateActors.as_view(), name = "ActorEdit"),
    path('actor-detail/<pk>', DetailActors.as_view(), name = "ActorDetail"),
    #URLs CRUD Directors
    path('directors', CreationDirectorForm.as_view(), name='Directors'),
    path('director-delete/<pk>', DeleteDirectors.as_view(), name = "DirectorDelete"),
    path('director-update/<pk>', UpdateDirectors.as_view(), name = "DirectorEdit"),
    path('director-detail/<pk>', DetailDirectors.as_view(), name = "DirectorDetail"),
    #URLs CRUD Blogs
    path('creation-blog', BlogsCreation.as_view(),name="BlogCreation"),
    path('detail-blog/<pk>', BlogsDetail.as_view(),name="BlogDetail"),
    path('delete-blog/<pk>', BlogsDelete.as_view(),name="BlogDelete"),
    path('update-blog/<pk>', BlogsAprove.as_view(),name="BlogEdit"),
    path('aprove-blog', aproveblog, name="AproveBlog"),
    #URLs CRUD Cinemas
    path('cinemas/', CreationCinemasForm.as_view(), name='Cinemas'),
    path('cinemas-delete/<pk>', DeleteCinemas.as_view(), name = "CinemaDelete"),
    path('cinemas-update/<pk>', UpdateCinemas.as_view(), name = "CinemaEdit"),
    path('cinemas-detail/<pk>', DetailCinemas.as_view(), name = "CinemaDetail"),
    #URLs destinadas a la búsqueda de modelos
    path('seeker-movie/', seekermovie, name="FindMovie"),
    path('seeker-cinema/', seekercinema, name="FindCinema"),
    path('seeker-actor/', seekeractor, name='FindActor'),
    path('seeker-director/', seekerdirector, name='FindDirector'),
    path('find-actor-get/', findactorget),
    path('find-movie-get/', findmovieget),
    path('find-cinema-get/',findcinemaget),
    path('find-director-get/', finddirectorget),
    #URLs destiandas a management de usuarios
    path('login/', LoginView.as_view(template_name= "login.html"), name= 'login'),
    path('logout/', LogoutView.as_view(template_name= "logout.html"), name= 'logout'),
    path('register/', register, name = 'Register'),
    path('edit_user/', edit_user, name = 'EditUser'),
    
    #URLs miscelaneas
    path('about/', about, name = 'About'),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
      
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)