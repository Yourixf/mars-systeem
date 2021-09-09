from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(reqeust):
    return HttpResponse("<h1> dit is de home pagina </h1>")
