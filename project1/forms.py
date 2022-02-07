from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.fields import DateField

from .models import Medewerkers, Contracten, Eindklanten, Brokers, Certificaten, Leaseautos


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FotoForm(ModelForm):
    class Meta:
        model = Medewerkers
        fields = ['foto_medewerker']


EIGENWERKNEMER_CHOICES = (
    ("1", "Zzper"),
    ("2", "Eigenwerknemer"),

)
OPLEIDINGNIVEAU_CHOICES = (
    ("1", "Middelbaar beroepsonderwijs (MBO)"),
    ("2", "Hoger beroepsonderwijs (HBO)"),
    ("3", "Wetenschappelijk onderwijs (WO)"),

)


class MedewerkersToevoegenForm(forms.ModelForm):
    bnsnummer = forms.IntegerField()
    geboorte_datum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    email = forms.EmailField(max_length=254)
    mobielnummer = forms.IntegerField()
    icenummer = forms.IntegerField()
    teriefindicatie = forms.FloatField()
    zzper_eigenwerknemer = forms.ChoiceField(choices=EIGENWERKNEMER_CHOICES)
    opleidings_niveau = forms.ChoiceField(choices=OPLEIDINGNIVEAU_CHOICES)

    class Meta:
        model = Medewerkers
        fields = '__all__'


class MedewerkersUpdateForm(ModelForm):
    bnsnummer = forms.IntegerField()
    geboorte_datum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    email = forms.EmailField(max_length=254)
    mobielnummer = forms.IntegerField()
    icenummer = forms.IntegerField()
    teriefindicatie = forms.FloatField()
    zzper_eigenwerknemer = forms.ChoiceField(choices=EIGENWERKNEMER_CHOICES)
    opleidings_niveau = forms.ChoiceField(choices=OPLEIDINGNIVEAU_CHOICES)

    class Meta:
        model = Medewerkers
        fields = '__all__'
        widgets = {
            'geboorte_datum': DateField(),

        }


class ContractenToevoegenForm(ModelForm):
    contract_uren = forms.IntegerField()
    salaris = forms.IntegerField()
    vakantie_dagen = forms.IntegerField()
    Onkostenvergoeding = forms.IntegerField()
    Startdatum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    Einddatum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    class Meta:
        model = Contracten
        fields = ['contract_uren', 'Startdatum', 'Einddatum', 'functie_contract', 'salaris', 'vakantie_dagen',
                  'Onkostenvergoeding']


class EindklantenToevoegenForm(forms.ModelForm):
    class Meta:
        model = Eindklanten
        fields = '__all__'


class EindklantenUpdateForm(forms.ModelForm):
    ACCOUNTMANAGER_CHOICES = (
        ('1', 'Yoeri Tromp'),
        ('2', 'Nicky Slothouwer'),
        ('3', 'Coen Berkhout jr'),
        ('4', 'Jessica Berkhout'),
    )
    accountmanager = forms.ChoiceField(choices=ACCOUNTMANAGER_CHOICES)
    klantnaam = forms.CharField(max_length=50)
    straat_klant = forms.CharField(max_length=150)
    huisnummer_klant = forms.CharField(max_length=20)
    postcode_klant = forms.CharField(max_length=10)
    vestigingplaats_klant = forms.CharField(max_length=150)
    telefoonnummer_klant = forms.CharField(max_length=17)
    portaal_klant = forms.URLField(max_length=300)

    class BrokersUpdateForm(forms.ModelForm):
        ACCOUNTMANAGER_CHOICES = (
            ('1', 'Yoeri Tromp'),
            ('2', 'Nicky Slothouwer'),
            ('3', 'Coen Berkhout jr'),
            ('4', 'Jessica Berkhout'),
        )
        accountmanager = forms.ChoiceField(choices=ACCOUNTMANAGER_CHOICES)
        klantnaam = forms.CharField(max_length=50)
        straat_klant = forms.CharField(max_length=150)
        huisnummer_klant = forms.CharField(max_length=20)
        postcode_klant = forms.CharField(max_length=10)
        vestigingplaats_klant = forms.CharField(max_length=150)
        telefoonnummer_klant = forms.CharField(max_length=17)
        portaal_klant = forms.URLField(max_length=300)

    class Meta:
        model = Eindklanten
        fields = '__all__'


class BrokersToevoegenForm(forms.ModelForm):
    class Meta:
        model = Brokers
        fields = '__all__'

class ContractenUpdateForm(ModelForm):
    contract_uren = forms.IntegerField()
    salaris = forms.IntegerField()
    vakantie_dagen = forms.IntegerField()
    Onkostenvergoeding = forms.IntegerField()
    Startdatum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    Einddatum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    class Meta:
        model = Contracten
        fields = ['contract_uren', 'Startdatum', 'Einddatum', 'functie_contract', 'salaris', 'vakantie_dagen',
                  'Onkostenvergoeding']

class CertificatenToevoegenForm(ModelForm):
    naam_certificaat = forms.CharField()
    datum_afronding = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    accreditatie_nummer = forms.IntegerField()
    naam_instituut = forms.CharField()

    class Meta:
        model = Certificaten
        fields = "__all__"

class LeaseautosToevoegenForm(ModelForm):
    kenteken = forms.CharField()
    start_datum_lease_auto = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    eind_datum_lease_auto = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    merk_auto = forms.CharField()
    type_auto = forms.CharField()
    leasemaatschappij = forms.CharField()
    kilometer_per_jaar = forms.IntegerField()
    lease_bedrag = forms.FloatField()

class Meta:
    model = Leaseautos
    fields = "__all__"
