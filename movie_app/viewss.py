from django.shortcuts import render, redirect
from django.http import HttpResponse
from movie_app.models import Movies
from django.db import connection, connections

# Create your views here.
user = {}


def index(request):
    if request.method == "POST":
        try:
            genres = request.POST.get('genre')
            cursor = connections['default'].cursor()
            movies = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM movie_app_movies where genre= %s", [genres])
                movies = cursor.fetchall()
            return render(request, 'index.html', {'movies': movies})
        except:
            movie = None
            movies = Movies.objects.get()
            return render(request, 'index.html', {'movies': movies})
    else:
        movies = Movies.objects.all()
        return render(request, 'index.html', {'movies': movies})


def first(request):
    return render(request, 'first.html')


def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('pass')
        if (name == 'admin' and password == 'admin'):
            return redirect("/insert_movies")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def insert_movies(request):
    if request.method == "POST":
        name = request.POST.get("name")
        movieid = request.POST.get("id")
        director = request.POST.get("director")
        actor = request.POST.get("actor")
        genre = request.POST.get("genre")
        language = request.POST.get("lang")
        cursor = connections['default'].cursor()
        cursor.execute("INSERT INTO movie_app_movies(movieid,name,language,genre,director,actor) VALUES( %s, %s, %s, %s, %s, %s )", [
                       movieid, name, language, genre, director, actor])
        with connection.cursor() as cursor:
            cursor.execute("select * from movie_app_movies")
            movies = cursor.fetchall()
            return render(request, 'insert_movies.html', {'movies': movies})
    else:
        movies = Movies.objects.all()
        return render(request, 'insert_movies.html', {'movies': movies})


def delete_movies(request):
    if request.method == "POST":
        try:
            movie_id = request.POST.get('id')
            cursor = connections['default'].cursor()
            cursor.execute(
                "DELETE from movie_app_movies where movieid=%s", [movie_id])
            movies = Movies.objects.all()
            return render(request, 'delete_movies.html', {'movies': movies})

        except:
            movie = None
            movies = Movies.objects.all()
            return render(request, 'delete_movies.html', {'movies': movies})
    else:
        movies = Movies.objects.all()
        return render(request, 'delete_movies.html', {'movies': movies})
