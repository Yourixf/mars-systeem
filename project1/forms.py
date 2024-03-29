# dit zijn de benodigde imports geweest voor die er nodig waren om de forms te maken.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.fields import DateField
# Haalt de models uit models.py
from .models import Medewerkers, Contracten, Eindklanten, Brokers, Certificaten, Aanbiedingen, \
    Opmerkingen
from django.forms.widgets import *
from django.contrib.admin import widgets
from datetime import *

from .models import *

# Dit is de forms.py template van Django hier kan je persoonlijke forms maken door middel van de in de class forms.Form te gebruiken kan je gepersonaliseerde forms maken.
# Ook is de mogelijkheid om ModelForm te gebruiken hier kan de de model aangeven "model = ...." dan pakt Django gelijk alle gegevens uit de specifieke Model class.
# Dan is er de mogelijkheid om aan te geven welke variable je in de forms wilt hebben "fields == ['blabla', blaadiebla]".
# Er is de mogelijk om te exclude te gebruiken dan pakt Django alle variable behalve die je aangeeft dit doe je zo "exclude = ('geslacht', 'naam')".
# In een ModelForm pakt maakt hij een standaard form van de Modelclass hierbij kijkt hij hoe je de variable hebt weggeschreven bijvoorbeeld een text veld, nummerveld enzv.
# Dit kan je aanpassen hier paar voorbeelden   bnsnummer = forms.IntegerField(),  zzper_eigenwerknemer = forms.ChoiceField(choices=EIGENWERKNEMER_CHOICES) Kijk maar even beneden voor nog meer voorbeelden.


# dit is de form om een nieuwe gebruiker aan te maken.
class CreateUserForm(UserCreationForm):
    # LopE3@fke
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Een keuze gebruiker een keuze laten maken door de de jou aangemaakte keuze's maak je zoals hier onder.
# zzper_eigenwerknemer = forms.ChoiceField(choices=EIGENWERKNEMER_CHOICES) Tussen de haakjes () verwijs je naar de gemaakte keuze's die je boven de forms zet.
EIGENWERKNEMER_CHOICES = (
    ("1", "Zzper"),
    ("2", "Eigenwerknemer"),

)
OPLEIDINGNIVEAU_CHOICES = (
    ("1", "Middelbaar beroepsonderwijs (MBO)"),
    ("2", "Hoger beroepsonderwijs (HBO)"),
    ("3", "Wetenschappelijk onderwijs (WO)"),

)

SOORT_RAPPORTAGE_CHOICES = (
    ('1', 'Gemiddeld tarief bij elke functie'),
    ('2', 'Totaal aantal aanbiedingen, intakes en plaatsingen per functie')
)

SOORT_DATUM_CHOICES = (
    ('1', forms.DateField(widget=SelectDateWidget)),
    ('2', forms.DateField(widget=SelectDateWidget)),
    ('3', forms.DateField(widget=SelectDateWidget)),
    ('4', forms.DateField(widget=SelectDateWidget)),
    ('5', forms.DateField(widget=SelectDateWidget)),
)

SOORT_WEERGAVE_CHOICES = (
    ('1', 'Pie chart'),
    ('2', 'Bar chart'),
    ('3', 'Tabel')
)

class WijzigingenDatumForm(forms.Form):
    aantalDagen = forms.IntegerField(initial=60, label='Wijzigingen van afgelopen aantal dagen')

class RapportageForm(forms.Form):
    soort_rapportage = forms.ChoiceField(widget=forms.RadioSelect, choices=SOORT_RAPPORTAGE_CHOICES)

    van_datum = forms.DateField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    tot_datum = forms.DateField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    soort_weergave = forms.ChoiceField(widget=forms.RadioSelect, choices=SOORT_WEERGAVE_CHOICES)

    #van_datum = forms.DateField(widget=forms.SelectDateWidget(attrs={'type':'date'}).year_field)



