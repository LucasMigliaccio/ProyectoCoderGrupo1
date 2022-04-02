from django.http import HttpResponse

from .forms import MoviesForm
from .models import Movies
from django.shortcuts import render


# Create your views here.

def movies(request,name, dir, act, date):
    movie = Movies(name, dir, act, date)
    movie.save()
    return HttpResponse(F"Peli creada")

def moviesForm(request):
    if request.method == "POST":

        myform = MoviesForm(request.POST)

        print(myform)

        if myform.is_valid:

            movie_info = myform.cleaned_data
            movie = Movies (name=movie_info["name"],dir=movie_info["dir"],act=movie_info["act"],date=movie_info["date"])
            movie.save()

            return HttpResponse(F"Peli creada")

    else:

        myform = MoviesForm()

    return render (request,"moviesForm.html",{"myform":myform})

   # return HttpResponse(F"Peli creada formulario")