from django.http import HttpResponse
from .forms import MoviesForm, UserForm, CinemaForm
from .models import Movies, Users, Cinemas
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def movies(request,name, dir, act, date):
    movie = Movies(name, dir, act, date)
    movie.save()
    return HttpResponse(F"Peli creada")

def moviesForm(request):
    if request.method == "POST":
        myform = MoviesForm(request.POST)
        if myform.is_valid:
            print(myform)
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
            print(myform)
            user_info = myform.cleaned_data
            user = Users(name=user_info["name"],surname=user_info["surname"],user_name=user_info["user_name"],password=user_info["password"],mail = user_info["mail"],birth_date = user_info["birth_date"],other_info = user_info["other_info"])
            user.save()
            return HttpResponse(F"Usuario creado")

    else:
        myform = UserForm()   
    return render (request,"usersForm.html",{"myform":myform})

def cinemaForm(request):
    if request.method == "POST":
        myform = CinemaForm(request.POST)
        if myform.is_valid:
            print(myform)
            cinema_info = myform.cleaned_data
            cinema = Cinemas(name=cinema_info["name"],address=cinema_info["address"],num_of_seats=cinema_info["num_of_seats"],mail=cinema_info["mail"], phone = cinema_info["phone"],other_info = cinema_info["other_info"])
            cinema.save()
            return HttpResponse(F"Cine creado")
    else:
        myform = CinemaForm()
        return render (request,"cinemaForm.html",{"myform":myform})


def findmovie (request):
    return render(request,"findmovie.html")

def find (request):
    if request.GET["nombre"]: 
        #return HttpResponse (request.GET['nombre'])    
        nombre = request.GET["nombre"]
        peliculas = Movies.objects.filter(name__icontains = nombre)
        return HttpResponse(peliculas)
        
    else:
         respuesta = "Cargar nombre"
         return HttpResponse (respuesta)

def index (request):
    return render(request,"index.html")

def busqueda_actores(request):
    return render(request, "busqueda_actores.html")

def buscar(request):
    if request.GET["actors"]:
        
        #mensaje= "Actor buscado: %r" %request.GET["actors"]
        actor_consulta = request.GET["actors"]
        actor_filtrado= Movies.objects.filter(act__icontains=actor_consulta)  

        return render(request, "resultados_busqueda_actor.html", {"actor":actor_filtrado, "query":actor_consulta} )
    else:
        mensaje = "Cargar nombre"

    return HttpResponse(mensaje)

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario= form.cleaned_data.get("usurname")
            contra= form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contra)
        
            if user is not None:
                login(request, user)

                return render(request, "padre.html", {"mensaje":f"Bienvenido {usuario}"} )
            else:
                return render(request, "padre.html", {"mensaje":"Error datos incorrectos"} )
        else:
            return render(request, "padre.html", {"mensaje":"Error, formulario erroneo"} )

    form= AuthenticationForm()

    return render (request, "login.html", {"form":form} ) 


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST) 

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "inicio.html", {"mensaje": f"Usuario {username} creado"})

    else:
        form= UserCreationForm()

    return render(request, "registro.html", {"form":form})    

            
    
    