# Dit is de Form om medewerkers toe te voegen. In dit geval heb ik de input van de variable soms wat veranderd.
# de class Meta is zodat Django gaat zoeken naar de gewenste model.
class MedewerkersForm(forms.ModelForm):
    bsnnummer = forms.IntegerField(required=False, label='BSN nummer')
    #geboorte_datum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}), required=False)
    telefoonnummer = forms.CharField(max_length=20, required=True, label='Telefoonnummer *')
    #foto_medewerker = forms.FileField(required=False)
    voornaam = forms.CharField(required=False)
    achternaam = forms.CharField(required=True, label='Achternaam *')
    banknummer = forms.CharField(max_length=100, label='Rekeningnummer', required=False , widget= forms.TextInput
                           (attrs={'placeholder':'NL99 BANK 0123 4567 89'}))

    class Meta:
        model = Medewerkers
        fields = '__all__'
        exclude = ['begindatum']

        widgets = {
            'geboortedatum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type':'date'}),
            'datum_in_dienst': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}
            )
        }

        labels = {
            'status':'Status opdracht',
            'bv': 'BV',
            'ice_telefoonnummer':'ICE telefoonnummer',
            'ice_persoon_naam':'ICE persoon naam',
            'roepnaam':'Roepnaam *'
        }


# Dit is de Form om Contracten toe te voegen. In dit geval heb ik de input van de variable soms wat veranderd.
# de class Meta is zodat Django gaat zoeken naar de gewenste model.
# De fields  = [] definieer je de variabele die je in de form wilt hebben.
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


class ContactpersoonForm(forms.ModelForm):
    opmerkingen = forms.CharField(widget=forms.Textarea, max_length=300, required=False)
    #klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING, blank=True)
    #vestiging = models.ForeignKey(Vestigingplaats, on_delete=models.DO_NOTHING, blank=True)
    #begindatum = forms.DateField(required=False)
    class Meta:
        model = Contactpersonen
        fields = ['naam', 'mail_adres', 'telefoonnummer', 'functie']
        #exclude = ['klant', 'vestiging', 'begindatum']


class ContactpersoonUpdatenForm(forms.ModelForm):
    opmerkingen = forms.CharField(widget=forms.Textarea, max_length=300, required=False)
    class Meta:
        model = Contactpersonen
        fields = '__all__'
        exclude = ['begindatum', 'klant', 'vestiging']


class ContactVestigingForm(forms.ModelForm):

    class Meta:
        model = Vestigingplaats
        fields = '__all__'
        exclude = ['klant', 'broker', 'contactpersoon', 'begindatum']


class VestigingplaatsForm(forms.ModelForm):
    #vestiging = forms.CharField(max_length=20, required=False)
    postcode = forms.CharField(max_length=10, required=False)
    straatnaam = forms.CharField(max_length=30, required=False)
    huisnummer = forms.IntegerField(required=False)
    plaats = forms.CharField(max_length=20, required=False)
    klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING)
    opmerkingen = forms.CharField(widget=forms.Textarea ,max_length=300, required=False)

    class Meta:
        model = Vestigingplaats
        fields = '__all__'
        exclude = ['klant', 'broker', 'contactpersoon', 'begindatum']


# VOOR  NIEUWE KLANTEN TABEL ( EINDKLANTEN EN BROKER SAMENGEVOEGD)
class KlantenToevoegenForm(forms.ModelForm):

    class Meta:
        model = Klanten
        soort = forms.CharField(max_length=15, required=False)
        portaal_broker = forms.URLField(max_length=300)
        fields = '__all__'
        exclude = ['contactpersoon', 'vestiging', 'soort', 'begindatum']
        labels = {
            "accountmanager": "4-Rest contactpersoon",
            "factuuremail":"Email adres factuur",

        }

soortKlanten = (
    ("1", "Eindklant"),
    ("2", "Tussenpartij")
)

class KlantenUpdatenForm(forms.ModelForm):
    soort = forms.ChoiceField(choices=soortKlanten, required=False)
    class Meta:
        model = Klanten
        portaal_broker = forms.URLField(max_length=300)
        fields = '__all__'
        exclude = ['contactpersoon', 'vestiging', 'begindatum']
        labels = {
            "accountmanager": "4-Rest contactpersoon",
            "soort": "Soort klant",

        }

