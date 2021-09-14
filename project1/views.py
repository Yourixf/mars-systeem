from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Medewerkers

def index(reqeust):
    return render(reqeust, 'project1/index.html', )

#def medewerkers(reqeust):
#    all_medewerkers = Medewerkers.objects.all()
#    html = ""
#    for medewerker in all_medewerkers:
#        url = str(medewerker.id) + '/'
#        html += '<a href="' + url + '">' + medewerker.voornaam + '</a><br>'
#       return HttpResponse(html)

def medewerkers(reqeust):
    alle_medewerkers = Medewerkers.objects.all()
    return render(reqeust, 'project1/medewerkers.html',{'alle_medewerkers': alle_medewerkers,})

def detail_medewerkers(reqeust, medewerkers_id):
    try:
        medewerkers = Medewerkers.objects.get(pk= medewerkers_id)
    except Medewerkers.DoesNotExist:
        raise Http404("Medewerker bestaat niet meer.")
    return render(reqeust, 'project1/detail.html', {'medewerkers': medewerkers,})




#def a(reqeust):
##    try:
#        all_medewerkers = Medewerkers.objects.all()
#        medewerkers = Medewerkers.objects.get(pk= medewerkers_id)
#    except Medewerkers.DoesNotExist:
#        raise Http404("medewerker bestaat niet")
#    return render(reqeust, 'project1/index.html', {'medewerkers': medewerkers})

def login(reqeust):
    return render(reqeust, 'project1/login.html', )






