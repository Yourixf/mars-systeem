from django.shortcuts import render, redirect
from django.views import generic
# from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib import messages
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Medewerkers, Leaseautos, Contracten, Certificaten, Opmerkingen
from .forms import CreateUserForm


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
    return render(request, 'project1/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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
    return render(request,'project1/index.html',)


#class IndexView(generic.ListView):
#    model = Medewerkers
#    template_name = 'project1/index.html'

@login_required(login_url='login')
def MedewerkersPage(request):
    medewerkers = Medewerkers.objects.all()
    return render(request, 'project1/medewerkers.html', {'medewerkers': medewerkers})

#class MedewerkersView(generic.ListView):
#    template_name = 'project1/medewerkers.html'
#    context_object_name = 'alle_medewerkers'
#
#    def get_queryset(self):
#        return Medewerkers.objects.all()

@login_required(login_url='login')
def Detail(request,pk):
    medewerkers = Medewerkers.objects.get(id=pk)
    context = {'medewerkers': medewerkers}
    return render(request, 'project1/detail.html', context,)



#class DetailView(generic.DetailView):
#    model = Medewerkers
#    template_name = 'project1/detail.html'

#    class DetailView(generic.DetailView):
#        model = Opmerkingen
#        template_name = 'project1/detail.html'

@login_required(login_url='login')
def Leaseautosdetail(request,pk):
    leaseautos = Leaseautos.objects.get(id=pk)
    context = {'leaseautos':leaseautos,}
    return render(request, 'project1/lease.autos.detail.html', context,)


#class LeaseautosdetailView(generic.DetailView):
#    model = Leaseautos
#    template_name = 'project1/lease.autos.detail.html'

@login_required(login_url='login')
def Contractendetail(request,pk):
    contracten = Contracten.objects.get(id=pk)
    context = {'contracten':contracten,}
    return render(request, 'project1/contracten.detail.html', context,)


#class ContractenCertificatendetailView(generic.DetailView):
#    model = Contracten
#    template_name = 'project1/contracten.detail.html'

@login_required(login_url='login')
def Certificatendetail(request,pk):
    certificaten = Certificaten.objects.get(id=pk)
    context = {'certificaten':certificaten,}
    return render(request, 'project1/certificaten.detail.html', context,)

#class CertificatendetailView(generic.DetailView):
#    model = Certificaten
#    template_name = 'project1/certificaten.detail.html'


# class MedewerkersCreate(CreateView):
#     model = Medewerkers
#     fields = ['voornaam', 'tussenvoegsel', 'achternaam', 'bnsnummer', 'huisnummer', 'straat', 'woonplaats', 'postcode']
#
#     # displays blank form
#     def get(self, request, **kwargs):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
