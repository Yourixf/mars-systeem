import os
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import first
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from mysite import settings
from project1 import forms
from datetime import *
from .forms import FotoForm, MedewerkersForm, ContractenToevoegenForm, EindklantenForm, \
    BrokersForm, CertificatenToevoegenForm, AanbiedingenForm, AanbiedingUpdatenForm, \
    OpdrachtenForm, OpdrachtenToevoegenForm, CvUploadForm, DocumentenUploadForm, FeedbackUploadForm, TaskItemCreateForm, \
    TaskItemUpdateForm, VestigingplaatsForm, ContactpersoonForm, ContactVestigingForm
from .models import Medewerkers, Contracten, Certificaten, Eindklanten, Brokers, Aanbiedingen, \
    Opdrachten, Opmerkingen, Vestigingplaats, Contactpersonen,  STATUS_OPDRACHT_CHOICES

# De views.py kan je functies wegschrijven voor in de templates. Hier voor kan je dingen importen die staan bovenaan de template. (dingen vanuit Django en vanuit andere templates zoals Forms, Models enzov).
# @login_required(login_url='login') is een ingebouwde Django functie ter beveiliging als de "User" niet is ingelogd kan die niet op die pagina komen.

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'url']


# Voor de CV's, Feedbackdocumenten en overige documenten zijn dit de formats waarin het mag geupload worden.
@login_required(login_url='login')
def ContactpersoonDetailPage(request, pk):
    contactpersoon = Contactpersonen.objects.get(id=pk)
    vestiging_lijst = Vestigingplaats.objects.filter(Q(contactpersoon_id=contactpersoon))

    context = {
        'contactpersoon': contactpersoon,
        'vestiging_lijst': vestiging_lijst,
    }
    return render(request, 'contactpersoon.detail.html', context)

@login_required(login_url='login')
def ContactVestigingDeleten(request, pk):
    vorige_pagina = request.META['HTTP_REFERER']
    vestiging = Vestigingplaats.objects.get(id=pk)

    contactpersoon = vestiging.contactpersoon
    contactpersoon.vestiging_id = ''
    contactpersoon.save()

    vestiging.contactpersoon_id = ''
    vestiging.save()




    return redirect(vorige_pagina)

@login_required(login_url='login')
def ContactVestigingToevoegen(request, pk):
    vorige_pagina = request.META['HTTP_REFERER']
    test = request.META['HTTP_REFERER']

    if 'broker' in vorige_pagina:
        request.session['vorige_pagina'] = 'broker'
        contactpersoon = Contactpersonen.objects.get(id=pk)
        broker = contactpersoon.broker
        vestiging_lijst = Vestigingplaats.objects.filter(broker_id=broker)

        context = {
            'contactpersoon': contactpersoon,
            'broker': broker,
            'vestiging_lijst': vestiging_lijst,
        }
        request.session['test'] = contactpersoon.id

    elif 'klant' in vorige_pagina:
        request.session['vorige_pagina'] = 'klant'
        contactpersoon = Contactpersonen.objects.get(id=pk)
        eindklant = contactpersoon.klant
        vestiging_lijst = Vestigingplaats.objects.filter(klant_id=eindklant.id)

        context = {
            'contactpersoon':contactpersoon,
            'eindklant': eindklant,
            'vestiging_lijst': vestiging_lijst,
        }
        request.session['test'] = contactpersoon.id

    if request.method == 'POST':
        previous_page = request.session.get('vorige_pagina')
        contactpersoon_id = request.session.get('test')
        if 'broker' in previous_page:
            contactpersoon = Contactpersonen.objects.get(id=contactpersoon_id)
            contactpersoon.vestiging_id = pk
            contactpersoon.save()

            vestiging = contactpersoon.vestiging
            vestiging.contactpersoon_id = contactpersoon_id
            vestiging.save()
            return redirect('brokers')
        elif 'klant' in previous_page:
            contactpersoon = Contactpersonen.objects.get(id=contactpersoon_id)
            contactpersoon.vestiging_id = pk
            contactpersoon.save()

            vestiging = contactpersoon.vestiging
            vestiging.contactpersoon_id = contactpersoon_id
            vestiging.save()

            return redirect('eindklanten')

    else:
        return render(request, 'contact.vestiging.toevoegen.html', context)



@login_required(login_url='login')
def ContactPersonenDelete(request, pk):
    contactpersoon = Contactpersonen.objects.get(id=pk)
    contactpersoon_form = ContactpersoonForm(request.POST or None, instance=contactpersoon)

    vorige_pagina = request.META['HTTP_REFERER']

    if 'broker' in vorige_pagina:
        contactpersoon = contactpersoon_form.save()
        try:
            broker = contactpersoon.broker
            broker.contactpersoon_id = ''
            vestiging = contactpersoon.vestiging
            vestiging.contactpersoon_id = ''
            vestiging.save()
            broker.save()
        except:
            broker = ''
        contactpersoon.vestiging_id = ''
        contactpersoon.broker_id = ''
        contactpersoon.save()
        contactpersoon.delete()

        if Contactpersonen.objects.filter(broker_id=broker).first():
            cobo = Contactpersonen.objects.filter(broker_id=broker).first()
            broker.contactpersoon_id = cobo
            broker.save()
        elif Contactpersonen.objects.filter(broker_id=broker).last():
            cobo = Contactpersonen.objects.filter(broker_id=broker).last()
            broker.contactpersoon_id = cobo
            broker.save()
        else:
            cobo = ''
            broker.contactpersoon_id = cobo
            broker.save()
        return redirect(vorige_pagina)
    elif 'klant' in vorige_pagina:
        contactpersoon = contactpersoon_form.save()
        try:
            klant = contactpersoon.klant
            vestiging = contactpersoon.vestiging

            klant.contactpersoon_id = ''
            vestiging.contactpersoon_id = ''
            vestiging.save()
            klant.save()
        except:
            klant = ''
        contactpersoon.vestiging_id = ''
        contactpersoon.klant_id = ''
        contactpersoon.save()
        contactpersoon.delete()

        if Contactpersonen.objects.filter(klant_id=klant).first():
            cobo = Contactpersonen.objects.filter(klant_id=klant).first()
            klant.contactpersoon_id = cobo
            klant.save()
        elif Contactpersonen.objects.filter(klant_id=klant).last():
            cobo = Contactpersonen.objects.filter(klant_id=klant).last()
            klant.contactpersoon_id = cobo
            klant.save()
        else:
            cobo = ''
            klant.contactpersoon_id = cobo
            klant.save()
        return redirect(vorige_pagina)


