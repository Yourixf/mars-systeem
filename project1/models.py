# Bij alle tamplates die waar functies staan worden kan je dingen importen die je vervolgens kan gebruiken in je code die staan hier onder.
# "from djano.db import blablabla" (voorbeeld van hieronder)
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone, dateformat

# Dit is de Model template hier staan bepaalde classes in en daaronder staan variable onder neerzetten die je vervolgens in functies weer naar boven kan halen.
# Meest gebruikte zijn (models.)
# CharField = text veld.
# InterField = nummerveld.
# FloatField = nummerveld met comma.
# En nog nog meer "Fields", FileField, ImageField, URLField en nog meer zoek dit als je niet weet wat het in houdt op op google.
# verder kan je na je gekozen veld tussen de haakjes ook nog extra dingen weg schrijven, hoeveel het maximale tekens het mag bevatten. Of het veld leeg mag wezen. Waar je het naar toe wil laten uploaden. Keuzes die je de persoon wilt laten kiezen als er iets niet duidelijk is kopieer het en plak het in google.


# Dit is de Model van de medewerkers hier staan alle gegevens van de medewerkers.
# Weet je niet wat de models.Charfield betekend kopieer dit en zet er Django krijg je de omschrijving van waar dit voor bedoeld is.
LEASE_AUTO_CHOICES = (
    ('1', 'Ja'),
    ('2', 'All in'),
    ('3', 'Lease vergoeding'),
    ('4', 'Geen')
)

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
    ('69', 'Service Analist'), ('70', ' Service Co�rdinator'), ('71', 'Servicedesk Medewerker'),
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
STATUS_AANBIEDING_CHOICES = (
    ('1', 'Open'),
    ('2', 'Intake'),
    ('3', 'Geplaatst'),
    ('4', 'Afgewezen'),
    ('5', 'Opdracht'),
    ('6', 'Verlopen'),
)

STATUS_OPDRACHT_CHOICES = (
    ('1', 'Lopend'),
    ('2', 'Afgelopen'),
)

INHUUR_CHOICES = (
    ("1", "Ja"),
    ("2", "Nee"),

)
OPLEIDINGNIVEAU_CHOICES = (
    ("1", "Middelbaar beroepsonderwijs (MBO)"),
    ("2", "Hoger beroepsonderwijs (HBO)"),
    ("3", "Wetenschappelijk onderwijs (WO)"),

)

STATUS_MEDEWERKER_CHOICES = (
    ('1', 'Intake'),
    ('2', 'Opdracht'),
    ('3', 'Leegloop'),
    ('4', 'Uit dienst'),
)

BV_CHOICES = (
    ('1', 'Holding'),
    ('2', 'Ict'),
    ('3', 'Infra'),
    ('4', 'III'),
    ('5', 'Extern')
)

BURGERLIJKE_STAAT_CHOICES = (
    ('1', ''),
    ('2', ''),
    ('3', ''),
    ('4', ''),

)

