from django.contrib import admin

from .models import *
# Register your models here.

class CinemaAdmin(admin.ModelAdmin):
    list_display = ["name","address"]
    search_fields = ["name"]

class MovieAdmin(admin.ModelAdmin):
    search_fields = ["name","date"]
    filter_horizontal = ["act","dir"]
        
class PersonAdmin(admin.ModelAdmin):
    search_fields = ["name","surname"]
    list_display = ["nac","birth_date"]

class BlogAdmin (admin.ModelAdmin):
    search_fields = ["title","author"]
    list_display = ["title","date","author","aprove"]

class AvatarAdmin (admin.ModelAdmin):
    search_fields = ["user"]
    list_display = ["user"]
    

admin.site.register(Movies, MovieAdmin)
admin.site.register(Cinemas, CinemaAdmin)
admin.site.register(Actors, PersonAdmin)
admin.site.register(Directors, PersonAdmin)
admin.site.register(Blogs, BlogAdmin)
admin.site.register(Avatar, AvatarAdmin)