@login_required(login_url='login')
def ContactPersonenToevoegen(request, pk):
    contactpersoon_form = ContactpersoonForm()
    vorige_pagina = request.META['HTTP_REFERER']
    if 'broker' in vorige_pagina:
        request.session['vorige_pagina'] = 'broker'
        broker_pk = Brokers.objects.get(id=pk)
        context = {
            'contactpersoon_form': contactpersoon_form,
            'broker_pk': broker_pk
        }
    elif 'klant' in vorige_pagina:
        request.session['vorige_pagina'] = 'klant'
        eind_klant_pk = Eindklanten.objects.get(id=pk)
        context = {
            'contactpersoon_form': contactpersoon_form,
            'eind_klant_pk': eind_klant_pk,
        }
    if request.method == 'POST':
        previous_page = request.session.get('vorige_pagina')
        contactpersoon_form = ContactpersoonForm(request.POST, request.FILES)
        if contactpersoon_form.is_valid():
            contactpersoon = contactpersoon_form.save()
            if 'broker' in previous_page:
                contactpersoon.broker_id = pk
                broker_pk = Brokers.objects.get(id=pk)
                broker_pk.contactpersoon_id = contactpersoon
                broker_pk.save()
                contactpersoon.save()
                return redirect('brokers')
            elif 'klant' in previous_page:
                contactpersoon.klant_id = pk
                klant_pk = Eindklanten.objects.get(id=pk)
                klant_pk.contactpersoon_id = contactpersoon
                klant_pk.save()
                contactpersoon.save()
                return redirect('eindklanten')
    else:
        return render(request, 'contactpersoon.toevoegen.html', context)


@login_required(login_url='login')
def ContactPersoonUpdaten(request, pk):
    contactpersoon_pk = Contactpersonen.objects.get(id=pk)
    contactpersoon_form = ContactpersoonForm(instance=contactpersoon_pk)

    vorige_pagina = request.META['HTTP_REFERER']
    if 'broker' in vorige_pagina:
        request.session['vorige_pagina'] = 'broker'
    elif 'klant' in vorige_pagina:
        request.session['vorige_pagina'] = 'klant'

    context = {
        'contactpersoon_form': contactpersoon_form,
        'contactpersoon_pk': contactpersoon_pk,
    }

    if request.method == 'POST':
        previous_page = request.session.get('vorige_pagina')
        contactpersoon_form = ContactpersoonForm(request.POST, request.FILES, instance=contactpersoon_pk)
        if contactpersoon_form.is_valid():
            contactpersoon = contactpersoon_form.save()
            contactpersoon.save()

            if 'broker' in previous_page:
                return redirect('brokers')
            elif 'klant' in previous_page:
                return redirect('eindklanten')
    else:
        return render(request, 'update.contactpersoon.html', context)

@login_required(login_url='login')
def VestigingToevoegen(request, pk):
    vestiging_form = VestigingplaatsForm()

    vorige_pagina = request.META['HTTP_REFERER']
    volgende_pagina = request.META['PATH_INFO']


    if 'broker' in vorige_pagina:
        request.session['vorige_pagina'] = 'broker'

        if 'vestiging' in volgende_pagina:
            print('patat')


        broker_pk = Brokers.objects.get(id=pk)

        context = {
            'vestiging_form': vestiging_form,
            'broker_pk': broker_pk,

        }
    elif 'klant' in vorige_pagina:
        request.session['vorige_pagina'] = 'klant'

        eind_klant_pk = Eindklanten.objects.get(id=pk)

        context = {
            'vestiging_form': vestiging_form,
            'eind_klant_pk': eind_klant_pk,
        }

    if request.method == 'POST':
        previous_page = request.session.get('vorige_pagina')

        vestiging_form = VestigingplaatsForm(request.POST, request.FILES)
        if vestiging_form.is_valid():
            vestiging = vestiging_form.save()

            if 'broker' in previous_page:
                vestiging.broker_id = pk
                broker_pk = Brokers.objects.get(id=pk)
                broker_pk.vestiging_id = vestiging
                broker_pk.save()
                vestiging.save()
                return redirect('brokers')

            elif 'klant' in previous_page:
                vestiging.klant_id = pk
                eind_klant_pk = Eindklanten.objects.get(id=pk)
                eind_klant_pk.vestiging_id = vestiging
                eind_klant_pk.save()
                vestiging.save()
                return redirect('eindklanten')
    else:
        return render(request, 'vestiging.toevoegen.html', context)


