from django.shortcuts import render
from django.http import HttpResponse

def default(request):
    return HttpResponse("<h1>Witaj w mojej aplikacji</h1>")
