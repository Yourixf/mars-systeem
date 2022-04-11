import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from mysite import settings
from project1 import forms
from .forms import FotoForm, MedewerkersToevoegenForm, ContractenToevoegenForm, EindklantenToevoegenForm, \
    BrokersToevoegenForm, CertificatenToevoegenForm, LeaseautosToevoegenForm, AanbiedingenToevoegenForm, \
    CvUploadForm, DocumentenUploadForm, FeedbackUploadForm
# Create your views here.
from .models import Medewerkers, Leaseautos, Contracten, Certificaten, Opmerking, Eindklanten, Brokers, Aanbiedingen

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'url']


def OpmerkingMedewerker(request, pk):
    medewerker = Medewerkers.objects.get(pk=pk)
    docid = int(request.GET.get('docid', 0))
    opmerkingen = Opmerking.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')


        if docid > 0:
            opmerking = Opmerking.objects.get(pk=docid)
            opmerking.title = title
            opmerking.content = content
            opmerking.save()

            return HttpResponseRedirect(request.path_info)
            # return redirect('/test/?docid=%i' % pk % docid)
        else:
            opmerking = Opmerking.objects.create(title=title, content=content)

            return HttpResponseRedirect(request.path_info, opmerking)
            # return redirect('/test/?docid=%i' % opmerking.id, medewerker)

    if docid > 0:
        opmerking = Opmerking.objects.get(pk=docid)
    else:
        opmerking = ''

    context = {
        'docid': docid,
        'opmerkingen': opmerkingen,
        'opmerking': opmerking,
        'medewerker': medewerker,
    }

    return render(request, 'opmerking.medewerker.html', context)


def delete_opmerking(request, docid, pk):
    medewerker = Medewerkers.objects.get(pk=pk)
    opmerking = Opmerking.objects.get(pk=docid)
    opmerking.delete()
    context = {
        'medewerker': medewerker
    }

    return render(request, 'opmerking.medewerker.html', context)

@login_required(login_url='login')
def Detail(request, pk):
    medewerkers = Medewerkers.objects.get(id=pk)
    context = {
        'medewerkers': medewerkers,
    }
    return render(request, 'detail.html', context)


@login_required(login_url='login')
def AanbiedingenDetail(request, pk):
    aanbieding = Aanbiedingen.objects.get(id=pk)
    aanbiedingen_list = Aanbiedingen.objects.all()
    context = {
        'aanbieding': aanbieding,
        'aanbiedingen_list': aanbiedingen_list
    }
    return render(request, 'aanbieding.detail.html', context)


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


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


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


@login_required(login_url='login')
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


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


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


@login_required(login_url='login')
def MedewerkersPage(request):
    medewerkers = Medewerkers.objects.all()
    return render(request, 'medewerkers.html', {'medewerkers': medewerkers})


@login_required(login_url='login')
def MedewerkersToevoegen(request):
    form = MedewerkersToevoegenForm(request.POST or None)

    context = {
        'form': form
    }
    if request.method == 'POST':
        form = MedewerkersToevoegenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'medewerker.toevoegen.html', context)




class MedewerkerUpdate(LoginRequiredMixin, UpdateView):
    model = Medewerkers
    fields = '__all__'
    template_name = 'update.medewerker.html'
    success_url = reverse_lazy('medewerkers')


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


@login_required(login_url='login')
def Leaseautosdetail(request, pk):
    leaseautos = Leaseautos.objects.get(id=pk)
    context = {'leaseautos': leaseautos, }
    return render(request, 'lease.autos.detail.html', context, )


@login_required(login_url='login')
def LeaseautosToevoegen(request, pk):
    medewerker_pk = Medewerkers.objects.get(id=pk)
    leaseauto = Leaseautos.objects.filter(medewerkers_id=pk)
    form = CertificatenToevoegenForm(instance=medewerker_pk)
    context = {
        'form': form,
        'leaseauto': leaseauto,
    }
    if request.method == 'POST':
        form = LeaseautosToevoegenForm(request.POST, request.FILES, instance=medewerker_pk)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'lease.autos.toevoegen.html', context)


@login_required(login_url='login')
def LeaseautoDelete(request, id):
    delete_lease_auto = Leaseautos.objects.get(id=id)
    delete_lease_auto.delete()
    return redirect('lease.autos.detail')


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