@login_required(login_url='login')
def VestigingUpdaten(request, pk):
    vestiging_pk = Vestigingplaats.objects.get(id=pk)
    vestiging_form = VestigingplaatsForm(instance=vestiging_pk)

    vorige_pagina = request.META['HTTP_REFERER']
    if 'broker' in vorige_pagina:
        request.session['vorige_pagina'] = 'broker'
    elif 'klant' in vorige_pagina:
        request.session['vorige_pagina'] = 'klant'

    previous_pagina = request.session.get('vorige_pagina')

    context = {
        'vestiging_form': vestiging_form,
        'vestiging_pk': vestiging_pk,
    }

    if request.method == 'POST':
        vestiging_form = VestigingplaatsForm(request.POST, request.FILES, instance=vestiging_pk)
        if vestiging_form.is_valid():
            vestiging = vestiging_form.save()
            vestiging.save()
            if 'broker' in previous_pagina:
                return redirect('brokers')
            elif 'klant' in previous_pagina:
                return redirect('eindklanten')

    else:
        return render(request, 'update.vestiging.html', context)



@login_required(login_url='login')
def VestigingDeleten(request, pk):
    vestiging = Vestigingplaats.objects.get(id=pk)
    vestiging_form = VestigingplaatsForm(request.POST or None, instance=vestiging)

    vorige_pagina = request.META['HTTP_REFERER']

    if 'broker' in vorige_pagina:
        vestiging = vestiging_form.save()
        broker = vestiging.broker
        broker.vestiging_id = ''

        broker.save()
        vestiging.save()
        vestiging.delete()

        if Vestigingplaats.objects.filter(broker_id=broker).first():
            vebo = Vestigingplaats.objects.filter(broker_id=broker).first()
            broker.vestiging_id = vebo
            broker.save()
        elif Vestigingplaats.objects.filter(broker_id=broker).last():
            vebo = Vestigingplaats.objects.filter(broker_id=broker).last()
            broker.vestiging_id = vebo
            broker.save()
        else:
            vebo = ''
            broker.vestiging_id = vebo
            broker.save()
        return redirect(vorige_pagina)

    elif 'klant' in vorige_pagina:
        vestiging = vestiging_form.save()
        klant = vestiging.klant
        klant.vestiging_id = ''

        klant.save()
        vestiging.save()
        vestiging.delete()

        if Vestigingplaats.objects.filter(klant_id=klant).first():
            vebo = Vestigingplaats.objects.filter(klant_id=klant).first()
            klant.vestiging_id = vebo
            klant.save()
        elif Vestigingplaats.objects.filter(klant_id=klant).last():
            vebo = Vestigingplaats.objects.filter(klant_id=klant).last()
            klant.vestiging_id = vebo
            klant.save()
        else:
            vebo = ''
            klant.vestiging_id = vebo
            klant.save()
        return redirect(vorige_pagina)

# Dit is de "ListView" van opmerkingen in die template krijg je alle ingevoerde opmerkingen.
# in de ListView,CreateView,UpdateView, DeleteView kan je geen @login_required(login_url='login') maar inplaats daarvan doe je tussen de haakjes
# class BLABLA(LoginRequiredMixin, ListView): zoals hier onder
class OpmerkingenPageView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Opmerkingen
    template_name = 'opmerking.medewerker.html'


# Dit is de "CreateView" van de opmerkingen pagina ( de form ) voor de opmerkingen.
# success_url = '/opmerkingen/' als de opmerking is geschreven en opgeslagen is kom je op de opmerkingen pagina.

class OpmerkingSchrijvenView(LoginRequiredMixin, CreateView):
    model = Opmerkingen
    template_name = 'opmerkingen.form.html'
    form_class = TaskItemCreateForm
    success_url = '/opmerkingen/'


# Dit is de UpdateView voor de opmerkingen in de OpmerkingenUpdateView

class OpmerkingenUpdateView(LoginRequiredMixin, UpdateView):
    model = Opmerkingen
    template_name = 'update.opmerking.form.html'
    form_class = TaskItemUpdateForm
    success_url = '/opmerkingen/'


# Hier is de "DeleteView" voor de opmerkingen in de "OpmerkingenDeleteView".
class OpmerkingenDeleteView(LoginRequiredMixin, DeleteView):
    model = Opmerkingen
    template_name = 'delete.opmerking.form.html'
    success_url = "/opmerkingen/"


# Dit is de de details pagina voor de Eindklanten,     eindklant_pk = Eindklanten.objects.get(id=pk) is bedoeld om elke detail per eindklant te zien is.
#    eindklant = Eindklanten.objects.all() is bedoeld zodat je elke variabele op de details pagina kan laten zien.
@login_required(login_url='login')
def EindklantDetail(request, pk):
    eindklant_pk = Eindklanten.objects.get(id=pk)
    vestiging_lijst = Vestigingplaats.objects.filter(Q(klant_id=eindklant_pk))
    contactpersoon_lijst = Contactpersonen.objects.filter(Q(klant_id=eindklant_pk))


    # hier kijkt de code als ware of er een vestiging adres is
    try:
        # als er een vestiging adres is bij de klant dan is staat die info in 'vestiging'
        vestiging = Vestigingplaats.objects.get(klant_id=eindklant_pk)
    except:
        # als er geen vestiging adres is bij de klant dan is de 'vestiging' variable leeg
        vestiging = ''

    context = {
        'eindklant_pk': eindklant_pk,
        'vestiging': vestiging,
        'vestiging_lijst': vestiging_lijst,
        'contactpersoon_lijst': contactpersoon_lijst

    }
    return render(request, 'eindklanten.detail.html', context)


