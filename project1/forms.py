from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from .models import Opmerkingen


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OpmerkingenForm(ModelForm):
    class Meta:
        model = Opmerkingen
        fields = ['opmerkingveld', 'datum_opmerkingen']
        widgets = {
            'opmerkingveld': Textarea(attrs={'cols': 40, 'rows': 20}),
        }
