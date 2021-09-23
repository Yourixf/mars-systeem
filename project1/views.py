from django.views import generic
from .models import Medewerkers, Leaseautos
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.decorators import login_required
# @login_required(login_url='/login/')
# def my_view(request):


class MedewerkersView(generic.ListView):
    template_name = 'project1/medewerkers.html'
    context_object_name = 'alle_medewerkers'

    def get_queryset(self):
        return Medewerkers.objects.all()

class DetailView(generic.DetailView):
    model = Medewerkers
    template_name = 'project1/detail.html'

class LeaseautosdetailView(generic.DetailView):
    context_object_name = 'alle_leaseautos'
    template_name = 'project1/lease.autos.detail.html'

class IndexView(generic.ListView):
    model = Medewerkers
    template_name = 'project1/index.html'


class MedewerkersCreate(CreateView):
    model = Medewerkers
    fields = ['voornaam', 'tussenvoegsel', 'achternaam', 'bnsnummer', 'huisnummer', 'straat', 'woonplaats', 'postcode']

class UserFormView(View):
    form_class = UserForm
    template_name = 'project1/register.html'

    #displays blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            gebruiker = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('project1:index')

        return render(request, self.template_name, {'form': form})


def home(request):
    return render(request, "project1/home.html")



def login(request):
    return render(request, "project1/login.html")









