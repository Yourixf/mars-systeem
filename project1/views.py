from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Medewerkers


def index(reqeust):
    return HttpResponse("<h1>dit home pagina</h1>")


def a(reqeust):
    alle_medewerkers = Medewerkers.objects.all()
    return render(reqeust, 'project1/index.html', {'alle_medewerkers': alle_medewerkers})







