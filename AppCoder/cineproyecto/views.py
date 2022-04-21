from django.http import HttpResponse
from .forms import MoviesForm, CinemaForm, UserRegisterForm, UserEditForm
from .models import Blogs, Movies, Cinemas
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin


# Create your views here.

# INICIO --
def index (request):
    return render(request,"index.html")

#Movies (ViewList / Seek / )

def allmovieslist (request):
    movies = Movies.objects.all().order_by('name')
    return render(request,"all-movies-list.html",{'movies':movies})

def seekermovie (request):
    return render(request,"seeker-movie.html")

def findmovieget (request):
    if request.GET["nombre"]: 
        name = request.GET["nombre"]
        movies = Movies.objects.filter(name__icontains = name).order_by('name')
        return render(request, "result-movie.html",{"movies": movies})   
    else:
         return render(request,"find-movie-get-else.html")

def creationmoviesForm(request):
    if request.method == "POST":
        myform = MoviesForm(request.POST)
        if myform.is_valid:
            print(myform)
            movie_info = myform.cleaned_data        
            movie = Movies (name=movie_info["Nombre"],dir=movie_info["Director"],act=movie_info["Actor"],date=movie_info["Fecha"])
            movie.save()
            return render(request,"success-movie-created.html")
    else:
        myform = MoviesForm()
    return render (request,"creation-movies-form.html",{"myform":myform})
#Cinemas

def allcinemalist (request):
    cinemas = Cinemas.objects.all().order_by('name')
    return render(request,"all-cinemas-list.html",{'cinemas':cinemas})

def seekercinema (request):
    return render(request,"seeker-cinema.html")

def findcinemaget (request):
    if request.GET["nombre"]: 
        name = request.GET["nombre"]
        cinemas = Cinemas.objects.filter(name__icontains = name).order_by('name')
        return render(request, "result-cinema.html",{"cinemas": cinemas})
        
    else:
         return render(request,"find-cinema-get-else.html")

def creationcinemaForm(request):
    if request.method == "POST":
        myform = CinemaForm(request.POST)
        if myform.is_valid:
            print(myform)
            cinema_info = myform.cleaned_data
            cinema = Cinemas(name=cinema_info["Nombre"],address=cinema_info["Direccion"],num_of_seats=cinema_info["Asientos"],mail=cinema_info["Mail"], phone = cinema_info["Telefono"],other_info = cinema_info["Informacion"])
            cinema.save()
            return render(request,"success-cinema-created.html")
    else:
        myform = CinemaForm()
        return render (request,"creation-cinema-form.html",{"myform":myform})

#Estrellas
def busqueda_actores(request):
    return render(request, "busqueda_actores.html")

def buscar(request):
    if request.GET["actors"]:
        #mensaje= "Actor buscado: %r" %request.GET["actors"]
        actors = request.GET["actors"]
        actor_filtrado= Movies.objects.filter(act__icontains=actors)  
        #return HttpResponse (actor_filtrado)
        return render(request, "resultados_busqueda_actor.html", {"actor_filtrado":actor_filtrado, "query":actors} )
    else:
        mensaje = "Cargar nombre"

    return HttpResponse(mensaje)

#Blogs

class BlogsCreation(CreateView):
    model = Blogs
    template_name = "creation-blogs-form.html"
    success_url = reverse_lazy("Inicio")
    fields = ["title","subtitle","body","date","author"]

      
def register(request):
    if request.method == "POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Usuario {username} creado")
            return ("Inicio")
    else:
        form= UserRegisterForm()

    context= {"form":form}
    return render(request, "register.html", context)

class Allmovieslist (ListView):
    model = Movies
    template_name = "all-movies-list.html"
    
    def get_queryset(self):
        return Movies.objects.order_by('name')


class CreationmovieForm(CreateView):
    model = Movies
    template_name = "creation-movies-form.html"
    success_url = "/cineproyecto/all-movies-list"
    fields = ['name','dir','act','date']


class DeleteMovie(DeleteView, LoginRequiredMixin):
    model = Movies
    template_name = 'confirm-delete-movies.html'
    success_url = "/cineproyecto/all-movies-list"


class UpdateMovies(UpdateView):
    model = Movies
    template_name = "update-movies.html"
    success_url = "/cineproyecto/all-movies-list"
    fields = ['name','dir','act','date']

class DetailMovies(DetailView):
    model = Movies
    template_name = "detail-movie.html"


class Allcinemalist (ListView):
    model = Cinemas
    template_name = "all-cinemas-list.html"
    
    def get_queryset(self):
         return Cinemas.objects.order_by('name')

@login_required
def edit_user(request):
    usuario = request.user
    if request.method == "POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.save()

            username = form.cleaned_data["username"]
            messages.success(request, f"Usuario {username} modificado")
            return redirect("Inicio")

    else:
        form = UserEditForm(initial={"email": usuario.email})
    
    return render(request,"edit-users-form.html",{"form":form, "user":usuario})

        













#     if request.method == "POST":
#         form = UserCreationForm(request.POST) 
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             form.save()
#             return render(request, "inicio.html", {"mensaje": f"Usuario {username} creado"})
#     else:
#         form= UserCreationForm()
#     return render(request, "registro.html", {"form":form})


# --- ELIMINAMOS VIEW PARA CREACION DE USER YA QUE USAMOS LA DE DJANGO ---
# def creationuserForm(request):
#     if request.method == "POST":
#         myform = UserForm(request.POST)
#         if myform.is_valid:
#             print(myform)
#             user_info = myform.cleaned_data
#             user = Users(name=user_info["Nombre"],surname=user_info["Apellido"],user_name=user_info["Usuario"],password=user_info["Contraseña"],mail = user_info["Mail"],birth_date = user_info["Cumpleaños"],other_info = user_info["Informacion"])
#             user.save()
#             return render(request,"success-user-created.html")

#     else:
#         myform = UserForm()   
#     return render (request,"creation-users-form.html",{"myform":myform})
    
# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():
#             usuario= form.cleaned_data.get("usurname")
#             contra= form.cleaned_data.get("password")
            
#             user = authenticate(username=usuario, password=contra)
        
#             if user is not None:
#                 login(request, user)

#                 return render(request, "padre.html", {"mensaje":f"Bienvenido {usuario}"} )
#             else:
#                 return render(request, "padre.html", {"mensaje":"Error datos incorrectos"} )
#         else:
#             return render(request, "padre.html", {"mensaje":"Error, formulario erroneo"} )

#     form= AuthenticationForm()

#     return render (request, "login.html", {"form":form} ) 
    


