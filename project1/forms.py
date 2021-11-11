from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from .models import Foto
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['foto_medewerker', 'medewerkers']