# Dit is de de details pagina voor de Brokers,     broker = Brokers.objects.get(id=pk) is bedoeld om elke detail per eindklant te zien is.
#  broker_list = Brokers.objects.all() is bedoeld zodat je elke variabele op de details pagina kan laten zien.
@login_required(login_url='login')
def BrokerDetail(request, pk):
    broker = Brokers.objects.get(id=pk)
    vestiging_lijst = Vestigingplaats.objects.filter(Q(broker_id=broker))
    contactpersoon_lijst = Contactpersonen.objects.filter(Q(broker_id=broker))


    context = {
        'broker': broker,
        'vestiging_lijst': vestiging_lijst,
        'contactpersoon_lijst': contactpersoon_lijst
    }
    return render(request, 'broker.detail.html', context)


# Dit is de de details pagina voor de Medewerkers,    medewerkers = Medewerkers.objects.get(id=pk) is bedoeld om elke detail per eindklant te zien is.
@login_required(login_url='login')
def MedewerkerDetail(request, pk):
    medewerkers = Medewerkers.objects.get(id=pk)
    context = {
        'medewerkers': medewerkers,
    }
    return render(request, 'medewerker.detail.html', context)



# Dit is de de details pagina voor de Brokers,   aanbieding = Aanbiedingen.objects.get(id=pk) is bedoeld om elke detail per eindklant te zien is.
#   aanbiedingen_list = Aanbiedingen.objects.all() is bedoeld zodat je elke variabele op de details pagina kan laten zien.
@login_required(login_url='login')
def AanbiedingenDetail(request, pk):
    aanbieding = Aanbiedingen.objects.get(id=pk)
    aanbiedingen_list = Aanbiedingen.objects.all()
    context = {
        'aanbieding': aanbieding,
        'aanbiedingen_list': aanbiedingen_list
    }
    return render(request, 'aanbieding.detail.html', context)


# Voor medewerkers heb zijn er 3 upload download opties de cv, feedback documenten en overige documenten. Deze functie's
#     form = CvUploadForm(instance=medewerker_pk) haalt de pk op van welke medewerker het bedreft en dat het alleen onder die medewerker kan geupload worden.
#  'file': request.POST.get('cv') vraagt wat voor file de cv mag wezen
# en dan de standaard save methode van Django :
#   if request.method == 'POST':
#        form = CvUploadForm(request.POST, request.FILES, instance=medewerker_pk)
#        if form.is_valid():
#            form.save()
@login_required(login_url='login')
def Cv_Upload(request, pk):
    medewerker_pk = Medewerkers.objects.get(id=pk)
    form = CvUploadForm(instance=medewerker_pk)
    context = {'form': form,
               'medewerker_pk': medewerker_pk,
               'file': request.POST.get('cv')
               }

    if request.method == 'POST':
        form = CvUploadForm(request.POST, request.FILES, instance=medewerker_pk)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'cv.upload.html', context)


# Dit is het pad dat Django volgt als een gebruiker de cv of dergelijke wilt downloaden.
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


# Voor medewerkers heb zijn er 3 upload download opties de cv, feedback documenten en overige documenten. Deze functie's
#     form = CvUploadForm(instance=medewerker_pk) haalt de pk op van welke medewerker het bedreft en dat het alleen onder die medewerker kan geupload worden.
#  'file': request.POST.get('feedback', 'title_feedback') vraagt wat voor file de feedbackdocument mag wezen
# en dan de standaard save methode van Django :
# if request.method == 'POST':
#    form = FeedbackUploadForm(request.POST, request.FILES, instance=medewerker_pk)
#    if form.is_valid():
#        form.save()
@login_required(login_url='login')
def Feedback_Upload(request, pk):
    medewerker_pk = Medewerkers.objects.get(id=pk)
    form = FeedbackUploadForm(instance=medewerker_pk)
    context = {'form': form,
               'medewerker_pk': medewerker_pk,
               'file': request.POST.get('feedback', 'title_feedback')
               }

    if request.method == 'POST':
        form = FeedbackUploadForm(request.POST, request.FILES, instance=medewerker_pk)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'feedback.upload.html', context)


# Voor medewerkers heb zijn er 3 upload download opties de cv, feedback documenten en overige documenten. Deze functie's
#     form = CvUploadForm(instance=medewerker_pk) haalt de pk op van welke medewerker het bedreft en dat het alleen onder die medewerker kan geupload worden.
#    'file': request.POST.get('documenten', 'title_documenten') vraagt wat voor file de cv mag wezen
# en dan de standaard save methode van Django :
# if request.method == 'POST':
#    form = DocumentenUploadForm(request.POST, request.FILES, instance=medewerker_pk)
#    if form.is_valid():
#    form.save()
@login_required(login_url='login')
def Documenten_Upload(request, pk):
    medewerker_pk = Medewerkers.objects.get(id=pk)
    form = DocumentenUploadForm(instance=medewerker_pk)
    context = {'form': form,
               'medewerker_pk': medewerker_pk,
               'file': request.POST.get('documenten', 'title_documenten')
               }

    if request.method == 'POST':
        form = DocumentenUploadForm(request.POST, request.FILES, instance=medewerker_pk)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'documenten.upload.html', context)


