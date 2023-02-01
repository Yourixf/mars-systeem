import getpass
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
from .forms import  *
from .models import *
from django.db.models import *
from itertools import chain


from django.contrib.auth.hashers import check_password


# De views.py kan je functies wegschrijven voor in de templates. Hier voor kan je dingen importen die staan bovenaan de template. (dingen vanuit Django en vanuit andere templates zoals Forms, Models enzov).
# @login_required(login_url='login') is een ingebouwde Django functie ter beveiliging als de "User" niet is ingelogd kan die niet op die pagina komen.

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'url']
# Voor de CV's, Feedbackdocumenten en overige documenten zijn dit de formats waarin het mag geupload worden.


@login_required(login_url='login')
def FactuurHistoryDetailPage(request, pk):
    opdracht = Opdrachten.objects.get(id=pk)

    if opdracht.aanbieding.broker_id:
        factuuremail = opdracht.aanbieding.broker.factuuremail
        broker_id = opdracht.aanbieding.broker_id
        broker_id = opdracht.aanbieding.broker_id
        try:
            hoofdvestiging = Vestigingplaats.objects.get(Q(klant_id=broker_id, vestiging='1'))
        except:
            hoofdvestiging = ''
    elif not opdracht.aanbieding.broker_id:
        factuuremail = opdracht.aanbieding.klant.factuuremail
        klant_id = opdracht.aanbieding.klant_id
        try:
            hoofdvestiging = Vestigingplaats.objects.get(Q(klant_id=klant_id, vestiging='1'))
        except:
            hoofdvestiging = ''


    context = {
        'opdracht':opdracht,
        'factuuremail':factuuremail,
        'hoofdvestiging':hoofdvestiging,
    }

    return render(request, 'factuur.history.detail.html', context)


@login_required(login_url='login')
def ContractHistoryPage(request):

    context = {
        '':''
    }

    return render(request, 'contract.history.html', context)

@login_required(login_url='login')
def FactuurHistoryPage(request):
    datum_nu = date.today() - timedelta(days=30)
    eind_datum = datum_nu + timedelta(days=60)
    opdrachten_list = Opdrachten.objects.filter(Q(status_opdracht=1), begindatum__range=[datum_nu, eind_datum])

    context = {
        'opdrachten_list':opdrachten_list,
    }

    return render(request, 'factuur.history.html', context)

@login_required(login_url='login')
def InhuurHistoryPage(request):


    context = {
        '':''
    }

    return render(request, 'inhuur.history.html', context)



@login_required(login_url='login')
def ContactpersoonDetailPage(request, pk):
    contactpersoon = Contactpersonen.objects.get(id=pk)
    vestiging = contactpersoon.vestiging_id
    vestiging_lijst = Vestigingplaats.objects.filter(id=vestiging)

    klant_pk = contactpersoon.klant
    klant_soort = klant_pk.soort

    context = {
        'contactpersoon': contactpersoon,
        'vestiging_lijst':vestiging_lijst,
        'klant_pk':klant_pk,
        'klant_soort':klant_soort
    }
    return render(request, 'contactpersoon.detail.html', context)

@login_required(login_url='login')
def ContactVestigingDeleten(request, pk):
    vorige_pagina = request.META['HTTP_REFERER']
    previous_page = request.session.get('vorige_pagina')
    contactpersoon = Contactpersonen.objects.get(id=pk)
    contactpersoon.vestiging_id = ''
    contactpersoon.save()
    contactpersoon_pk = contactpersoon.pk

    return redirect('detail_contactpersonen', contactpersoon_pk)

