from django.urls import path
from .views import movies, moviesForm

urlpatterns = [
    path('new-movie/', movies),
    path('new-movie-form/', moviesForm, name="FormularioPelicula"),
]