@login_required(login_url='login')
def Contractendetail(request, pk):
    contracten = Contracten.objects.get(id=pk)
    certificaten = Certificaten.objects.get(id=pk)
    context = {'contracten': contracten, 'certificaten': certificaten, }
    return render(request, 'contracten.detail.html', context, )


@login_required(login_url='login')
def ContractenToevoegen(request, pk):
    medewerker_pk = Medewerkers.objects.get(id=pk)
    contract = Contracten.objects.filter(medewerkers_id=pk)
    form = ContractenToevoegenForm(instance=medewerker_pk)
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


@login_required(login_url='login')
def ContractenDelete(request, id):
    delete_contract = Contracten.objects.get(id=id)
    delete_contract.delete()
    return redirect('contracten.detail')



class ContractenUpdate(LoginRequiredMixin, UpdateView):
    model = Contracten
    fields = '__all__'
    template_name = 'update.contracten.html'
    success_url = reverse_lazy('contracten.detail')


@login_required(login_url='login')
def EindklantenPage(request):
    eindkanten_list = Eindklanten.objects.all()
    return render(request, 'eindklanten.html', {'eindkanten_list': eindkanten_list, })


@login_required(login_url='login')
def EindklantToevoegen(request):
    form = EindklantenToevoegenForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = EindklantenToevoegenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eindklanten')
    else:
        return render(request, 'eindklant.toevoegen.html', context)



class EindklantUpdate(LoginRequiredMixin, UpdateView):
    model = Eindklanten
    fields = '__all__'
    template_name = 'update.eindklant.html'
    success_url = reverse_lazy('eindklanten')


@login_required(login_url='login')
def EindklantDelete(request, id):
    delete_eindklant = Eindklanten.objects.get(id=id)
    delete_eindklant.delete()
    return redirect('eindklanten')


@login_required(login_url='login')
def BrokersPage(request):
    brokers_list = Brokers.objects.all()
    return render(request, 'brokers.html', {'brokers_list': brokers_list, })


@login_required(login_url='login')
def BrokersToevoegen(request):
    form = BrokersToevoegenForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = BrokersToevoegenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brokers')
    else:
        return render(request, 'brokers.toevoegen.html', context)


@login_required(login_url='login')
def BrokerDelete(request, id):
    delete_broker = Brokers.objects.get(id=id)
    delete_broker.delete()
    return redirect('brokers')


class BrokerUpdate(LoginRequiredMixin, UpdateView):
    model = Brokers
    fields = '__all__'
    template_name = 'update.broker.html'
    success_url = reverse_lazy('brokers')


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


@login_required(login_url='login')
def AanbiedingToevoegen(request):
    form = AanbiedingenToevoegenForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = AanbiedingenToevoegenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('aanbiedingen')
    else:
        return render(request, 'aanbiedingen.toevoegen.html', context)


@login_required(login_url='login')
def AanbiedingDelete(request, id):
    delete_aanbieding = Aanbiedingen.objects.get(id=id)
    delete_aanbieding.delete()
    return redirect('aanbiedingen')



class AanbiedingUpdate(LoginRequiredMixin, UpdateView):
    model = Aanbiedingen
    fields = '__all__'
    template_name = 'aanbieding.update.html'
    success_url = reverse_lazy('aanbiedingen')


@login_required(login_url='login')
def AanbiedingenPage(request):
    aanbieding_list = Aanbiedingen.objects.filter(Q(status=1) | Q(status=2) | Q(status=3))
    context = {
        'aanbieding_list': aanbieding_list,

    }
    return render(request, 'aanbiedingen.html', context)


@login_required(login_url='login')
def ArchiefAanbiedingenPage(request):
    aanbieding_list = Aanbiedingen.objects.filter(Q(status=4) | Q(status=5))
    context = {
        'aanbieding_list': aanbieding_list,

    }
    return render(request, 'aanbiedingen.archief.html', context)


@login_required(login_url='login')
def BrokerDetail(request, pk):
    broker = Brokers.objects.get(id=pk)
    broker_list = Brokers.objects.all()
    context = {
        'broker_list': broker_list,
        'broker': broker

    }
    return render(request, 'broker.detail.html', context)


@login_required(login_url='login')
def EindklantDetail(request, pk):
    eindklant = Eindklanten.objects.get(id=pk)
    eindklant_list = Eindklanten.objects.all()
    context = {
        'eindklant_list': eindklant_list,
        'eindklant': eindklant

    }
    return render(request, 'eindklanten.detail.html', context)
