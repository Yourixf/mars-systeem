# Bij alle tamplates die waar functies staan worden kan je dingen importen die je vervolgens kan gebruiken in je code die staan hier onder.
# "from djano.db import blablabla" (voorbeeld van hieronder)
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Dit is de Model template hier staan bepaalde classes in en daaronder staan variable onder neerzetten die je vervolgens in functies weer naar boven kan halen.
# Meest gebruikte zijn (models.)
# CharField = text veld.
# InterField = nummerveld.
# FloatField = nummerveld met comma.
# En nog nog meer "Fields", FileField, ImageField, URLField en nog meer zoek dit als je niet weet wat het in houdt op op google.
# verder kan je na je gekozen veld tussen de haakjes ook nog extra dingen weg schrijven, hoeveel het maximale tekens het mag bevatten. Of het veld leeg mag wezen. Waar je het naar toe wil laten uploaden. Keuzes die je de persoon wilt laten kiezen als er iets niet duidelijk is kopieer het en plak het in google.


# Dit is de Model van de medewerkers hier staan alle gegevens van de medewerkers.
# Weet je niet wat de models.Charfield betekend kopieer dit en zet er Django krijg je de omschrijving van waar dit voor bedoeld is.
class Medewerkers(models.Model):
    voornaam = models.CharField(max_length=100)#max_length=... is bedoeld voor hoeveel tekens het maximaal mag bevatten.
    tussenvoegsel = models.CharField(max_length=6, blank=True) #blank=True betekend dat het veld leeg mag zijn ( bij Charfield )
    achternaam = models.CharField(max_length=100)
    bnsnummer = models.IntegerField(null=True)# null=True betekend dat het veld leeg mag zijn ( bij IntegerField )
    huisnummer = models.CharField(max_length=20)
    straat = models.CharField(max_length=150)
    woonplaats = models.CharField(max_length=150)
    postcode = models.CharField(max_length=10)
    mobielnummer = models.IntegerField(null=True)
    icenummer = models.IntegerField(null=True)
    email = models.EmailField(max_length=150)
    tariefindicatie = models.FloatField(max_length=20)
    zzper_eigenwerknemer = models.CharField(max_length=50)
    opleidings_niveau = models.CharField(max_length=50)
    burgerlijkse_staat = models.CharField(max_length=100)
    geboorte_datum = models.DateField(null=True)
    foto_medewerker = models.ImageField(upload_to='',
                                        default='userimg.png') # de default foto voor de medewerkers.
    cv = models.FileField(upload_to='static/', null=True) #upload to upload het naar de static files
    title_cv = models.CharField(max_length=50, null=True)
    feedback = models.FileField(upload_to='static/', null=True)
    title_feedback = models.CharField(max_length=50, null=True)
    documenten = models.FileField(upload_to='static/', null=True)
    title_documenten = models.CharField(max_length=50, null=True)

    def get_absolut_url(self):
        return reverse('project1:detail', kwargs={'pk': self.pk}) # dit is voor de details dat elke medewerker zijn eigen detail pagina krijgt met pk

    def __str__(self):
        return self.voornaam + " " + self.tussenvoegsel + " " + self.achternaam # de Self voegt deze 3 variabele bij elkaar die je samen kan ophalen.

class Opmerkingen(models.Model):
    DEFAULT = 'DEFAULT'
    MEDEWERKERS = 'MEDEWERKERS'
    EINDKLANTEN = 'EINDKLANTEN'
    BROKERS = 'BROKERS'
    CATEGORIES = (      # de keuze voor de categorieen.
        (DEFAULT,DEFAULT),
        (MEDEWERKERS,MEDEWERKERS),
        (EINDKLANTEN,EINDKLANTEN),
        (BROKERS,BROKERS),
    )
    title = models.CharField(max_length=100,blank=True,null=True)
    body = models.TextField(null=True,blank=True)
    due_date = models.DateTimeField(default=timezone.now) # timezone.now vult standaard de tijd waarin je de form opent.
    task_finished = models.BooleanField(default=True)
    category = models. CharField(max_length=20, choices=CATEGORIES, default=DEFAULT) # haalt de keuze van de CATEGORIES op.

    def __str__(self):
        return f'{self.title}'

