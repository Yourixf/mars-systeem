# dit zijn de benodigde imports geweest voor die er nodig waren om de forms te maken.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.fields import DateField
# Haalt de models uit models.py
from .models import Medewerkers, Contracten, Eindklanten, Brokers, Certificaten, Aanbiedingen, \
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
class MedewerkersForm(forms.ModelForm):
    bnsnummer = forms.IntegerField(required=False)
    #geboorte_datum = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}), required=False)
    email = forms.EmailField(max_length=254, required=False)
    telefoonnummer = forms.CharField(max_length=20, required=False)
    icenummer = forms.IntegerField(required=False)
    #foto_medewerker = forms.FileField(required=False)

    class Meta:
        model = Medewerkers
        fields = '__all__'
        exclude = ('document', "cv", 'title_cv', 'feedback', 'title_feedback', 'documenten', 'title_documenten', 'foto_medewerker')

        widgets = {
            'geboorte_datum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type':'date'}),
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


class VestigingplaatsForm(forms.ModelForm):
    soort_vestiging = forms.CharField(max_length=20, required=False)
    postcode = forms.CharField(max_length=10, required=False)
    straatnaam = forms.CharField(max_length=30, required=False)
    huisnummer = forms.IntegerField(required=False)
    plaats = forms.CharField(max_length=20, required=False)
    klant = models.ForeignKey(Eindklanten, on_delete=models.DO_NOTHING)
    broker = models.ForeignKey(Brokers, on_delete=models.DO_NOTHING)

    class Meta:
        model = Vestigingplaats
        fields = '__all__'
        exclude = ['klant', 'broker']


# Dit is de Form om Eindklanten toe te voegen. In dit geval heb ik de input van de variable soms wat veranderd.
# de class Meta is zodat Django gaat zoeken naar de gewenste model.
# Met de fields = '__all__' pakt Django alle variabele uit de model.
# Met de  exclude = [] zorg je ervoor dat Django deze niet mee pakt in de Form.
class EindklantenForm(forms.ModelForm):

    klantnaam = forms.CharField(max_length=50, required=False)
    telefoonnummer_klant = forms.CharField(max_length=17, required=False)
    portaal_klant = forms.URLField(max_length=300, required=False)
    #vestigingSoort = forms.ModelChoiceField(queryset=Vestigingplaats.objects.get(Vestigingplaats.soort))
    class Meta:
        model = Eindklanten
        fields = ['accountmanager', 'klantnaam', 'telefoonnummer_klant', 'portaal_klant',]
        #exclude = ('straat_klant', 'plaats_klant', 'postcode_klant', 'huisnummer_klant', 'opmerking_title', 'opmerking_intro', 'opmerking_body', 'opmerking_date_added',)



# DIt is de form om brokers toe te voegen waarbij die alle variabele pakt uit de Brokers model.
class BrokersForm(forms.ModelForm):
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
FUNCTIE_CHOICES = (
    ('1', '.NET Developer'), ('3', ' 3D - tekenaar'), ('4', ' Android Developer '), ('5', ' App Developer'),
    ('6', 'Applicatie Specialist'), ('7', ' Applicatiebeheerder'), ('8', 'Applicatieontwerper'),
    ('9', 'Applicatieontwerper'),
    ('10', 'Applicatieontwikkelaar'), ('11', 'Application Designer'), ('12', 'Assistent filiaalmanager '),
    ('13', 'Backend Developer'),
    ('14', 'Beleidsmedewerker Informatiebeveiliging'), ('15', 'Business Analist'), ('16', 'Business Architect '),
    ('17', 'Citrix Specialist'),
    ('18', 'Commercieel Directeur'), ('19', 'Content Manager'), ('20', 'Contractmanager '),
    ('21', 'Data - analist'),
    ('22', 'Database Administrator'), ('23', 'Directeur ICT'), ('24', 'Directeur IT '), ('25', 'Embedded Engineer'),
    ('26', 'Filiaalmanager'), ('27', 'Functioneel Beheerder'), ('28', 'Hacker '), ('29', 'Hardware Engineer'),
    ('30', 'Helpdeskmedewerker'), ('31', ' HTML Specialist'), ('32', 'Applicatieontwerper'),
    ('33', 'ICT Specialist'), ('34', ' ICT Supportmedewerker'), ('35', 'Informatieanalist'),
    ('36', 'Informatiemanager'),
    ('37', 'Infrastructuur Ontwerper'), ('38', ' Infrastructuur Specialist'), ('39', 'iOS Developer'),
    ('40', 'Architect'),
    ('41', 'IT Auditor'), ('42', ' IT Trainee'), ('43', 'JAVA Developer'), ('44', 'Junior Pega Developer'),
    ('45', 'Leraar Informatica'), ('46', ' Management Consultant'), ('47', 'Netwerk Engineer'),
    ('48', 'Netwerkbeheerder'),
    ('49', 'Netwerkmanager'), ('50', ' Netwerkspecialist'), ('51', 'Operations Manager'), ('52', 'PHP Developer'),
    ('53', 'PHP Programmeur'), ('54', ' PLC Engineer'), ('55', 'PLC Programmeur'), ('56', 'Procesmanager'),
    ('57', 'Processpecialist'), ('58', ' Programmeur'), ('59', 'Projectcontroller'), ('60', 'Projectmanager IT'),
    ('61', 'ApplicatieSpecialist'), ('62', ' Applicatiebeheerder'), ('63', 'Applicatieontwerper'),
    ('64', 'Requirements Analist'),
    ('65', 'Sales Analist'), ('66', ' Sales Manager'), ('67', 'Scrum Master'), ('68', 'SEO specialist'),
    ('69', 'Service Analist'), ('70', ' Service Coördinator'), ('71', 'Servicedesk Medewerker'),
    ('71', 'Shopmanager'),
    ('72', 'Software designer'), ('73', ' Software Engineer'), ('74', 'Software tester'),
    ('75', 'Supportmedewerker'),
    ('76', 'Systeemarchitect'), ('77', ' Systeembeheerder'), ('78', 'Systeemontwerper'),
    ('79', 'Systeemontwikkelaar'),
    ('80', 'Systeemoperator'), ('81', ' Systeemspecialist'), ('82', 'System Engineer'),
    ('83', 'Technical support engineer'),
    ('84', 'Technisch adviseur'), ('85', ' Technisch Ontwerper'), ('86', 'Telecom Engineer'),
    ('87', 'Telecommunicatiemanager'),
    ('88', 'Test Engineer'), ('89', ' Testanalist'), ('90', 'Testconsultant'), ('91', 'Tester'),
    ('92', 'Testmanager'), ('93', ' Webdeveloper'), ('94', 'Webmaster'), ('95', 'Servicemanager'),
    ('96', 'Packager'),

)
STATUS_CHOICES1 = (
    ('1', 'Open'),
    ('2', 'Geselecteerd'),
    ('3', 'Intake'),
    ('4', 'Geplaatst'),
    ('5', 'Afgewezen'),
)