class Medewerkers(models.Model):
    voornaam = models.CharField(max_length=100, blank=True)  # max_length=... is bedoeld voor hoeveel tekens het maximaal mag bevatten.
    tussenvoegsel = models.CharField(max_length=6, blank=True)  # blank=True betekend dat het veld leeg mag zijn ( bij Charfield )
    achternaam = models.CharField(max_length=100, blank=True)
    bnsnummer = models.IntegerField(null=True, blank=True)  # null=True betekend dat het veld leeg mag zijn ( bij IntegerField )
    huisnummer = models.CharField(max_length=20, blank=True)
    straat = models.CharField(max_length=150, blank=True)
    woonplaats = models.CharField(max_length=150, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    telefoonnummer = models.CharField(null=True, max_length=20, blank=True)
    icenummer = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    tariefindicatie = models.FloatField(max_length=20, blank=True)
    inhuur = models.CharField(choices=INHUUR_CHOICES, max_length=50, blank=True)
    opleidingsniveau = models.CharField(choices=OPLEIDINGNIVEAU_CHOICES,max_length=50, blank=True)
    burgerlijkse_staat = models.CharField(max_length=100, blank=True)
    geboortedatum = models.DateField(null=True, blank=True)
    foto_medewerker = models.FileField(upload_to='images/', default='userimg.png')  # de default foto voor de medewerkers.
    cv = models.FileField(upload_to='static/', null=True, blank=True)  # upload to upload het naar de static files
    beschrijving = models.CharField(max_length=50, null=True, blank=True)
    feedback = models.FileField(upload_to='static/', null=True, blank=True)
    soort_document = models.CharField(max_length=50, null=True, blank=True)
    documenten = models.FileField(upload_to='static/', null=True, blank=True)
    titel_documenten = models.CharField(max_length=50, null=True, blank=True)
    lease_auto = models.CharField(max_length=15, choices=LEASE_AUTO_CHOICES, null=True, blank=True)
    status = models.CharField(choices=STATUS_MEDEWERKER_CHOICES, max_length=50, blank=True)
    bv = models.CharField(choices=BV_CHOICES, blank=True, max_length=50)

    def get_absolut_url(self):
        return reverse('project1:detail', kwargs={
            'pk': self.pk})  # dit is voor de details dat elke medewerker zijn eigen detail pagina krijgt met pk

    def __str__(self):
        return self.voornaam + " " + self.tussenvoegsel + " " + self.achternaam  # de Self voegt deze 3 variabele bij elkaar die je samen kan ophalen.


class Opmerkingen(models.Model):
    DEFAULT = 'DEFAULT'
    MEDEWERKERS = 'MEDEWERKERS'
    EINDKLANTEN = 'EINDKLANTEN'
    BROKERS = 'BROKERS'
    CATEGORIES = (  # de keuze voor de categorieen.
        (DEFAULT, DEFAULT),
        (MEDEWERKERS, MEDEWERKERS),
        (EINDKLANTEN, EINDKLANTEN),
        (BROKERS, BROKERS),
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(
        default=timezone.now)  # timezone.now vult standaard de tijd waarin je de form opent.
    task_finished = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=CATEGORIES,
                                default=DEFAULT)  # haalt de keuze van de CATEGORIES op.

    def __str__(self):
        return f'{self.title}'


class Contracten(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING)  # door de ForeignKey in te vullen van de medewerker is het contract gelinkt met de medewerker.
    contract_uren = models.IntegerField(null=True)
    Startdatum = models.DateField(null=True)
    Einddatum = models.DateField(null=True)
    functie_contract = models.CharField(max_length=100)
    salaris = models.FloatField(max_length=20)
    vakantie_dagen = models.IntegerField(null=True)
    Onkostenvergoeding = models.FloatField(max_length=20)


class Certificaten(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING)  # door de ForeignKey in te vullen van de medewerker is de certificaat gelinkt met de medewerker.
    naam_certificaat = models.CharField(max_length=100)
    datum_afronding = models.DateField(null=True)
    accreditatie_nummer = models.CharField(max_length=100)
    naam_instituut = models.CharField(max_length=100)


class Eindklanten(models.Model):
    accountmanager = models.CharField(max_length=5, choices=ACCOUNTMANAGER_CHOICES, null=True, blank=True)
    klantnaam = models.CharField(max_length=50, null=True, blank=True)
    telefoonnummer_klant = models.CharField(max_length=17, null=True, blank=True)
    portaal_klant = models.URLField(max_length=300, null=True, blank=True)
    contactpersoon = models.ForeignKey("Contactpersonen", on_delete=models.DO_NOTHING, blank=True)
    vestiging = models.ForeignKey("Vestigingplaats", on_delete=models.DO_NOTHING, blank=True)


    def get_absolut_url(self):
        return reverse('project1:eindklanten.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.klantnaam


class Brokers(models.Model):
    accountmanager = models.CharField(max_length=4, choices=ACCOUNTMANAGER_CHOICES, blank=True)
    broker_naam = models.CharField(max_length=50, blank=True)
    telefoonnummer_broker = models.CharField(null=True, max_length=20, blank=True)
    portaal_broker = models.URLField(max_length=300, null=True, blank=True)
    vestiging = models.ForeignKey("Vestigingplaats", on_delete=models.DO_NOTHING, blank=True)
    contactpersoon = models.ForeignKey("Contactpersonen", on_delete=models.DO_NOTHING, blank=True)
    vestiging = models.ForeignKey("Vestigingplaats", on_delete=models.DO_NOTHING, blank=True)

    def get_absolut_url(self):
        return reverse('project1:broker.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.broker_naam


class Vestigingplaats(models.Model):
    vestiging = models.CharField(max_length=20, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    straatnaam = models.CharField(max_length=30, blank=True)
    huisnummer = models.IntegerField(blank=True)
    plaats = models.CharField(max_length=20, blank=True)
    klant = models.ForeignKey(Eindklanten, on_delete=models.DO_NOTHING, blank=True)
    broker = models.ForeignKey(Brokers, on_delete=models.DO_NOTHING, blank=True)
    contactpersoon = models.ForeignKey("Contactpersonen", on_delete=models.DO_NOTHING, blank=True)
    opmerkingen = models.CharField(max_length=300, blank=True)


class Contactpersonen(models.Model):
    naam = models.CharField(max_length=50, blank=True)
    mail_adres = models.CharField(max_length=50, blank=True)
    telefoonnummer = models.CharField(max_length=30, blank=True)
    functie = models.CharField(max_length=50, blank=True)
    klant = models.ForeignKey(Eindklanten, on_delete=models.DO_NOTHING, blank=True)
    broker = models.ForeignKey(Brokers, on_delete=models.DO_NOTHING, blank=True)
    vestiging = models.ForeignKey(Vestigingplaats, on_delete=models.DO_NOTHING, blank=True)
    opmerkingen = models.CharField(max_length=300, blank=True)

class Aanbiedingen(models.Model):
    aangemaakt_door = models.CharField(max_length=50, choices=ACCOUNTMANAGER_CHOICES, blank=True)
    registratie = models.DateField(null=True, blank=True)
    laatste_update = models.DateField(null=True, blank=True)
    functie = models.CharField(max_length=50, choices=FUNCTIE_CHOICES)
    functie_aanbieding = models.CharField(max_length=50)
    klant = models.ForeignKey(Eindklanten, on_delete=models.DO_NOTHING, blank=True)
    broker = models.ForeignKey(Brokers, on_delete=models.DO_NOTHING, blank=True)
    accountmanager = models.CharField(max_length=4, choices=ACCOUNTMANAGER_CHOICES, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_AANBIEDING_CHOICES)
    tarief = models.FloatField(max_length=14, default=True, null=True)
    betaalkorting = models.FloatField(max_length=14, default=True, null=True)
    medewerker = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING, blank=False)

    def get_status_count(self):
        return Aanbiedingen.objects.all().filter(status='1').count()


class Opdrachten(models.Model):
    aanbieding = models.ForeignKey(Aanbiedingen, on_delete=models.DO_NOTHING, blank=True)
    status_opdracht = models.CharField(max_length=50, choices=STATUS_OPDRACHT_CHOICES)
    startdatum = models.DateField(null=True, blank=True)
    einddatum = models.DateField(null=True, blank=True)
    tarief_opdracht = models.FloatField(default=True, blank=True)
    opdracht_betaalkorting = models.FloatField(default=True, null=True, blank=True)
    aantal_uren = models.IntegerField(blank=True)
    opdracht_aangemaakt_door = models.CharField(max_length=4, choices=ACCOUNTMANAGER_CHOICES, blank=True)
    date_created = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))

    def get_status_count(self):
        return Opdrachten.objects.all().filter(status='1').count()