# Haalt de gegevens van de CreateUserForm uit de forms.py en met de POST method is de mode waarbij een form kan worden ingevuld.
# Met de if request.method == 'POST': checkt django of het klopt dat het een form is die wordt ingevuld.
# dan komt if form.is_valid(): form.save() is de functie dat django checkt of de form 'valid' is en dan slaat die de form op.
# daarna een succes bericht ( messages.success(request, 'account is gemaakt voor ' + user) en daarna stuurt die je terug naar de login pagina.

login_required(login_url='login')


def registerPage(request):
    form = forms.CreateUserForm()

    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account is gemaakt voor ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


# De login vraagt om een username en password, als deze overeen komen kom je in de applicatie. anders kom je terug bij de login pagina met een bericht dat het wachtwoord of username niet klopt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username', )
        password = request.POST.get('password', )

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Gebruikersnaam of wachtwoord klopt niet')

    context = {}
    return render(request, "login.html", context)


# standaard Django logout functie, die je daarna weer naar de login pagina brengt.
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


# Dit is de home pagina waar je een aantal dingen op kan zien.
#    all_aanbieding = Aanbiedingen.objects.all() is om alle variable van de aanbiedingen op te halen.
#    open_aanbied_count = Aanbiedingen.get_status_count(Aanbiedingen.status) En hier haalt die
@login_required(login_url='login')
def Index(request):
    all_aanbieding = Aanbiedingen.objects.all()
    open_aanbied_count = Aanbiedingen.get_status_count(Aanbiedingen.status)
    all_medewerkers = Medewerkers.objects.all()
    medewerkers_count = all_medewerkers.count()
    all_klanten = Eindklanten.objects.all()
    klanten_count = all_klanten.count()
    context = {
        'all_medewerkers': all_medewerkers,
        'medewerkers_count': medewerkers_count,
        'all_aanbieding': all_aanbieding,
        'open_aanbied_count': open_aanbied_count,
        'all_klanten': all_klanten,
        'klanten_count': klanten_count,
    }
    return render(request, 'index.html', context)


# Dit is de Medewerkers pagina  medewerkers = Medewerkers.objects.all() haalt allemedewerkers op.
@login_required(login_url='login')
def MedewerkersPage(request):
    medewerkers = Medewerkers.objects.filter(Q(status='1') | Q(status='2') | Q(status='3'))

    context = {
        'medewerkers': medewerkers,
    }
    return render(request, 'medewerkers.html', context)


@login_required(login_url='login')
def MedewerkersLeegloop(request):
    # medewerkers = Medewerkers.objects.all()

    medewerkers = Medewerkers.objects.filter(Q(status='3'))

    context = {
        'medewerkers': medewerkers
    }

    return render(request, 'leegloop.medewerkers.html', context)

@login_required(login_url='login')
def ArchiefMedewerkers(request):
    medewerkers = Medewerkers.objects.filter(Q(status='4'))

    context = {
        'medewerkers': medewerkers,
    }
    return render(request, 'archief.medewerkers.html', context)

@login_required(login_url='login')
def MedewerkerAanbiedingOpdrachten(request, pk):
    medewerker = Medewerkers.objects.get(id=pk)
    aanbieding_list = Aanbiedingen.objects.filter(Q(medewerker=medewerker))
    opdracht_list = Opdrachten.objects.filter(Q(aanbieding__medewerker=medewerker))

    context = {
        'aanbieding_list': aanbieding_list,
        'opdracht_list': opdracht_list,
        'medewerker':medewerker,

    }

    return render(request, 'medewerker.opdrachten.aanbiedingen.html', context)


# De Medewerkerstoevoegen form uit de Forms.py
@login_required(login_url='login')
def MedewerkersToevoegen(request):
    form = MedewerkersForm(request.POST or None)

    context = {
        'form': form
    }
    if request.method == 'POST':
        form = MedewerkersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'medewerker.toevoegen.html', context)


# De MedewerkersUpdate form uit de Forms.py
# Nieuwe update functie, pakt nu de zelfde form als toevoegen zodat het gesynchroniseerd is
@login_required(login_url='login')
def MedewerkersUpdaten(request, pk):
    medewerker = Medewerkers.objects.get(id=pk)
    form = MedewerkersForm(request.POST or None, instance=medewerker)

    if request.method == 'POST':
        form = MedewerkersForm(request.POST or None, instance=medewerker)
        # form.save() om de nieuwe data op te slaan
        if form.is_valid():
            form.save()
            return redirect('medewerkers')

    return render(request, "update.medewerker.html", {'medewerker': medewerker, 'form': form})


# De medewerkerDelete hier vraagt django om de pk van de medewerker en met de .delete functie verwijdert Django deze medewerker en geeft een succes message.

@login_required(login_url='login')
def MedewerkerDelete(request, pk):
    med = Medewerkers.objects.filter(pk=pk)
    delete_med = Medewerkers.objects.get(pk=pk)
    if request.method == "POST":
        delete_med.delete()
        messages.success(request, "Deze medewerker is verwijderd.")
        return redirect("medewerkers")
    context = {"delete_med": delete_med, "med": med}
    return render(request, "confirm.delete.html", context)


# Dit is de form voor de foto toevoegen voor de medewerkers.
# Omdat de foto gelinkt is met een medewerker haalt Django eerst de PK op van de medewerker zodat die gelinkt is aan deze medewerker.
# Met de if request.method == 'POST': checkt django of het klopt dat het een form is die wordt ingevuld.
# dan komt if form.is_valid(): form.save() is de functie dat django checkt of de form 'valid' is en dan slaat die de form op.
# Als allesd goed is gegaan gaat die naar de template van de medewerkers.
@login_required(login_url='login')
def Foto_Toevoegen(request, pk):
    medewerker_pk = Medewerkers.objects.get(id=pk)
    form = FotoForm(instance=medewerker_pk)
    context = {'form': form,
               'medewerker_pk': medewerker_pk}

    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES, instance=medewerker_pk)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'foto.medewerker.form.html', context)