STATUS_CHOICES2 = (
    ('1', 'Open'),
    ('2', 'Geselecteerd'),
    ('3', 'Intake'),
    ('4', 'Geplaatst'),
    ('5', 'Afgewezen'),
    ('6', 'Opdracht'),
    ('7', 'Verlopen'),
)

class AanbiedingenForm(forms.ModelForm):
    functie = forms.ChoiceField(required=False, choices=FUNCTIE_CHOICES)
    functie_aanbieding = forms.CharField(required=False)
    klant = models.ForeignKey(Eindklanten, on_delete=models.DO_NOTHING)
    broker = models.ForeignKey(Brokers, on_delete=models.DO_NOTHING)
    status = forms.ChoiceField(required=False, choices=STATUS_CHOICES2)
    tarief = forms.DecimalField(initial=00.00, required=False)
    betaalkorting = forms.DecimalField(initial=00.00, required=False)
    medewerker = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING)

    class Meta:
        model = Aanbiedingen
        fields = '__all__'

        widgets = {
            'registratie': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}),
            'laatste_update': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}),

        }
class AanbiedingUpdatenForm(forms.ModelForm):
    aangemaakt_door = forms.ChoiceField(choices=ACCOUNTMANAGER_CHOICES, required=False)
    #registratie = forms.CharField(required=False)
    #laatste_update = forms.CharField(required=False)
    functie = forms.ChoiceField(required=False, choices=FUNCTIE_CHOICES)
    functie_aanbieding = forms.CharField(required=False)
    klant = models.ForeignKey(Eindklanten, on_delete=models.DO_NOTHING)
    broker = models.ForeignKey(Brokers, on_delete=models.DO_NOTHING)
    accountmanager = forms.ChoiceField(required=False, choices=ACCOUNTMANAGER_CHOICES)
    status = forms.ChoiceField(required=False, choices=STATUS_CHOICES2)
    tarief = forms.DecimalField(initial=00.00, required=False)
    betaalkorting = forms.DecimalField(initial=00.00, required=False)
    medewerker = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING)

    class Meta:
        model = Aanbiedingen
        fields = '__all__'

        widgets = {
            'registratie': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}),
            'laatste_update': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}),

        }
class OpdrachtenForm(forms.ModelForm):
    aanbieding = models.ForeignKey(Aanbiedingen, on_delete=models.DO_NOTHING, blank=True)
    status_opdracht = forms.ChoiceField(choices=STATUS_OPDRACHT_CHOICES, required=False)
    tarief_opdracht = forms.FloatField(required=False)
    opdracht_betaalkorting = forms.FloatField(required=False)
    aantal_uren = forms.IntegerField(required=False)
    class Meta:
        model = Opdrachten
        fields = '__all__'

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
    tarief_opdracht = forms.FloatField(required=False)
    class Meta:
        model = Opdrachten
        fields = '__all__'
        exclude = ['aanbieding', 'status_opdracht', 'opdracht_aangemaakt_door', 'date_created',]

        widgets = {
            'startdatum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}),
            'einddatum': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'})
        }

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