class Leaseautos(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE) #door de ForeignKey in te vullen van de medewerker is de lease auto gelinkt met de medewerker.
    kenteken = models.CharField(max_length=10)
    start_datum_lease_auto = models.DateField(null=True) # DateField is een datum veld.
    eind_datum_lease_auto = models.DateField(null=True)
    merk_auto = models.CharField(max_length=50)
    type_auto = models.CharField(max_length=100)
    leasemaatschappij = models.CharField(max_length=100)
    kilometer_per_jaar = models.IntegerField(null=True)
    lease_bedrag = models.FloatField(max_length=20)

    def __str__(self):
        return self.merk_auto + " " + self.kenteken


class Contracten(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE) #door de ForeignKey in te vullen van de medewerker is het contract gelinkt met de medewerker.
    contract_uren = models.IntegerField(null=True)
    Startdatum = models.DateField(null=True)
    Einddatum = models.DateField(null=True)
    functie_contract = models.CharField(max_length=100)
    salaris = models.FloatField(max_length=20)
    vakantie_dagen = models.IntegerField(null=True)
    Onkostenvergoeding = models.FloatField(max_length=20)


class Certificaten(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE) #door de ForeignKey in te vullen van de medewerker is de certificaat gelinkt met de medewerker.
    naam_certificaat = models.CharField(max_length=100)
    datum_afronding = models.DateField(null=True)
    accreditatie_nummer = models.CharField(max_length=100)
    naam_instituut = models.CharField(max_length=100)


class Eindklanten(models.Model):
    ACCOUNTMANAGER_CHOICES = (
        ('1', 'Yoeri Tromp'),
        ('2', 'Nicky Slothouwer'),
        ('3', 'Coen Berkhout jr'),
        ('4', 'Jessica Berkhout'),
    )
    accountmanager = models.CharField(max_length=5, choices=ACCOUNTMANAGER_CHOICES)
    klantnaam = models.CharField(max_length=50)
    straat_klant = models.CharField(max_length=150)
    huisnummer_klant = models.CharField(max_length=20)
    postcode_klant = models.CharField(max_length=10)
    vestigingplaats_klant = models.CharField(max_length=150)
    telefoonnummer_klant = models.CharField(max_length=17, null=True)
    portaal_klant = models.URLField(max_length=300, null=True)


    def get_absolut_url(self):
        return reverse('project1:eindklanten.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.klantnaam


class Brokers(models.Model):
    ACCOUNTMANAGER_CHOICES = (
        ('1', 'Yoeri Tromp'),
        ('2', 'Nicky Slothouwer'),
        ('3', 'Coen Berkhout jr'),
        ('4', 'Jessica Berkhout'),
    )
    accountmanager = models.CharField(max_length=4, choices=ACCOUNTMANAGER_CHOICES)
    broker_naam = models.CharField(max_length=50)
    straat_broker = models.CharField(max_length=150)
    huisnummer_broker = models.CharField(max_length=20)
    postcode_broker = models.CharField(max_length=10)
    vestigingplaats_broker = models.CharField(max_length=150)
    telefoonnummer_broker = models.IntegerField(null=True)
    portaal_broker = models.URLField(max_length=300, null=True)

    def get_absolut_url(self):
        return reverse('project1:broker.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.broker_naam


class Aanbiedingen(models.Model):
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
    STATUS_CHOICES = (
        ('1', 'Open'),
        ('2', 'Geselecteerd'),
        ('3', 'Intake'),
        ('4', 'Geplaatst'),
        ('5', 'Afgewezen'),
    )
    aangemaakt_door = models.CharField(max_length=50, choices=ACCOUNTMANAGER_CHOICES)
    registratie = models.DateField(null=True)
    laatste_update = models.DateField(null=True)
    functie = models.CharField(max_length=50, choices=FUNCTIE_CHOICES)
    functie_aanbieding = models.CharField(max_length=50)
    klant_naam = models.CharField(max_length=50)
    broker = models.CharField(max_length=50, null=True)
    accountmanager = models.CharField(max_length=4, choices=ACCOUNTMANAGER_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    tarief = models.FloatField(max_length=14, default=True, null=False)
    betaalkorting = models.FloatField(max_length=14, default=True, null=False)
    medewerker = models.CharField(max_length=50)

    def get_status_count(self):
        return Aanbiedingen.objects.all().filter(status='1').count()
