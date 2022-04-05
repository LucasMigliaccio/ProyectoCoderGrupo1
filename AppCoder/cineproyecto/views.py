from django.http import HttpResponse

from .forms import MoviesForm, UserForm
from .models import Movies, Users
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
            movie = Movies (name=movie_info["Nombre"],dir=movie_info["Director"],act=movie_info["Actor"],date=movie_info["Fecha"])
            movie.save()
            return HttpResponse(F"Pelicula creada")
    else:
        myform = MoviesForm()
    return render (request,"moviesForm.html",{"myform":myform})

def userForm(request):
    if request.method == "POST":
        myform = UserForm(request.POST)
        if myform.is_valid:
            user_info = myform.cleaned_data
            user = Users(name=user_info["Nombre"],surname=user_info["Apellido"],user_name=user_info["Nombre de Usuario"],password=user_info["Contraseña"],mail = user_info["Email"],birth_date = user_info["Fecha de nacimiento"],other_info = user_info["Otros datos"])
            user.save()
            return HttpResponse(F"Usuario creado")
    else:
        myform = UserForm()   
    return render (request,"usersForm.html",{"myform":myform})

def findmovie (request):
    return render(request,"findmovie.html")

def find (request):
    if request.GET["nombre"]: 
        #return HttpResponse (request.GET['nombre'])    
        nombre = request.GET["nombre"]
        peliculas = Movies.objects.filter(name__icontains = nombre)
        return HttpResponse(peliculas)
        #return render(request,"searchresponse.html",{"Título": peliculas})

    else:
         respuesta = "Cargar nombre"
         return HttpResponse (respuesta)