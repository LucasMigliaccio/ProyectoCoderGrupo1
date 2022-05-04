from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.http import HttpResponse, Http404, JsonResponse
from .forms import ActorForm, MoviesForm, CinemaForm, UserRegisterForm, UserEditForm, DirectorsForm, ThreadForm, MessageForm
from .models import Blogs, Movies, Cinemas, Actors, Directors, Avatar, MessageModel, ThreadModel
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin, UserPassesTestMixin
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib import messages
# Create your views here.

# Vista para traer Avatar y llevarlo a página de Index (líneas de tal a tal)
#
#

def index(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request,"index.html",{"avatar":avatar})
    else:
        return render(request,"index.html")

#
#
#

# Vista para renderizar sección "about us" (lineas de tal a tal)
#
#
def about (request):
    return render(request,"about-us.html")

#
#
#

# Clases y funciones de management de modelo Movies: listado, creación, actualización, detalles, busqueda
#
#

class Allmovieslist (ListView):
    model = Movies
    template_name = "all-movies-list.html"
    
    def get_queryset(self):
        return Movies.objects.order_by('name')

class CreationmovieForm(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Movies
    template_name = "creation-movies-form.html"
    permission_required = 'cineproyecto.add_movies'
    success_url = "/cineproyecto/all-movies-list"
    form_class = MoviesForm

class DeleteMovie(LoginRequiredMixin, PermissionRequiredMixin, DeleteView ):
    model = Movies
    permission_required = 'cineproyecto.delete_movies'
    template_name = 'confirm-delete-movies.html'
    success_url = "/cineproyecto/all-movies-list"

class UpdateMovies(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Movies
    permission_required = 'cineproyecto.change_movies'
    template_name = "update-movies.html"
    success_url = "/cineproyecto/all-movies-list"
    form_class = MoviesForm

class DetailMovies(LoginRequiredMixin, DetailView):
    model = Movies
    template_name = "detail-movie.html"

def seekermovie (request):
    return render(request,"seeker-movie.html")

def findmovieget (request):
    if request.GET["nombre"]: 
        name = request.GET["nombre"]
        movies = Movies.objects.filter(name__icontains = name).order_by('name')
        return render(request, "result-movie.html",{"movies": movies, "nombre": name})   
    else:
         return render(request,"find-movie-get-else.html")

#
#
# Fin CRUD y búsqueda modelo Movies

# Clases y funciones de management de modelo Actors: listado, creación, actualización, detalles, busqueda
#
#

class Allactorslist (ListView):
    model = Actors
    template_name = "all-actors-list.html"
    
    def get_queryset(self):
        return Actors.objects.order_by('surname')

class CreationActorForm(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Actors
    template_name = "creation-actors-form.html"
    permission_required = 'cineproyecto.add_actors'
    success_url = "/cineproyecto/all-actors-list"
    form_class = ActorForm

class DeleteActors (LoginRequiredMixin, PermissionRequiredMixin, DeleteView ):
    model = Actors
    permission_required = 'cineproyecto.delete_actors'
    template_name = 'confirm-delete-actors.html'
    success_url = "/cineproyecto/all-actors-list"

class UpdateActors (LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Actors
    permission_required = 'cineproyecto.change_actors'
    template_name = "update-actors.html"
    success_url = "/cineproyecto/all-actors-list"
    form_class = ActorForm

class DetailActors(LoginRequiredMixin, DetailView):
    model = Actors
    template_name = "detail-actor.html"

def seekeractor(request):
    return render(request, "seeker-actor.html")

def findactorget(request):
    if request.GET["name"]:
        name = request.GET["name"]
        actors= Actors.objects.filter(name__icontains=name).order_by('name') | Actors.objects.filter(surname__icontains=name).order_by('name') | Actors.objects.filter(nac__icontains=name).order_by('name')
        
        print(actors)  
        return render(request, "result-actor.html", {"actors":actors, "name":name} )
    else:
        mensaje = "Cargar nombre"

    return render(request,"find-actor-get-else.html")

#
#
# Fin CRUD y búsqueda modelo Actors

# Clases y funciones de management de modelo Directors: listado, creación, actualización, detalles, busqueda
# 
#
  
class Alldirectorslist (ListView):
    model = Directors
    template_name = "all-directors-list.html"

class CreationDirectorForm(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Directors
    template_name = "creation-directors-form.html"
    permission_required = 'cineproyecto.add_directors'
    success_url = "/cineproyecto/all-director-list"
    form_class = DirectorsForm

class DeleteDirectors (LoginRequiredMixin, PermissionRequiredMixin, DeleteView ):
    model = Directors
    permission_required = 'cineproyecto.delete_directors'
    template_name = 'confirm-delete-directors.html'
    success_url = "/cineproyecto/all-director-list"

class UpdateDirectors (LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Directors
    permission_required = 'cineproyecto.change_directors'
    template_name = "update-directors.html"
    success_url = "/cineproyecto/all-director-list"
    form_class = DirectorsForm

class DetailDirectors(LoginRequiredMixin, DetailView):
    model = Directors
    template_name = "detail-director.html"
    
    def get_queryset(self):
        return Directors.objects.order_by('surname')

def seekerdirector(request):
    return render(request, "seeker-director.html")

def finddirectorget(request):
    if request.GET["name"]:
        name = request.GET["name"]
        director= Directors.objects.filter(name__icontains=name).order_by('name') | Directors.objects.filter(surname__icontains=name).order_by('name') | Directors.objects.filter(nac__icontains=name).order_by('name')
                 
        return render(request, "result-director.html", {"directors":director, "name":name} )
    else:
        return render(request,"find-actor-get-else.html")

#
#
# Fin CRUD y búsqueda modelo Directors

# Clases y funciones de management de modelo Cinemas: listado, creación, actualización, detalles, busqueda
#
#

class Allcinemalist (ListView):
    model = Cinemas
    template_name = "all-cinemas-list.html"
    
    def get_queryset(self):
         return Cinemas.objects.order_by('name')

class CreationCinemasForm(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Cinemas
    template_name = "creation-cinemas-form.html"
    permission_required = 'cineproyecto.add_cinemas'
    success_url = "/cineproyecto/all-cinema-list"
    form_class = CinemaForm

class DeleteCinemas(LoginRequiredMixin, PermissionRequiredMixin, DeleteView ):
    model = Cinemas
    permission_required = 'cineproyecto.delete_cinemas'
    template_name = 'confirm-delete-cinema.html'
    success_url = "/cineproyecto/all-cinema-list"
    
class UpdateCinemas(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Cinemas
    permission_required = 'cineproyecto.change_cinemas'
    template_name = "update-cinemas.html"
    success_url = "/cineproyecto/all-cinema-list"
    form_class = CinemaForm

class DetailCinemas(LoginRequiredMixin, DetailView):
    model = Cinemas
    template_name = "detail-cinema.html"

def seekercinema (request):
    return render(request,"seeker-cinema.html")

def findcinemaget (request):
    if request.GET["nombre"]: 
        name = request.GET["nombre"]
        cinemas = Cinemas.objects.filter(name__icontains = name).order_by('name')
        return render(request, "result-cinema.html",{"cinemas": cinemas, "nombre":name})
        
    else:
         return render(request,"find-cinema-get-else.html")

#
#
# Fin CRUD y búsqueda modelo Cinemas

# Clases y funciones de management de modelo Blogs: listado, creación, aprobación, actualización, detalles, busqueda
#
#

class Allbloglist (ListView):
    model = Blogs
    template_name = "all-blogs-list.html"
    
    def get_queryset(self):
        return Blogs.objects.order_by('date')

    def get_context_data(self,**kwargs):
        context = super(Allbloglist,self).get_context_data(**kwargs)
        context['lastblogs'] = Blogs.objects.filter(aprove=True).order_by("-date")[:3]
        return context

class BlogsDetail (DetailView):
    model= Blogs
    template_name = "detail-blog.html"

class BlogsCreation(LoginRequiredMixin, CreateView):
    model = Blogs
    template_name = "creation-blogs-form.html"
    success_url = reverse_lazy("Inicio")
    fields = ["title","subtitle","body","img"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date = datetime.now() 
        return super(BlogsCreation, self).form_valid(form)

class BlogsAprove(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blogs
    template_name = "update-blogs.html"
    permission_required = 'cineproyecto.change_blogs'
    success_url = reverse_lazy("Inicio")
    fields = ["title","subtitle","body","aprove"]

@staff_member_required
def aproveblog(request):
    toaprove = Blogs.objects.filter(aprove=False).order_by("-date")
    return render (request, "all-blogs-toaprove.html", {"blog_toaprove":toaprove})
  
class BlogsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView ):
    model = Blogs
    permission_required = 'cineproyecto.delete_blogs'
    template_name = 'confirm-delete-blogs.html'
    success_url = "/cineproyecto/pages"

#
#
# Fin funciones de creación y gestión de Blogs


# Función para registro de usuarios      
def register(request):
    if request.method == "POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            form.save()

            avatar = Avatar(user= User.objects.get(username=username), picture = "avatars\250.jpg")
            avatar.save()
            return render (request,"index.html")
        else:
            print("FALLO EL FORM IS VALID")
    else:
        form= UserRegisterForm()

    context= {"form":form}
    return render(request, "register.html", context)


#Función para edición de usuarios (debe estar logueado)
@login_required
def edit_user(request):
    usuario = request.user
    if request.method == "POST":
        form= UserEditForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.save()
            avatar = Avatar.objects.get(user=usuario)
            avatar.delete()
            avatar2 = Avatar(user= usuario , picture = data["img"])
            avatar2.save()
            messages.success(request, f"Usuario {usuario} modificado")
            return redirect("Inicio")

    else:
        form = UserEditForm(initial={"email": usuario.email, "first_name":usuario.first_name, "last_name":usuario.last_name})
    
    return render(request,"edit-users-form.html",{"form":form, "user":usuario})

class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        users = User.objects.all()
        context = {
            'threads': threads,
            'users': users
        }

        return render(request, 'inbox.html', context)


# Views destinadas a la creación y gestión de mensajería

class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()
        users = User.objects.all()
        context = {
            'form': form,
            'users':users
        }

        return render(request, 'create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('thread', pk=thread.pk)
        except:
            return redirect('create-thread')

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }

        return render(request, 'thread.html', context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')
        )

        message.save()
        return redirect('thread', pk=pk)

#
#
# Fin views destinadas a gestión de mensajería


