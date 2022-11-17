from django.contrib import admin
from movie_app.models import Movies, Directors, Actors

admin.site.register(Movies)
admin.site.register(Directors)
admin.site.register(Actors)
# Register your models here.
