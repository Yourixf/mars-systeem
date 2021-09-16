from django.shortcuts import render, get_object_or_404
from .models import Medewerkers



def index(reqeust):
    return render(reqeust, 'project1/index.html', )

def medewerkers(reqeust):
    alle_medewerkers = Medewerkers.objects.all()
    return render(reqeust, 'project1/medewerkers.html',{'alle_medewerkers': alle_medewerkers,})

def detail_medewerkers(reqeust, medewerkers_id):
    medewerkers = get_object_or_404(Medewerkers, pk=medewerkers_id)
    return render(reqeust, 'project1/detail.html', {'medewerkers': medewerkers,})

def login(reqeust):
    return render(reqeust, 'project1/login.html', )