# Dit is de Form om Eindklanten toe te voegen. In dit geval heb ik de input van de variable soms wat veranderd.
# de class Meta is zodat Django gaat zoeken naar de gewenste model.
# Met de fields = '__all__' pakt Django alle variabele uit de model.
# Met de  exclude = [] zorg je ervoor dat Django deze niet mee pakt in de Form.
class EindklantenForm(forms.ModelForm):
    klantnaam = forms.CharField(max_length=50, required=False)
    telefoonnummer_klant = forms.CharField(max_length=17, required=False)
    portaal_klant = forms.URLField(max_length=300, required=False)
    class Meta:
        model = Eindklanten
        fields = ['accountmanager', 'klantnaam', 'telefoonnummer_klant', 'portaal_klant',]



# DIt is de form om brokers toe te voegen waarbij die alle variabele pakt uit de Brokers model.
class BrokersForm(forms.ModelForm):
    class Meta:
        portaal_broker = forms.URLField(max_length=300)
        model = Brokers
        fields = '__all__'
        exclude = ['vestiging', 'contactpersoon']
        labels = {
            "accountmanager": "4-Rest contactpersoon",
            "broker_naam": "Tussenpartij naam",
            "telefoonnummer_broker": "Telefoonnummer tussenpartij",
            "portaal_broker": "Portaal tussenpartij"
        }




# De Form om wijzigingen van de Contracten toe te voegen dit is precies de zelfde form als de ContractenToevoegen Form alleen dan voor de update.
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

# DIt is de form om Certificaten toe te voegen waarbij die alle variabele pakt uit de Certificaten model.
class CertificatenToevoegenForm(ModelForm):
    naam_certificaat = forms.CharField()
    datum_afronding = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    accreditatie_nummer = forms.IntegerField()
    naam_instituut = forms.CharField()

    class Meta:
        model = Certificaten
        fields = "__all__"


"""""
 Dit is de Form voor aanbiedingen hier heb ik weer gebruikt van de keuzevelden, en wat aanpassingen van de variabele in de Form.
    def __init__(self, *args, **kwargs):
        super(AanbiedingenToevoegenForm, self).__init__(*args, **kwargs)
       self.fields['broker'].required = False
 Dit is zodat Django begrijpt dat de broker gekozen moet worden uit eerder aangemaakte brokers.
"""""
ACCOUNTMANAGER_CHOICES = (
    ('1', 'Yoeri Tromp'),
    ('2', 'Nicky Slothouwer'),
    ('3', 'Coen Berkhout jr'),
    ('4', 'Jessica Berkhout'),
)


STATUS_AANBIEDING_CHOICES = (
    ('1', 'Open'),
    ('2', 'Intake'),
    ('3', 'Geplaatst'),
    ('4', 'Afgewezen'),
    ('5', 'Opdracht'),
    ('6', 'Verlopen'),
)

class AanbiedingenForm(forms.ModelForm):
    #aangemaakt_door = forms.ChoiceField(choices=ACCOUNTMANAGER_CHOICES, required=False)
    #registratie = forms.DateField(required=False)
    #laatste_update = forms.DateField(required=False)
    functie = forms.CharField(required=False)
    functie_aanbieding = forms.CharField(required=False)
    klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING, null=True, blank=True)
    broker = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING, null=True, blank=True)
    #accountmanager = forms.ChoiceField(choices=ACCOUNTMANAGER_CHOICES, required=False)
    status = forms.ChoiceField(required=False, choices=STATUS_AANBIEDING_CHOICES)
    tarief = forms.DecimalField(initial=00.00, required=False, max_value=200)
    betaalkorting = forms.DecimalField(initial=00.00, required=False)
    opmerking = forms.CharField(widget=forms.Textarea, max_length=600, required=False, label='Aanbieding opmerking')

    class Meta:
        model = Aanbiedingen
        fields = '__all__'
        exclude = ['begindatum', 'registratie', 'laatste_update',]

        labels = {
            "accountmanager": "4-Rest contactpersoon",
            "broker": "Tussenpartij",
            "medewerker":"Medewerker *",
        }
