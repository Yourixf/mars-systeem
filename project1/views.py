from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FotoForm
from . import forms
from django.views.generic.edit import CreateView
# Create your views here.
from .models import Medewerkers, Leaseautos, Contracten, Certificaten, Opmerkingen, Foto
from django.core.files.storage import FileSystemStorage

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


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
    return render(request, 'project1/register.html', context)


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
    return render(request, "project1/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def Index(request):
    return render(request, 'project1/index.html', )


@login_required(login_url='login')
def MedewerkersPage(request):
    medewerkers = Medewerkers.objects.all()
    return render(request, 'project1/medewerkers.html', {'medewerkers': medewerkers})



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
        return render(request, 'project1/detail.html', context)

    return render(request, 'project1/detail.html', context)


@login_required(login_url='login')
def Leaseautosdetail(request, pk):
    leaseautos = Leaseautos.objects.get(id=pk)
    context = {'leaseautos': leaseautos, }
    return render(request, 'project1/lease.autos.detail.html', context, )


@login_required(login_url='login')
def Contractendetail(request, pk):
    contracten = Contracten.objects.get(id=pk)
    certificaten = Certificaten.objects.get(id=pk)
    context = {'contracten': contracten, 'certificaten': certificaten, }
    return render(request, 'project1/contracten.detail.html', context, )


# class Medewerker_foto(CreateView):
#     model = Medewerkers
#     fields = ['foto_medewerker']
#     template_name = 'project1/foto.medewerker.form.html'


def Medewerker_foto(request, pk):
    """Process images uploaded by users"""
    medewerker = Medewerkers.objects.get(id=pk)
    medewerker.save()
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'project1/foto.medewerker.form.html', {'form': form, 'img_obj': img_obj})
    else:
        form = FotoForm()
    return render(request, 'project1/foto.medewerker.form.html', {'form': form})