@login_required(login_url='login')
def ContactVestigingToevoegen(request, pk):
    vorige_pagina = request.META['HTTP_REFERER']
    test = request.META['HTTP_REFERER']

    if 'broker' in vorige_pagina:
        request.session['vorige_pagina'] = 'broker'
        contactpersoon = Contactpersonen.objects.get(id=pk)
        broker_pk = contactpersoon.klant
        vestiging_lijst = Vestigingplaats.objects.filter(klant_id=broker_pk)

        context = {
            'contactpersoon': contactpersoon,
            'broker_pk': broker_pk,
            'vestiging_lijst': vestiging_lijst,
        }
        request.session['test'] = contactpersoon.id

    elif 'klant' in vorige_pagina:
        request.session['vorige_pagina'] = 'klant'
        contactpersoon = Contactpersonen.objects.get(id=pk)
        eind_klant_pk = contactpersoon.klant
        vestiging_lijst = Vestigingplaats.objects.filter(klant_id=eind_klant_pk)

        context = {
            'contactpersoon':contactpersoon,
            'eind_klant_pk': eind_klant_pk,
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
            brokerr = contactpersoon.klant.pk

            return redirect('broker_detail', brokerr)
        elif 'klant' in previous_page:
            contactpersoon = Contactpersonen.objects.get(id=contactpersoon_id)
            contactpersoon.vestiging_id = pk
            contactpersoon.save()
            klantt = contactpersoon.klant.pk

            return redirect('eindklant_detail', klantt)

    else:
        return render(request, 'contact.vestiging.toevoegen.html', context)



@login_required(login_url='login')
def ContactPersonenDelete(request, pk):
    contactpersoon = Contactpersonen.objects.get(id=pk)
    contactpersoon_form = ContactpersoonForm(request.POST or None, instance=contactpersoon)

    klant = contactpersoon.klant

    contactpersoon = contactpersoon_form.save()
    contactpersoon.vestiging_id = ''
    contactpersoon.save()
    contactpersoon.delete()

    if klant.soort == '1':
        return redirect('eindklant_detail', klant.pk)
    elif klant.soort == '2':
        return redirect('broker_detail', klant.pk)

@login_required(login_url='login')
def ContactPersonenToevoegen(request, pk):
    contactpersoon_form = ContactpersoonForm()

    klant_pk = Klanten.objects.get(id=pk)
    context = {
        'contactpersoon_form':contactpersoon_form,
        'klant_pk':klant_pk
    }

    if request.method == 'POST':
        contactpersoon_form = ContactpersoonForm(request.POST, request.FILES)
        if contactpersoon_form.is_valid():
            contactpersoon = contactpersoon_form.save()
            contactpersoon.klant_id = pk
            contactpersoon.save()
            if klant_pk.soort == '1':
                return redirect('eindklant_detail', klant_pk.pk)
            elif klant_pk.soort == '2':
                return redirect('broker_detail', klant_pk.pk)
    else:
        return render(request, 'contactpersoon.toevoegen.html', context)


@login_required(login_url='login')
def ContactPersoonUpdaten(request, pk):
    contactpersoon_pk = Contactpersonen.objects.get(id=pk)
    contactpersoon_form = ContactpersoonUpdatenForm(instance=contactpersoon_pk)

    vorige_pagina = request.META.get('HTTP_REFERER')
    request.session['vorige_pagina'] = 'klant'
    klant_pk = contactpersoon_pk.klant
    context = {
        'contactpersoon_form': contactpersoon_form,
        'contactpersoon_pk': contactpersoon_pk,
        'klant_pk':klant_pk
    }

    if request.method == 'POST':
        previous_page = request.session.get('vorige_pagina')
        contactpersoon_form = ContactpersoonUpdatenForm(request.POST, request.FILES, instance=contactpersoon_pk)
        if contactpersoon_form.is_valid():

            if Contactpersonen_History.objects.filter(contactpersoon_id=contactpersoon_pk.pk):
                contactpersonen_lijst = Contactpersonen_History.objects.filter(contactpersoon_id=contactpersoon_pk.pk)
                laatste_contactpersoon = contactpersonen_lijst.latest('id')
                laatste_update_nmr = laatste_contactpersoon.update_id
                update_nmr = laatste_update_nmr + 1
            elif not Contactpersonen_History.objects.filter(contactpersoon_id=contactpersoon_pk.pk):
                update_nmr = 1

            if contactpersoon_pk.klant:
                contactKlant_id = contactpersoon_pk.klant_id
                contactKlant = Klanten.objects.get(id=contactKlant_id)
            elif not contactpersoon_pk.klant_id:
                contactKlant = None

            if contactpersoon_pk.vestiging_id:
                contactVestiging_id = contactpersoon_pk.vestiging_id
                contactVestiging = Vestigingplaats.objects.get(id=contactVestiging_id)
            elif not contactpersoon_pk.vestiging_id:
                contactVestiging = None

            contactpersoon_history = Contactpersonen_History(
                contactpersoon=contactpersoon_pk,
                update_id=update_nmr,
                naam=contactpersoon_form.initial.get('naam'),
                mail_adres=contactpersoon_form.initial.get('mail_adres'),
                telefoonnummer=contactpersoon_form.initial.get('telefoonnummer'),
                functie=contactpersoon_form.initial.get('functie'),
                klant=contactKlant,
                vestiging=contactVestiging,
                opmerkingen=contactpersoon_form.initial.get('opmerkingen'),
            )

            contactpersoon_history.save()
            contactpersoon = contactpersoon_form.save()
            contactpersoon.begindatum = dateformat.format(timezone.now(), 'o-m-d')
            contactpersoon.save()

            if klant_pk.soort == '1':
                return redirect('eindklant_detail', klant_pk.pk)
            elif klant_pk.soort == '2':
                return redirect('broker_detail', klant_pk.pk)
    else:
        return render(request, 'update.contactpersoon.html', context)

@login_required(login_url='login')
def VestigingToevoegen(request, pk):
    vestiging_form = VestigingplaatsForm()

    klant_pk = Klanten.objects.get(id=pk)

    context = {
        'vestiging_form':vestiging_form,
        'klant_pk':klant_pk
    }

    if request.method == 'POST':
        vestiging_form = VestigingplaatsForm(request.POST, request.FILES)
        if vestiging_form.is_valid():
            vestiging = vestiging_form.save()
            vestiging.klant_id = pk
            vestiging.save()

            if klant_pk.soort == '1':
                return redirect('eindklant_detail', klant_pk.pk)
            elif klant_pk.soort == '2':
                return redirect('broker_detail', klant_pk.pk)
    else:
        return render(request, 'vestiging.toevoegen.html', context)

@login_required(login_url='login')
def VestigingUpdaten(request, pk):
    vestiging_pk = Vestigingplaats.objects.get(id=pk)
    vestiging_form = VestigingplaatsForm(instance=vestiging_pk)

    vorige_pagina = request.META['HTTP_REFERER']
    request.session['vorige_pagina'] = 'klant'
    klant_pk = vestiging_pk.klant

    context = {
        'vestiging_form': vestiging_form,
        'vestiging_pk': vestiging_pk,
        'klant_pk': klant_pk
    }
    previous_pagina = request.session.get('vorige_pagina')

    if request.method == 'POST':
        vestiging_form = VestigingplaatsForm(request.POST, request.FILES, instance=vestiging_pk)
        if vestiging_form.is_valid():

            if Vestigingplaats_History.objects.filter(Q(vestig_id=vestiging_pk.pk)):
                vestiging = Vestigingplaats_History.objects.filter(Q(vestig_id=vestiging_pk.pk))
                laatste_vestiging = vestiging.latest('id')
                laatste_update_nmr = laatste_vestiging.update_id
                update_nmr = laatste_update_nmr + 1
            elif not Vestigingplaats_History.objects.filter(Q(vestig_id=vestiging_pk.pk)):
                update_nmr = 1

            if vestiging_pk.klant:
                vestigingKlant_id = vestiging_pk.klant_id
                vestigingKlant = Klanten.objects.get(id=vestigingKlant_id)
            elif not vestiging_pk.klant:
                vestigingKlant = None

            History_record = Vestigingplaats_History(
                vestig=vestiging_pk,
                update_id=update_nmr,
                postcode=vestiging_form.initial.get('postcode'),
                straatnaam=vestiging_form.initial.get('straatnaam'),
                huisnummer=vestiging_form.initial.get('huisnummer'),
                plaats=vestiging_form.initial.get('plaats'),
                vestiging=vestiging_form.initial.get('vestiging'),
                klant=vestigingKlant,
                opmerkingen=vestiging_form.initial.get('opmerkingen')
            )

            History_record.save()
            vestiging_form = vestiging_form.save()
            vestiging_form.begindatum = dateformat.format(timezone.now(), 'o-m-d')
            vestiging_form.save()

            if klant_pk.soort =='2':
                return redirect('broker_detail', klant_pk.pk)
            elif klant_pk.soort == '1' :
                return redirect('eindklant_detail', klant_pk.pk)

    else:
        return render(request, 'update.vestiging.html', context)


@login_required(login_url='login')
def VestigingDetailPage(request, pk):
    vestiging = Vestigingplaats.objects.get(id=pk)

    vorige_pagina = request.META['HTTP_REFERER']

    klant_pk = vestiging.klant

    context = {
        'vestiging': vestiging,
        'klant_pk': klant_pk,
    }

    return render(request, 'vestiging.detail.html', context)

@login_required(login_url='login')
def VestigingDeleten(request, pk):
    vestiging = Vestigingplaats.objects.get(id=pk)
    klant = vestiging.klant

    vestiging.klant_id = ''
    vestiging.save()

    contactpersoon_lijst = Contactpersonen.objects.filter(vestiging_id=vestiging.id)

    for c in contactpersoon_lijst:
        c.vestiging_id = ''
        c.save()

    vestiging.delete()

    if klant.soort == '1':
        return redirect('eindklant_detail', klant.pk)
    elif klant.soort == '2':
        return redirect('broker_detail', klant.pk)



    #vestiging = vestiging_form.save()
    #klant = vestiging.klant
    #klant.vestiging_id = ''

    #klant.save()
    #vestiging.save()
    # vestiging.delete()

    #if klant.soort == '1':
    #    return redirect('eindklant_detail', klant.pk)
    #elif klant.soort == '2':
    #    return redirect('broker_detail', klant.pk)

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



# Dit is de de details pagina voor de Medewerkers,    medewerkers = Medewerkers.objects.get(id=pk) is bedoeld om elke detail per eindklant te zien is.
@login_required(login_url='login')
def MedewerkerDetail(request, pk):
    medewerkers = Medewerkers.objects.get(id=pk)


    documenten_lijst = Documenten.objects.filter(medewerker_id=pk)
    context = {
        'medewerkers': medewerkers,
        'documenten_lijst': documenten_lijst,
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
    documenten_form = DocumentenForm(instance=medewerker_pk)
    #file = request.POST.get('documenten')
    context = {
        'medewerker_pk': medewerker_pk,
        'documenten_form': documenten_form,
    }

    if request.method == 'POST':
        documenten_form = DocumentenForm(request.POST, request.FILES)
        if documenten_form.is_valid():
            document = documenten_form.save()
            document.save()
            document.medewerker_id = pk
            document.save()

            return redirect('details', medewerker_pk.id)
    else:
        return render(request, 'documenten.upload.html', context)


@login_required(login_url='login')
def DocumentenDelete(request, pk):
    document = Documenten.objects.get(id=pk)
    medewerker = document.medewerker_id
    document.medewerker_id = ''
    document_path = document.document

    try:
        file_path = os.path.join(settings.MEDIA_ROOT, str(document_path))
        if os.path.exists(file_path):
            os.remove(file_path)
    except:
        file = ''

    document.save()
    document.delete()

    return redirect('details', medewerker)

@login_required(login_url='login')
def DocumentenUpdate(request, pk):
    document = Documenten.objects.get(id=pk)
    document_form = DocumentenUpdatenForm(instance=document)
    context = {
        'document':document,
        'document_form':document_form,
    }
    if request.method == 'POST':
        document_form = DocumentenUpdatenForm(request.POST, request.FILES, instance=document)
        if document_form.is_valid():

            if Documenten_History.objects.filter(Q(document_id=document.pk)):
                Docu = Documenten_History.objects.filter(Q(document_id=document.pk))
                laatste_docu = Docu.latest('id')
                laatste_update_nmr = laatste_docu.update_id
                update_nmr = laatste_update_nmr + 1
            elif not Documenten_History.objects.filter(Q(document_id=document.pk)):
                update_nmr = 1

            if document.medewerker_id:
                documentMedewerker_id = document.medewerker_id
                documentMedewerker = Medewerkers.objects.get(id=documentMedewerker_id)
            elif not document.medewerker_id:
                documentMedewerker = None


            history_record = Documenten_History(
                document=document,
                naam_document=document_form.initial.get('naam_document'),
                update_id=update_nmr,
                soort_document=document_form.initial.get('soort_document'),
                beschrijving=document_form.initial.get('beschrijving'),
                document_path=document_form.initial.get('document_path'),
                medewerker=documentMedewerker
                )

            originele_document = document_form.save()

            originele_document.begindatum = dateformat.format(timezone.now(), 'o-m-d')
            originele_document.save()
            history_record.save()
            return redirect('medewerkers')

    return render(request, 'documenten.update.html', context)



# Haalt de gegevens van de CreateUserForm uit de forms.py en met de POST method is de mode waarbij een form kan worden ingevuld.
# Met de if request.method == 'POST': checkt django of het klopt dat het een form is die wordt ingevuld.
# dan komt if form.is_valid(): form.save() is de functie dat django checkt of de form 'valid' is en dan slaat die de form op.
# daarna een succes bericht ( messages.success(request, 'account is gemaakt voor ' + user) en daarna stuurt die je terug naar de login pagina.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account is gemaakt voor ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


# De login vraagt om een username en password, als deze overeen komen kom je in de applicatie. anders kom je terug bij de login pagina met een bericht dat het wachtwoord of username niet klopt
def loginPage(request):
    message =''
    if request.method == 'POST':
        username = request.POST.get('username', )
        password = request.POST.get('password', )

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = messages.info(request, 'Gebruikersnaam of wachtwoord klopt niet')

    context = {'message':message}
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
    all_medewerkers_indienst = Medewerkers.objects.all().exclude(Q(status='4'))
    medewerkers_count = all_medewerkers_indienst.count()

    leegloop_medewerkers = Medewerkers.objects.filter(Q(status='3'))
    leegloop_medewerkers_count = leegloop_medewerkers.count()

    all_klanten = Eindklanten.objects.all()
    klanten_count = all_klanten.count()

    all_aanbieding = Aanbiedingen.objects.filter(Q(status='1'))
    open_aanbied_count = all_aanbieding.count()

    arrayMedeAanbieding = []

    for medewerker in all_medewerkers_indienst:
        aanbiedingen = all_aanbieding.filter(medewerker=medewerker).count()
        if aanbiedingen > 0 :
            class medeAanb():
                medePK = medewerker.pk
                medeNaam = medewerker
                aanb = aanbiedingen
            arrayMedeAanbieding.append(medeAanb)

    datum_nu = date.today()
    eind_datum = datum_nu + timedelta(days=60)
    all_aflopendeOpdr = Opdrachten.objects.filter(Q(status_opdracht=1), einddatum__range=[datum_nu, eind_datum])

    context = {
        'medewerkers_count': medewerkers_count,
        'leegloop_medewerkers_count': leegloop_medewerkers_count,
        'klanten_count': klanten_count,
        'open_aanbied_count': open_aanbied_count,
        'all_aanbieding':all_aanbieding,
        'all_aflopendeOpdr':all_aflopendeOpdr,
        'arrayMedeAanbieding':arrayMedeAanbieding,
    }
    return render(request, 'index.html', context)


# Dit is de Medewerkers pagina  medewerkers = Medewerkers.objects.all() haalt allemedewerkers op.
@login_required(login_url='login')
def MedewerkersPage(request):
    medewerkers = Medewerkers.objects.all().exclude(Q(status='4'))
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
    aanbieding_list = aanbieding_list.exclude(Q(status='6'))

    opdracht_list = Opdrachten.objects.filter(Q(aanbieding__medewerker=medewerker))
    opdracht_list = opdracht_list.exclude(Q(status_opdracht='2'))

    context = {
        'aanbieding_list': aanbieding_list,
        'opdracht_list': opdracht_list,
        'medewerker':medewerker,
    }

    return render(request, 'medewerker.opdrachten.aanbiedingen.html', context)


# De Medewerkerstoevoegen form uit de Forms.py
@login_required(login_url='login')
def MedewerkersToevoegen(request):
    medewerker_form = MedewerkersForm(request.POST or None)

    context = {
        'medewerker_form': medewerker_form
    }
    if request.method == 'POST':
        medewerker_form = MedewerkersForm(request.POST, request.FILES)
        if medewerker_form.is_valid():
            medewerker_form.save()
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
        medewerker_form = MedewerkersForm(request.POST or None, instance=medewerker)
        # form.save() om de nieuwe data op te slaan
        if medewerker_form.is_valid():

            if Medewerkers_History.objects.filter(medewerker_id=medewerker.pk):
                mede = Medewerkers_History.objects.filter(medewerker_id=medewerker.pk)
                laatste_mede = mede.latest('id')
                laatste_update_nmr = laatste_mede.update_id
                update_nmr = laatste_update_nmr + 1
            elif not Medewerkers_History.objects.filter(medewerker_id=medewerker.pk):
                update_nmr = 1

            History_record = Medewerkers_History(
                medewerker=medewerker,
                update_id=update_nmr,
                voornaam=medewerker_form.initial.get('voornaam'),
                tussenvoegsel=medewerker_form.initial.get('tussenvoegsel'),
                achternaam=medewerker_form.initial.get('achternaam'),
                roepnaam=medewerker_form.initial.get('roepnaam'),
                functie=medewerker_form.initial.get('functie'),
                geboortedatum=medewerker_form.initial.get('geboortedatum'),
                geboorteplaats=medewerker_form.initial.get('geboorteplaats'),
                nationaliteit=medewerker_form.initial.get('nationaliteit'),
                straat=medewerker_form.initial.get('straat'),
                huisnummer=medewerker_form.initial.get('huisnummer'),
                postcode=medewerker_form.initial.get('postcode'),
                woonplaats=medewerker_form.initial.get('woonplaats'),
                telefoonnummer=medewerker_form.initial.get('telefoonnummer'),
                bsnnummer=medewerker_form.initial.get('bsnnummer'),
                banknummer=medewerker_form.initial.get('banknummer'),
                bv=medewerker_form.initial.get('bv'),
                burgerlijkse_staat=medewerker_form.initial.get('burgelijkse_staat'),
                opleidingsniveau=medewerker_form.initial.get('opleidingsniveau'),
                ice_persoon_naam=medewerker_form.initial.get('ice_persoon_naam'),
                ice_telefoonnummer=medewerker_form.initial.get('ice_telefoonnummer'),
                datum_in_dienst=medewerker_form.initial.get('datum_in_dienst'),
                lease_auto=medewerker_form.initial.get('lease_auto'),
                aantal_uur=medewerker_form.initial.get('aantal_uur'),
                status=medewerker_form.initial.get('status'),
                tariefindicatie=medewerker_form.initial.get('tariefindicatie'),
            )

            orginele_medewerker_form = medewerker_form.save()
            orginele_medewerker_form.begindatum = dateformat.format(timezone.now(), 'o-m-d')
            History_record.save()
            orginele_medewerker_form.save()
            return redirect('details', medewerker.pk)

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
    #eindklanten_list = Eindklanten.objects.all()
   #eindklant_pk = Eindklanten.objects.filter()
    #vestiging = Vestigingplaats.objects.filter(klant_id=eindklant_pk)
    #contactpersoon = Contactpersonen.objects.filter(klant_id=eindklant_pk)

    eindklanten_list = Klanten.objects.filter(Q(soort='1'))


    context = {
        'eindklanten_list': eindklanten_list,
        #'vestiging': vestiging,
        #'eindklant_pk': eindklant_pk,
        #'contactpersoon': contactpersoon
    }

    return render(request, 'eindklanten.html', context)


# De eindklant toevoegen form EindklantenToevoegenForm uit de forms.py
@login_required(login_url='login')
def EindklantToevoegen(request):
    klant_form = KlantenToevoegenForm(request.POST or None)

    context = {
        'klant_form': klant_form,
    }


    if request.method == 'POST':
        klant_form = KlantenToevoegenForm(request.POST, request.FILES)

        if klant_form.is_valid():
            klant = klant_form.save()
            klant.soort = '1'
            klant.save()
            return redirect('eindklanten')
    else:
        return render(request, 'eindklant.toevoegen.html', context)


# De updateview voor de Eindklanten.

@login_required(login_url='login')
def EindklantenUpdaten(request, pk):
    eindklant = Klanten.objects.get(id=pk)
    eindklant_form = KlantenUpdatenForm(request.POST or None, instance=eindklant)

    context = {
        'eindklant': eindklant,
        'eindklant_form': eindklant_form,
    }
    if request.method == 'POST':
        eindklant_form = KlantenUpdatenForm(request.POST or None, instance=eindklant)
        if eindklant_form.is_valid():

            if Klanten_History.objects.filter(Q(klant_id=eindklant.pk)):
                klant = Klanten_History.objects.filter(Q(klant_id=eindklant.pk))
                laatste_klant = klant.latest('id')
                laatste_update_nmr = laatste_klant.update_id
                update_nmr = laatste_update_nmr + 1
            elif not Klanten_History.objects.filter(Q(klant_id=eindklant.pk)):
                update_nmr = 1


            initi = eindklant_form.initial

            History_Record = Klanten_History(
                klant=eindklant,
                update_id=update_nmr,
                accountmanager=eindklant_form.initial.get('accountmanager'),
                naam=eindklant_form.initial.get('naam'),
                telefoonnummer=eindklant_form.initial.get('telefoonnummer'),
                portaal=eindklant_form.initial.get('portaal'),
                soort=eindklant_form.initial.get('soort')
            )

            originele_eindklant = eindklant_form.save()

            originele_eindklant.begindatum = dateformat.format(timezone.now(), 'o-m-d')


            History_Record.save()
            originele_eindklant.save()
            return redirect('eindklanten')
    return render(request, "update.eindklant.html", context)


# De Delete functie voor de eindklanten.
@login_required(login_url='login')
def EindklantDelete(request, id):
    delete_eindklant = Klanten.objects.get(id=id)
    delete_eindklant.delete()
    return redirect('eindklanten')


# Dit is de de details pagina voor de Eindklanten,     eindklant_pk = Eindklanten.objects.get(id=pk) is bedoeld om elke detail per eindklant te zien is.
#    eindklant = Eindklanten.objects.all() is bedoeld zodat je elke variabele op de details pagina kan laten zien.
@login_required(login_url='login')
def EindklantDetail(request, pk):
    eindklant_pk = Klanten.objects.get(id=pk)
    vestiging_lijst = Vestigingplaats.objects.filter(Q(klant_id=eindklant_pk.id))
    contactpersoon_lijst = Contactpersonen.objects.filter(Q(klant_id=eindklant_pk.id))

    pizza = False

    for c in contactpersoon_lijst:
        if hasattr(c, 'vestiging'):
            pizza = True
        elif not hasattr(c, 'vestiging'):
            pizza = False
            break

    # hier kijkt de code of er een vestiging adres is
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
        'contactpersoon_lijst': contactpersoon_lijst,
        'pizza' : pizza

    }
    return render(request, 'eindklanten.detail.html', context)



# De overzicht pagina van de Brokers   brokers_list = Brokers.objects.all() haalt alle gegevens op uit de Brokers model.
@login_required(login_url='login')
def BrokersPage(request):
    brokers_list = Klanten.objects.filter(Q(soort='2'))


    context = {
        'brokers_list':brokers_list,
    }

    return render(request, 'brokers.html', context)


# De Brokers toevoegen form BrokersToevoegenForm uit de forms.py
@login_required(login_url='login')
def BrokersToevoegen(request):
    form = KlantenToevoegenForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = KlantenToevoegenForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            form.save()

            form.soort = '2'
            form.save()
            return redirect('brokers')
    else:
        return render(request, 'brokers.toevoegen.html', context)


# De Delete functie voor de Broker.
@login_required(login_url='login')
def BrokerDelete(request, id):
    delete_broker = Klanten.objects.get(id=id)
    delete_broker.delete()
    return redirect('brokers')


# De updateview voor de Brokers.

@login_required(login_url='login')
def BrokerUpdaten(request, pk):
    broker = Klanten.objects.get(id=pk)
    broker_form = KlantenUpdatenForm(request.POST or None, instance=broker)

    context = {
        'broker': broker,
        'broker_form': broker_form,
    }

    if request.method == 'POST':
        broker_form = KlantenUpdatenForm(request.POST or None, instance=broker)
        if broker_form.is_valid():

            if Klanten_History.objects.filter(Q(klant_id= broker.pk)):
                klant = Klanten_History.objects.filter(Q(klant_id=broker.pk))
                laatste_klant = klant.latest('id')
                laatste_update_nmr = laatste_klant.update_id
                update_nmr = laatste_update_nmr + 1
            elif not Klanten_History.objects.filter(Q(klant_id=broker.pk)):
                update_nmr = 1

            History_Record = Klanten_History(
                klant=broker,
                update_id=update_nmr,
                accountmanager=broker_form.initial.get('accountmanager'),
                naam=broker_form.initial.get('naam'),
                telefoonnummer=broker_form.initial.get('telefoonnummer'),
                portaal=broker_form.initial.get('portaal'),
                soort=broker_form.initial.get('soort')
            )

            History_Record.save()

            broker = broker_form.save()
            broker.begindatum = dateformat.format(timezone.now(), 'o-m-d')
            broker.save()
            return redirect('brokers')

    return render(request, "update.broker.html", context)


# Dit is de de details pagina voor de Brokers,     broker = Brokers.objects.get(id=pk) is bedoeld om elke detail per eindklant te zien is.
#  broker_list = Brokers.objects.all() is bedoeld zodat je elke variabele op de details pagina kan laten zien.
@login_required(login_url='login')
def BrokerDetail(request, pk):
    klant = Klanten.objects.get(id=pk)
    vestiging_lijst = Vestigingplaats.objects.filter(Q(klant_id=klant.id))
    contactpersoon_lijst = Contactpersonen.objects.filter(Q(klant_id=klant.id))


    context = {
        'klant': klant,
        'vestiging_lijst': vestiging_lijst,
        'contactpersoon_lijst': contactpersoon_lijst
    }
    return render(request, 'broker.detail.html', context)


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
       # aanbieding_form = AanbiedingenForm(request.POST, request.FILES)
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
        return redirect('index')
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

        if aanbieding_form.is_valid():

            if Aanbiedingen_History.objects.filter(Q(aanbieding_id=aanbieding.pk)):
                aanbiedingen = Aanbiedingen_History.objects.filter(Q(aanbieding_id=aanbieding.pk))
                laatste_aanbieding = aanbiedingen.latest('id')
                laatste_update_nmr = laatste_aanbieding.update_id
                update_nmr = laatste_update_nmr + 1
            elif not Aanbiedingen_History.objects.filter(Q(aanbieding_id=aanbieding.pk)):
                update_nmr = 1

            if aanbieding.klant_id:
                aanbiedingKlant_id = aanbieding.klant_id
                aanbiedingKlant = Klanten.objects.get(id=aanbiedingKlant_id)
            elif not aanbieding.klant_id:
                aanbiedingKlant = None

            if aanbieding.broker_id:
                aanbiedingBroker_id = aanbieding.broker_id
                aanbiedingBroker = Klanten.objects.get(id=aanbiedingBroker_id)
            elif not aanbieding.broker_id:
                aanbiedingBroker = None

            if aanbieding.medewerker_id:
                aanbiedingMedewerker_id = aanbieding.medewerker_id
                aanbiedingMedewerker = Medewerkers.objects.get(id=aanbiedingMedewerker_id)
            elif not aanbieding.medewerker_id:
                aanbiedingMedewerker = None

            history_record = Aanbiedingen_History(
                aanbieding=aanbieding,
                update_id=update_nmr,
                aangemaakt_door=aanbieding_form.initial.get('aangemaakt_door'),
                registratie=aanbieding_form.initial.get('registratie'),
                laatste_update=aanbieding_form.initial.get('laatste_update'),
                functie=aanbieding_form.initial.get('functie'),
                functie_aanbieding=aanbieding_form.initial.get('functie_aanbieding'),
                klant=aanbiedingKlant,
                broker=aanbiedingBroker,
                accountmanager=aanbieding_form.initial.get('accountmanager'),
                status=aanbieding_form.initial.get('status'),
                tarief=aanbieding_form.initial.get('tarief'),
                betaalkorting=aanbieding_form.initial.get('betaalkorting'),
                opmerking=aanbieding_form.initial.get('opmerking'),
                medewerker=aanbiedingMedewerker,
            )

            history_record.save()

            aanbieding = aanbieding_form.save()

            aanbieding.begindatum = dateformat.format(timezone.now(), 'o-m-d')
            aanbieding.save()

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

            # Voor oprachten history functie
            if Opdrachten_History.objects.filter(Q(opdracht_id=opdracht.pk)):
                opdr = Opdrachten_History.objects.filter(Q(opdracht_id=opdracht.pk))
                laatste_opdr = opdr.latest('id')
                laatste_update_nmr = laatste_opdr.update_id
                update_nmr = laatste_update_nmr + 1
            if not Opdrachten_History.objects.filter(Q(opdracht_id=opdracht.pk)):
                update_nmr = 1


            if opdracht.aanbieding:
                opdrachtAanbieding_id = opdracht.aanbieding_id
                opdrachtAanbieding = Aanbiedingen.objects.get(id=opdrachtAanbieding_id)
            elif not opdracht.aanbieding:
                opdrachtAanbieding = None


            Opdracht_history_record = Opdrachten_History(
                opdracht=opdracht,
                update_id=update_nmr,
                aanbieding=opdrachtAanbieding,
                status_opdracht=opdracht_form.initial.get('status_opdracht'),
                startdatum=opdracht_form.initial.get('startdatum'),
                einddatum=opdracht_form.initial.get('einddatum'),
                tarief_opdracht=opdracht_form.initial.get('tarief_opdracht'),
                opdracht_betaalkorting=opdracht_form.initial.get('opdracht_betaalkorting'),
                aantal_uren=opdracht_form.initial.get('aantal_uren'),
                opdracht_aangemaakt_door=opdracht_form.initial.get('opdracht_aangemaakt_door'),
                opdracht_nummer=opdracht_form.initial.get('opdracht_nummer'),
                opmerking=opdracht_form.initial.get('opmerking'),
                date_created=opdracht_form.initial.get('date_created')
            )

            Opdracht_history_record.save()
            opdracht = opdracht_form.save()
            opdracht.begindatum= dateformat.format(timezone.now(), 'o-m-d')
            opdracht.save()

            # Voor aanbiedingen history functie
            if Aanbiedingen_History.objects.filter(Q(aanbieding_id=aanbieding.pk)):
                aanbiedingen = Aanbiedingen_History.objects.filter(Q(aanbieding_id=aanbieding.pk))
                laatste_aanbieding = aanbiedingen.latest('id')
                laatste_update_nmr = laatste_aanbieding.update_id
                update_nmr = laatste_update_nmr + 1
            elif not Aanbiedingen_History.objects.filter(Q(aanbieding_id=aanbieding.pk)):
                update_nmr = 1

            if aanbieding.klant_id:
                aanbiedingKlant_id = aanbieding.klant_id
                aanbiedingKlant = Klanten.objects.get(id=aanbiedingKlant_id)
            elif not aanbieding.klant_id:
                aanbiedingKlant = None

            if aanbieding.broker_id:
                aanbiedingBroker_id = aanbieding.broker_id
                aanbiedingBroker = Klanten.objects.get(id=aanbiedingBroker_id)
            elif not aanbieding.broker_id:
                aanbiedingBroker = None

            if aanbieding.medewerker_id:
                aanbiedingMedewerker_id = aanbieding.medewerker_id
                aanbiedingMedewerker = Medewerkers.objects.get(id=aanbiedingMedewerker_id)
            elif not aanbieding.medewerker_id:
                aanbiedingMedewerker = None

            history_record = Aanbiedingen_History(
                aanbieding=aanbieding,
                update_id=update_nmr,
                aangemaakt_door=aanbieding_form.initial.get('aangemaakt_door'),
                registratie=aanbieding_form.initial.get('registratie'),
                laatste_update=aanbieding_form.initial.get('laatste_update'),
                functie=aanbieding_form.initial.get('functie'),
                functie_aanbieding=aanbieding_form.initial.get('functie_aanbieding'),
                klant=aanbiedingKlant,
                broker=aanbiedingBroker,
                accountmanager=aanbieding_form.initial.get('accountmanager'),
                status=aanbieding_form.initial.get('status'),
                tarief=aanbieding_form.initial.get('tarief'),
                betaalkorting=aanbieding_form.initial.get('betaalkorting'),
                medewerker=aanbiedingMedewerker
            )

            history_record.save()

            aanbieding = aanbieding_form.save()
            aanbieding.begindatum = dateformat.format(timezone.now(), 'o-m-d')
            aanbieding.save()

            medewerker = aanbieding.medewerker
            if opdracht.status_opdracht == '2':
                aanbieding.status = '6'
                aanbieding.save()
                medewerker.status = '3'
                medewerker.save()

            if aanbieding.status == '1':
                medewerker.status = '3'
                medewerker.save()
            elif aanbieding.status == '2':
                medewerker.status = '1'
                medewerker.save()
            elif aanbieding.status == '3':
                medewerker.status = '2'
                medewerker.save()
            elif aanbieding.status == '4':
                medewerker.status = '3'
                medewerker.save()
            elif aanbieding.status == '5':
                medewerker.status = '2'
                medewerker.save()
            elif aanbieding.status == '6':
                medewerker.status = '3'
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