# Dit is de detail pagina van de certificaten en contracten.
@login_required(login_url='login')
def Contractendetail(request, pk):
    contracten = Contracten.objects.get(id=pk)
    certificaten = Certificaten.objects.get(id=pk)
    context = {
        'contracten': contracten,
        'certificaten': certificaten,
    }
    return render(request, 'contracten.detail.html', context, )


# hier Voeg je een Contract toe aan een medewerker     medewerker_pk = Medewerkers.objects.get(id=pk) haalt de medewerker op zodat die gelinkt is met het contract.
# deze ContractenToevoegenForm is de form die gebruit wordt uit de forms.py
@login_required(login_url='login')
def ContractenToevoegen(request, pk):
    medewerker_pk = Medewerkers.objects.get(id=pk)
    contract = Contracten.objects.filter(medewerkers_id=pk)
    form = ContractenToevoegenForm()
    context = {
        'form': form,
        'contract': contract,
    }
    if request.method == 'POST':
        form = ContractenToevoegenForm(request.POST, request.FILES, instance=medewerker_pk)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'contracten.toevoegen.html', context)


# Dit is de delete functie vand de lease auto's
# De .delete is de django functie waardoor het contract verwijderd wordt.
@login_required(login_url='login')
def ContractenDelete(request, id):
    delete_contract = Contracten.objects.get(id=id)
    delete_contract.delete()
    return redirect('contracten.detail')


# De updateview voor de contracten.
class ContractenUpdate(LoginRequiredMixin, UpdateView):
    model = Contracten
    fields = '__all__'
    template_name = 'update.contracten.html'
    success_url = reverse_lazy('contracten.detail')


# De is de overzicht pagina van de Eindklanten     eindklanten_list = Eindklanten.objects.all() haalt alle gegevens op uit de Eindklanten model.
@login_required(login_url='login')
def EindklantenPage(request):
    eindklanten_list = Eindklanten.objects.all()

    eindklant_pk = Eindklanten.objects.filter()

    vestiging = Vestigingplaats.objects.filter(klant_id=eindklant_pk)

    context = {
        'eindklanten_list': eindklanten_list,
        'vestiging': vestiging,
        'eindklant_pk': eindklant_pk,
    }

    return render(request, 'eindklanten.html', context)


# De eindklant toevoegen form EindklantenToevoegenForm uit de forms.py
@login_required(login_url='login')
def EindklantToevoegen(request):
    klant_form = EindklantenForm(request.POST or None)

    context = {
        'klant_form': klant_form,
    }

    if request.method == 'POST' and 'vestigingtoevoegen' in request.POST:
        if klant_form.is_valid():
            klant = klant_form.save()
            klant.save()

            return redirect('vestiging_toevoegen', klant.pk)

    elif request.method == 'POST' and 'vestigingtoevoegen' not in request:
        klant_form = EindklantenForm(request.POST, request.FILES)

        if klant_form.is_valid():
            klant = klant_form.save()
            klant.save()
            return redirect('eindklanten')
    else:
        return render(request, 'eindklant.toevoegen.html', context)


# De updateview voor de Eindklanten.

@login_required(login_url='login')
def EindklantenUpdaten(request, pk):
    eindklant = Eindklanten.objects.get(id=pk)
    eindklant_form = EindklantenForm(request.POST or None, instance=eindklant)
    # eindklanten = Eindklanten.objects.get(id=pk)
    context = {
        'eindklant': eindklant,
        'eindklant_form': eindklant_form,
    }
    if request.method == 'POST':
        form = EindklantenForm(request.POST or None, instance=eindklant)
        if form.is_valid():
            form.save()
            return redirect('eindklanten')
    return render(request, "update.eindklant.html", context)


# De Delete functie voor de eindklanten.
@login_required(login_url='login')
def EindklantDelete(request, id):
    delete_eindklant = Eindklanten.objects.get(id=id)
    delete_eindklant.delete()
    return redirect('eindklanten')


# De overzicht pagina van de Brokers   brokers_list = Brokers.objects.all() haalt alle gegevens op uit de Brokers model.
@login_required(login_url='login')
def BrokersPage(request):
    brokers_list = Brokers.objects.all()
    return render(request, 'brokers.html', {'brokers_list': brokers_list, })


# De Brokers toevoegen form BrokersToevoegenForm uit de forms.py
@login_required(login_url='login')
def BrokersToevoegen(request):
    form = BrokersForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = BrokersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brokers')
    else:
        return render(request, 'brokers.toevoegen.html', context)


# De Delete functie voor de Broker.
@login_required(login_url='login')
def BrokerDelete(request, id):
    delete_broker = Brokers.objects.get(id=id)
    delete_broker.delete()
    return redirect('brokers')


# De updateview voor de Brokers.

@login_required(login_url='login')
def BrokerUpdaten(request, pk):
    broker = Brokers.objects.get(id=pk)
    form = BrokersForm(request.POST or None, instance=broker)

    if request.method == 'POST':
        form = BrokersForm(request.POST or None, instance=broker)
        if form.is_valid():
            form.save()
            return redirect('brokers')

    return render(request, "update.broker.html", {'broker': broker, 'form': form})


