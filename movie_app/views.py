from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
user = {}


def home(request):
    return render(request, 'home.html')


def first(request):
    render(request, 'first.html')
    user = request.POST
    print(list(user)[1])
    if (list(user)[1] == 'admin'):
        return render(request, 'login.html')
    else:
        return render(request, 'home.html')