class AanbiedingUpdatenForm(forms.ModelForm):
    aangemaakt_door = forms.ChoiceField(choices=ACCOUNTMANAGER_CHOICES, required=False)
    #registratie = forms.CharField(required=False)
    #laatste_update = forms.CharField(required=False)
    functie = forms.CharField(required=False)
    functie_aanbieding = forms.CharField(required=False)
    klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING)
    #accountmanager = forms.ChoiceField(required=False, choices=ACCOUNTMANAGER_CHOICES)
    status = forms.ChoiceField(required=False, choices=STATUS_AANBIEDING_CHOICES)
    tarief = forms.DecimalField(initial=00.00, required=False)
    betaalkorting = forms.DecimalField(initial=00.00, required=False)
    medewerker = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING)
    opmerking = forms.CharField(widget=forms.Textarea, max_length=600, required=False, label='Aanbieding opmerking')
    registratie = forms.DateField(required=False, label='Registratiedatum', disabled=True)
    laatste_update = forms.DateField(required=False, label='Laatste update datum', disabled=True)

    class Meta:
        model = Aanbiedingen
        fields = '__all__'
        exclude = ['begindatum']

        labels = {
            "broker":"Tussenpartij",
            "accountmanager":"4-Rest contactpersoon",
            "klant":"Eindklant",
        }
class OpdrachtenForm(forms.ModelForm):
    aanbieding = models.ForeignKey(Aanbiedingen, on_delete=models.DO_NOTHING, blank=True)
    status_opdracht = forms.ChoiceField(choices=STATUS_OPDRACHT_CHOICES, required=False)
    tarief_opdracht = forms.FloatField(min_value=0, required=False)
    opdracht_betaalkorting = forms.FloatField(min_value=0, required=False)
    aantal_uren = forms.IntegerField(required=False, min_value=0, max_value=40)
    opmerking = forms.CharField(widget=forms.Textarea, max_length=600, required=False, label='Opdracht opmerking')

    date_created = forms.DateField(required=False, label='Registratiedatum', disabled=True)

    class Meta:
        model = Opdrachten
        fields = '__all__'
        exclude = ['aanbieding', 'begindatum']

        widgets = {
            'startdatum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}),
            'einddatum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}),
            'date_created': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'})
        }


class OpdrachtenToevoegenForm(forms.ModelForm):
    aanbieding = models.ForeignKey(Aanbiedingen, on_delete=models.DO_NOTHING)
    tarief_opdracht = forms.FloatField(min_value=0, required=False)
    opdracht_betaalkorting = forms.FloatField(min_value=0, required=False)
    aantal_uren = forms.IntegerField(required=False, min_value=0, max_value=40, initial=0)
    opmerking = forms.CharField(widget=forms.Textarea, max_length=600, required=False)

    class Meta:
        model = Opdrachten
        fields = '__all__'
        exclude = ['aanbieding', 'status_opdracht', 'opdracht_aangemaakt_door', 'date_created', 'begindatum']

        widgets = {
            'startdatum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}),
            'einddatum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'})
        }



# Dit is de Form om Documenten toe te voegen deze heb ik in de url en de instellingen laten verwijzen naar de static>images>static (onderaan het project).


class DocumentenForm(ModelForm):
    beschrijving = forms.CharField(widget=forms.Textarea, max_length=600, required=False)
    document = forms.FileField(required=True)
    class Meta:
        model = Documenten
        fields = ['naam_document', 'soort_document', 'beschrijving', 'document']
        exclude = ['begindatum']



class DocumentenUpdatenForm(ModelForm):
    beschrijving = forms.CharField(widget=forms.Textarea, max_length=600, required=False)

    class Meta:
        model = Documenten
        fields = ['naam_document', 'soort_document', 'beschrijving']
        exclude = ['begindatum']




class DocumentenHistoryForm(ModelForm):
    document = models.ForeignKey("Documenten", on_delete=models.DO_NOTHING, blank=True)
    update_id = forms.IntegerField(required=False)
    naam_document = forms.CharField(max_length=20, required=False)
    soort_document = forms.CharField(max_length=50, required=False)
    beschrijving = forms.CharField(widget=forms.Textarea, max_length=600, required=False)
    document_path = forms.FileField(required=False)
    medewerker = models.ForeignKey("Medewerkers", on_delete=models.DO_NOTHING, blank=True)
    updatedatum = forms.DateField(required=False)
    class Meta:
        model = Documenten_History
        fields = '__all__'
        exclude = ['updatedatum', 'update_id']

        widgets = {
            'updatedatum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'})
        }

class TaskItemCreateForm(forms.ModelForm):
    class Meta:
        model = Opmerkingen
        fields = ('title', 'body', 'due_date', 'category')


class TaskItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Opmerkingen
        fields = ('title', 'body', 'due_date', 'task_finished', 'category')