# De Certificaten toevoegen form CertificatenToevoegenForm uit de forms.py
@login_required(login_url='login')
def CertificatenToevoegen(request, pk):
    medewerker_pk = Medewerkers.objects.get(id=pk)
    certificaat = Certificaten.objects.filter(medewerkers_id=pk)
    form = CertificatenToevoegenForm(instance=medewerker_pk)
    context = {
        'form': form,
        'certificaat': certificaat,
    }
    if request.method == 'POST':
        form = CertificatenToevoegenForm(request.POST, request.FILES, instance=medewerker_pk)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'certificaten.toevoegen.html', context)


# De aanbiedingen toevoegen form AanbiedingenToevoegenForm uit de forms.py
@login_required(login_url='login')
def AanbiedingToevoegen(request):
    aanbieding_form = AanbiedingenForm(request.POST or None)
    context = {
        'aanbieding_form': aanbieding_form
    }
    if request.method == 'POST':
        aanbieding_form = AanbiedingenForm(request.POST, request.FILES)
        # NO VALID FUNCTIE INDOUWEN
        if aanbieding_form.is_valid():
            aanbieding = aanbieding_form.save(commit=False)
            aanbieding_status = aanbieding.status

            medewerker = aanbieding.medewerker
            if aanbieding_status == '1':
                medewerker.status = '3'
                medewerker.save()
            elif aanbieding_status == '2':
                medewerker.status = '1'
                medewerker.save()
            elif aanbieding_status == '3':
                medewerker.status = '2'
                medewerker.save()
            elif aanbieding_status == '4':
                medewerker.status = '3'
                medewerker.save()
            elif aanbieding_status == '5':
                medewerker.status = '2'
                medewerker.save()

                if Opdrachten.objects.filter(aanbieding=aanbieding).exists():
                    return redirect('aanbiedingen')
                else:
                    return redirect('toevoegen_opdracht', aanbieding.pk)
                aanbieding.save()
            elif aanbieding_status == '6':
                medewerker.status = '3'
                medewerker.save()
            else:
                aanbieding.save()
            aanbieding.save()
            return redirect('aanbiedingen')
    else:
        return render(request, 'aanbiedingen.toevoegen.html', context)


# De Delete functie voor de Aanbiedingen.
@login_required(login_url='login')
def AanbiedingDelete(request, pk):
    aanbieding = Aanbiedingen.objects.get(id=pk)

    try:
        opdracht = Opdrachten.objects.get(aanbieding_id=aanbieding)
        #opdracht.aanbieding_id = ''
        opdracht.delete()

    except:
        opdracht = ''
    aanbieding.delete()
    return redirect('aanbiedingen')


# De updateview voor de UpdateView.

@login_required(login_url='login')
def AanbiedingUpdaten(request, pk):
    aanbieding = Aanbiedingen.objects.get(id=pk)
    aanbieding_form = AanbiedingUpdatenForm(request.POST or None, instance=aanbieding)


    if Opdrachten.objects.filter(aanbieding=aanbieding).exists():
        pizza=''
    else:
        if aanbieding.status == '5':
            aanbieding.status = '1'


            aanbieding.save()

    context = {
        'aanbieding': aanbieding,
        'aanbieding_form': aanbieding_form,
    }

    if request.method == 'POST':
        #aanbieding_form = AanbiedingUpdatenForm(request.POST or None, instance=aanbieding)
        if aanbieding_form.is_valid():
            aanbieding = aanbieding_form.save()
            aanbieding_status = aanbieding.status
            medewerker = aanbieding.medewerker
            if aanbieding_status == '1':
                medewerker.status = '3'
                medewerker.save()
            elif aanbieding_status == '2':
                medewerker.status = '1'
                medewerker.save()
            elif aanbieding_status == '3':
                medewerker.status = '2'
                medewerker.save()
            elif aanbieding_status == '4':
                medewerker.status = '3'
                medewerker.save()
            elif aanbieding_status == '5':
                medewerker.status = '2'
                medewerker.save()
                if Opdrachten.objects.filter(aanbieding=aanbieding).exists():
                    return redirect('aanbiedingen')
                else:
                    aanbieding.save()
                    return redirect('toevoegen_opdracht', aanbieding.pk)
            elif aanbieding_status == '6':
                medewerker.status = '3'
                medewerker.save()
            else:
                aanbieding_form.save()
            return redirect('aanbiedingen')
    return render(request, "aanbieding.update.html", context)


# Dit is de openstaande aanbiedingen deze zijn gefilterd op status Open, Geselecteerd, of Intake. Dan komen ze bij mee open aanbiedingen te staan op deze pagina.
#    aanbieding_list = Aanbiedingen.objects.filter(Q(status=1) | Q(status=2) | Q(status=3)) dit is de filter for de 3 statussen waardoor ze op deze pagina komen.
@login_required(login_url='login')
def AanbiedingenPage(request):
    aanbieding_list = Aanbiedingen.objects.filter(Q(status=1) | Q(status=2))

    context = {
        'aanbieding_list': aanbieding_list,

    }
    return render(request, 'aanbiedingen.html', context)


# Dit is de gearchiefeerde aanbiedingen deze zijn gefilterd op status Afgewezen of Geplaatst. Dan komen ze bij mee archief aanbiedingen te staan op deze pagina.
#     aanbieding_list = Aanbiedingen.objects.filter(Q(status=4) | Q(status=5)) dit is de filter for de overige 2 statussen waardoor ze op deze pagina komen.
@login_required(login_url='login')
def ArchiefAanbiedingenPage(request):
    aanbieding_list = Aanbiedingen.objects.filter(Q(status=4) | Q(status=6))
    context = {
        'aanbieding_list': aanbieding_list,

    }
    return render(request, 'aanbiedingen.archief.html', context)


