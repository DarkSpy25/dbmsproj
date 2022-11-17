from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
user = {}


def home(request):
    return render(request, 'home.html')


def first(request):
    return render(request, 'first.html')


def login(request):
    return render(request, 'login.html')
