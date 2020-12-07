from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def default(request):
    return HttpResponse("<h1>Witaj w mojej aplikacji</h1>")