@login_required(login_url='login')
def AanbiedingMetOpdracht(request):
    aanbieding_list = Aanbiedingen.objects.filter(Q(status=3) | Q(status=5))
    aanbieding_list.all()
    context = {
        'aanbieding_list': aanbieding_list,
    }

    return render(request, 'aanbiedingen.met.opdracht.html', context)


@login_required(login_url='login')
def OpdrachtToevoegen(request, pk):
    aanbieding = Aanbiedingen.objects.get(id=pk)
    aanbieding_tarief = aanbieding.tarief
    aanbieding_betaal_korting = aanbieding.betaalkorting

    opdracht_form = OpdrachtenToevoegenForm(initial={'tarief_opdracht': aanbieding_tarief, 'opdracht_betaalkorting': aanbieding_betaal_korting})

    context = {
        'opdracht_form': opdracht_form,
        'aanbieding': aanbieding,
    }
    # als de form is ingevuld en verstuurd word doet hij het volgende
    if request.method == 'POST':
        opdracht_form = OpdrachtenToevoegenForm(request.POST, request.FILES)
        if opdracht_form.is_valid():
            opdracht = opdracht_form.save()
            opdracht.aanbieding = aanbieding
            opdracht.status_opdracht = '1'
            opdracht.opdracht_aangemaakt_door = aanbieding.aangemaakt_door
            opdracht.save()
            aanbieding.status = '5'
            aanbieding.save()

            medewerker = opdracht.aanbieding.medewerker
            medewerker.status = '2'
            medewerker.save()
            opdracht.save()

            return redirect('lopende_opdrachten')
        # dit gebeurt als de form niet valid is
        else:
            # hier word de gebruiker doorgestuurd naar de form
            return render(request, 'opdracht.toevoegen.html', context)
    # als er niet ge "POST" word stuurt hij je naar de form
    else:
        return render(request, 'opdracht.toevoegen.html', context)


@login_required(login_url='login')
def lopendeOpdrachtenPage(request):
    lopendeOpdrachtenList = Opdrachten.objects.filter(Q(status_opdracht=1))

    context = {
        'lopendeOpdrachtenList': lopendeOpdrachtenList,
    }

    return render(request, 'lopende.opdrachten.html', context)


@login_required(login_url='login')
def aflopendeOpdrachtenPage(request):
    datum_nu = date.today()
    eind_datum = datum_nu + timedelta(days=60)
    aflopendeOpdrachten = Opdrachten.objects.filter(Q(status_opdracht=1), einddatum__range=[datum_nu, eind_datum])

    context = {
        'aflopendeOpdrachten': aflopendeOpdrachten,
    }

    return render(request, 'aflopende.opdrachten.html', context)


@login_required(login_url='login')
def archiefOpdrachtenPage(request):
    opdrachtenLijst = Opdrachten.objects.filter(Q(status_opdracht=2))

    context = {
        'opdrachtenLijst': opdrachtenLijst,
    }

    return render(request, 'archief.opdrachten.html', context)


@login_required(login_url='login')
def OpdrachtenUpdaten(request, pk):
    opdracht = Opdrachten.objects.get(id=pk)
    opdracht_form = OpdrachtenForm(request.POST or None, instance=opdracht)

    aanbieding = opdracht.aanbieding
    aanbieding_form = AanbiedingUpdatenForm(request.POST or None, instance=aanbieding)

    context = {
        'opdracht': opdracht,
        'aanbieding': aanbieding,
        'opdracht_form': opdracht_form,
        'aanbieding_form': aanbieding_form,
    }

    if request.method == 'POST':
        opdracht_form = OpdrachtenForm(request.POST or None, instance=opdracht)
        aanbieding_form = AanbiedingUpdatenForm(request.POST or None, instance=aanbieding)
        if opdracht_form.is_valid() and aanbieding_form.is_valid():
            opdracht = opdracht_form.save()
            aanbieding = aanbieding_form.save()
            medewerker = aanbieding.medewerker
            if opdracht.status_opdracht == '2':
                aanbieding.status = '6'
                aanbieding.save()
                medewerker.status = '3'
                medewerker.save()

            return redirect('lopende_opdrachten')
    return render(request, 'opdracht.update.html', context)


@login_required(login_url='login')
def OpdrachtenDetail(request, pk):
    opdracht = Opdrachten.objects.get(id=pk)
    opdracht_list = Opdrachten.objects.all()
    context = {
        'opdracht': opdracht,
        'opdracht_list': opdracht_list
    }
    return render(request, 'opdracht.detail.html', context)


@login_required(login_url='login')
def OpdrachtDelete(request, pk):
    opdracht = Opdrachten.objects.get(id=pk)

    try:
        aanbieding = opdracht.aanbieding
        aanbieding.status = '1'
        medewerker = aanbieding.medewerker
        medewerker.status = '3'
        medewerker.save()
        aanbieding.save()
    except:
        aanbieding = ''

    if opdracht.status_opdracht == '1':
        opdracht.status_opdracht = '2'
        opdracht.save()
        return redirect('lopende_opdrachten')
    elif opdracht.status_opdracht == '2':
        opdracht.delete()
        return redirect('archief_opdrachten')
    else:
        return redirect('lopende_opdrachten')

