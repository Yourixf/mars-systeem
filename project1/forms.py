# dit zijn de benodigde imports geweest voor die er nodig waren om de forms te maken.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.fields import DateField
# Haalt de models uit models.py
from .models import Medewerkers, Contracten, Eindklanten, Brokers, Certificaten, Leaseautos, Aanbiedingen, \
    Opmerkingen

from .models import *

# Dit is de forms.py template van Django hier kan je persoonlijke forms maken door middel van de in de class forms.Form te gebruiken kan je gepersonaliseerde forms maken.
# Ook is de mogelijkheid om ModelForm te gebruiken hier kan de de model aangeven "model = ...." dan pakt Django gelijk alle gegevens uit de specifieke Model class.
# Dan is er de mogelijkheid om aan te geven welke variable je in de forms wilt hebben "fields == ['blabla', blaadiebla]".
# Er is de mogelijk om te exclude te gebruiken dan pakt Django alle variable behalve die je aangeeft dit doe je zo "exclude = ('geslacht', 'naam')".
# In een ModelForm pakt maakt hij een standaard form van de Modelclass hierbij kijkt hij hoe je de variable hebt weggeschreven bijvoorbeeld een text veld, nummerveld enzv.
# Dit kan je aanpassen hier paar voorbeelden   bnsnummer = forms.IntegerField(),  zzper_eigenwerknemer = forms.ChoiceField(choices=EIGENWERKNEMER_CHOICES) Kijk maar even beneden voor nog meer voorbeelden.


# dit is de form om een nieuwe gebruiker aan te maken.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Een form voor alleen de  "foto_medewerker" variabele uit de Mederwerkers Model.
class FotoForm(ModelForm):
    class Meta:
        model = Medewerkers
        fields = ['foto_medewerker']


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


# Dit is de Form om medewerkers toe te voegen. In dit geval heb ik de input van de variable soms wat veranderd.
# de class Meta is zodat Django gaat zoeken naar de gewenste model.
class MedewerkersToevoegenForm(forms.ModelForm):
    class Meta:
        model = Medewerkers
        fields = '__all__'
        exclude = ('document', "cv", 'title_cv', 'feedback', 'title_feedback', 'documenten', 'title_documenten')


# De Form om wijzigingen van de medewerkers toe te voegen dit is precies de zelfde form als de medewerkerstoevoegen Form alleen dan voor de update.
class MedewerkersUpdateForm(ModelForm):
    bnsnummer = forms.IntegerField()
    geboorte_datum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    email = forms.EmailField(max_length=254)
    telefoonnummer = forms.CharField(max_length=20)
    icenummer = forms.IntegerField()
    teriefindicatie = forms.FloatField()
    zzper_eigenwerknemer = forms.ChoiceField(choices=EIGENWERKNEMER_CHOICES)
    opleidings_niveau = forms.ChoiceField(choices=OPLEIDINGNIVEAU_CHOICES)

    class Meta:
        model = Medewerkers
        fields = ['cv', 'title_cv', 'feedback', 'title_feedback', 'title_documenten']
        #exclude = ('document', 'cv', 'title_cv', 'feedback', 'title_feedback', 'documenten', 'title_documenten')
        widgets = {
            'geboorte_datum': DateField(),

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


# Dit is de Form om Eindklanten toe te voegen. In dit geval heb ik de input van de variable soms wat veranderd.
# de class Meta is zodat Django gaat zoeken naar de gewenste model.
# Met de fields = '__all__' pakt Django alle variabele uit de model.
# Met de  exclude = [] zorg je ervoor dat Django deze niet mee pakt in de Form.
class EindklantenToevoegenForm(forms.ModelForm):
    class Meta:
        model = Eindklanten
        fields = '__all__'
        exclude = ['opmerking_title', 'opmerking_intro', 'opmerking_body', 'opmerking_date_added']


# De Form om wijzigingen van de Eindklanten toe te voegen dit is precies de zelfde form als de Eindklanten Form alleen dan voor de update.
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

# De Form om wijzigingen van de Brokers toe te voegen dit is precies de zelfde form als de Brokers Form alleen dan voor de update.
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
        model = Brokers
        fields = '__all__'
        exclude = ['opm_title', 'opm_intro', 'opm_body', 'opm_date_added']

# DIt is de form om brokers toe te voegen waarbij die alle variabele pakt uit de Brokers model.
class BrokersToevoegenForm(forms.ModelForm):
    class Meta:
        portaal_broker = forms.URLField(max_length=300)
        model = Brokers
        fields = '__all__'

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

# Dit is de Form om Leaseauto's toe te voegen. In dit geval heb ik de input van de variable soms wat veranderd.
class LeaseautosToevoegenForm(forms.ModelForm):
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

"""""
 Dit is de Form voor aanbiedingen hier heb ik weer gebruikt van de keuzevelden, en wat aanpassingen van de variabele in de Form.
    def __init__(self, *args, **kwargs):
        super(AanbiedingenToevoegenForm, self).__init__(*args, **kwargs)
       self.fields['broker'].required = False
 Dit is zodat Django begrijpt dat de broker gekozen moet worden uit eerder aangemaakte brokers.
"""""

class AanbiedingenToevoegenForm(ModelForm):


    aangemaakt_door = forms.ModelChoiceField(queryset=Medewerkers.objects.all(), required=False)
    registratie = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}), required=False)
    laatste_update = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}), required=False)
    tarief = forms.DecimalField(initial=00.00, required=False)
    betaalkorting = forms.DecimalField(initial=00.00, required=False)
    medewerker = forms.ModelChoiceField(queryset=Medewerkers.objects.all(), required=False)
    functie = forms.ChoiceField(required=False)
    functie_aanbieding = forms.CharField(required=False)
    status = forms.ChoiceField(required=False)
    klant_naam = forms.ModelChoiceField(queryset=Eindklanten.objects.all(), required=False)
    broker = forms.ModelChoiceField(queryset=Eindklanten.objects.all(), blank=True, required=False)
    accountmanager = forms.CharField(required=False)
    class Meta:
        model = Aanbiedingen
        fields = '__all__'

# Dit is de Form om Cv's toe te voegen deze heb ik in de url en de instellingen laten verwijzen naar de static>images>static (onderaan het project).
class CvUploadForm(ModelForm):
    class Meta:
        model = Medewerkers
        fields = ['title_cv', 'cv']

# Dit is de Form om Feedback's toe te voegen deze heb ik in de url en de instellingen laten verwijzen naar de static>images>static (onderaan het project).
class FeedbackUploadForm(ModelForm):
    class Meta:
        model = Medewerkers
        fields = ['title_feedback', 'feedback']

# Dit is de Form om Documenten toe te voegen deze heb ik in de url en de instellingen laten verwijzen naar de static>images>static (onderaan het project).
class DocumentenUploadForm(ModelForm):
    class Meta:
        model = Medewerkers
        fields = ['title_documenten', 'documenten']


class TaskItemCreateForm(forms.ModelForm):
    class Meta:
        model = Opmerkingen
        fields = ('title', 'body', 'due_date', 'category')


class TaskItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Opmerkingen
        fields = ('title', 'body', 'due_date', 'task_finished', 'category')