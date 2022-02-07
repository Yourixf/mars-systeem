from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from project1 import forms
from .forms import FotoForm, MedewerkersToevoegenForm, ContractenToevoegenForm, EindklantenToevoegenForm, BrokersToevoegenForm, CertificatenToevoegenForm, LeaseautosToevoegenForm

# Create your views here.
from .models import Medewerkers, Leaseautos, Contracten, Certificaten, Opmerkingen, Eindklanten, Brokers

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'url']


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


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def Index(request):
    return render(request, 'index.html', )


@login_required(login_url='login')
def MedewerkersPage(request):
    medewerkers = Medewerkers.objects.all()
    return render(request, 'medewerkers.html', {'medewerkers': medewerkers})


@login_required(login_url='login')
def Detail(request, pk):
    medewerkers = Medewerkers.objects.get(id=pk)
    opmerkingen = Opmerkingen.objects.filter(medewerkers_id=pk)
    context = {'medewerkers': medewerkers, 'Opmerkingen': opmerkingen}
    all_data = Opmerkingen.objects.all().order_by("-id")
    if request.method == "POST":
        datum = request.POST["Datum"]
        medewerkers = Medewerkers.objects.get(id=pk)
        name_user = request.POST["Naam"]
        opmerking = request.POST["Opmerking"]
        data = Opmerkingen(datum_opmerkingen=datum, medewerkers=medewerkers, opmerkingveld=opmerking,
                           naam_user=name_user, )
        data.save()
        context = {'medewerkers': medewerkers, 'Opmerkingen': all_data}
        return render(request, 'detail.html', context)

    return render(request, 'detail.html', context)


@login_required(login_url='login')
def Leaseautosdetail(request, pk):
    leaseautos = Leaseautos.objects.get(id=pk)
    context = {'leaseautos': leaseautos, }
    return render(request, 'lease.autos.detail.html', context, )


@login_required(login_url='login')
def Contractendetail(request, pk):
    contracten = Contracten.objects.get(id=pk)
    certificaten = Certificaten.objects.get(id=pk)
    context = {'contracten': contracten, 'certificaten': certificaten, }
    return render(request, 'contracten.detail.html', context, )


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



class MedewerkerUpdate(UpdateView):
    model = Medewerkers
    fields = '__all__'
    template_name = 'update.medewerker.html'
    success_url = reverse_lazy('medewerkers')


class EindklantUpdate(UpdateView):
    model = Eindklanten
    fields = '__all__'
    template_name = 'update.eindklant.html'
    success_url = reverse_lazy('eindklanten')

class BrokerUpdate(UpdateView):
    model = Brokers
    fields = '__all__'
    template_name = 'update.broker.html'
    success_url = reverse_lazy('brokers')

@login_required(login_url='login')
def MedewerkerDelete(request, pk):
    delete_med = Medewerkers.objects.get(pk=pk)
    delete_med.delete()
    return redirect('medewerkers')


@login_required(login_url='login')
def EindklantenPage(request):
    eindkanten_list = Eindklanten.objects.all()
    return render(request, 'eindklanten.html', {'eindkanten_list': eindkanten_list, })


@login_required(login_url='login')
def EindklantToevoegen(request):
    form = EindklantenToevoegenForm()
    context = {
        'form': form
    }
    if request.method == 'get':
        form = EindklantenToevoegenForm(request)
        if form.is_valid():
            form.save()
            return redirect('eindklanten')
    else:
        return render(request, 'eindklant.toevoegen.html', context)


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

def BrokerDelete(request, id):
    delete_broker = Brokers.objects.get(id=id)
    delete_broker.delete()
    return redirect('brokers')

class ContractenUpdate(UpdateView):
    model = Contracten
    fields = '__all__'
    template_name = 'update.contracten.html'
    success_url = reverse_lazy('contracten.detail')

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
        form = CertificatenToevoegen(request.POST, request.FILES, instance=medewerker_pk)
        if form.is_valid():
            form.save()
            return redirect('medewerkers')
    else:
        return render(request, 'certificaten.toevoegen.html', context)

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

def LeaseautoDelete(request, id):
    delete_lease_auto = Leaseautos.objects.get(id=id)
    delete_lease_auto.delete()
    return redirect('lease.autos.detail')

def ContractenDelete(request, id):
    delete_contract = Contracten.objects.get(id=id)
    delete_contract.delete()
    return redirect('contracten.detail')

