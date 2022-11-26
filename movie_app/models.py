from django.db import models

# Create your models here.


class Movies(models.Model):
    movieid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actors(models.Model):
    actorid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Directors(models.Model):
    directorid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name
