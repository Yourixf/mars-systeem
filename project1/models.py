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
    ('1', 'Ict'),
    ('2', 'Infra'),
    ('3', 'III'),
    ('4', 'Extern')
)

BURGERLIJKE_STAAT_CHOICES = (
    ('1', 'Gehuwd'),
    ('2', 'Ongehuwd'),
    ('3', 'Gescheiden/beëindigd samenleving'),
    ('4', 'Weduwe/weduwnaar'),
    ('5', 'Samenwonend zonder samenlevingscontract'),
    ('6', 'Geregistreerd Partnerschap')
)

KANTOOR_CHOICES = (
    ('1', 'Hoofdkantoor'),
    ('2', 'Bijkantoor')
)

KLANT_SOORT_CHOICES = (
    ('1', 'Eindklant'),
    ('2', 'Tussenpartij'),
)

class Documenten(models.Model):
    naam_document = models.CharField(max_length=20, blank=True)
    soort_document = models.CharField(max_length=50, blank=True)
    beschrijving = models.CharField(max_length=600, blank=True)
    document = models.FileField(upload_to='static/', null=True, blank=True)
    medewerker = models.ForeignKey("Medewerkers", on_delete=models.DO_NOTHING, blank=True)
    begindatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))

class Documenten_History(models.Model):
    document = models.ForeignKey("Documenten", on_delete=models.DO_NOTHING, blank=True)
    update_id = models.IntegerField(null=True, blank=True)
    naam_document = models.CharField(max_length=20, blank=True)
    soort_document = models.CharField(max_length=50, blank=True)
    beschrijving = models.CharField(max_length=600, blank=True)
    document_path = models.FileField(upload_to='static/', null=True, blank=True)
    medewerker = models.ForeignKey("Medewerkers", on_delete=models.DO_NOTHING, blank=True)
    updatedatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))
    

class Medewerkers(models.Model):
    voornaam = models.CharField(max_length=100, blank=True)  # max_length=... is bedoeld voor hoeveel tekens het maximaal mag bevatten.
    werkmail = models.EmailField(max_length=150, blank=True)
    roepnaam = models.CharField(max_length=100, blank=True)
    functie = models.CharField(max_length=50, blank=True)
    tussenvoegsel = models.CharField(max_length=6, blank=True)  # blank=True betekend dat het veld leeg mag zijn ( bij Charfield )
    opleidingsniveau = models.CharField(choices=OPLEIDINGNIVEAU_CHOICES, max_length=50, blank=True)
    achternaam = models.CharField(max_length=100, blank=True)
    datum_in_dienst = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))
    geboortedatum = models.DateField(null=True, blank=True)
    burgerlijkse_staat = models.CharField(choices=BURGERLIJKE_STAAT_CHOICES, max_length=100, blank=True)
    geboorteplaats = models.CharField(max_length=100, blank=True)
    bsnnummer = models.IntegerField(null=True, blank=True)  # null=True betekend dat het veld leeg mag zijn ( bij IntegerField )
    nationaliteit = models.CharField(max_length=100, blank=True)
    lease_auto = models.CharField(max_length=15, choices=LEASE_AUTO_CHOICES, null=True, blank=True)
    straat = models.CharField(max_length=150, blank=True)
    bv = models.CharField(choices=BV_CHOICES, blank=True, max_length=50)
    huisnummer = models.CharField(max_length=20, blank=True)
    ice_persoon_naam = models.CharField( max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    ice_telefoonnummer = models.IntegerField(null=True, blank=True)
    woonplaats = models.CharField(max_length=150, blank=True)
    aantal_uur = models.IntegerField(null=True, blank=True)
    banknummer = models.CharField(max_length=100, blank=True)
   # privémail = models.EmailField(max_length=150, blank=True)
    tariefindicatie = models.FloatField(max_length=20, blank=True, null=True, default=0)
    telefoonnummer = models.CharField(null=True, max_length=20, blank=True)
    status = models.CharField(choices=STATUS_MEDEWERKER_CHOICES, max_length=50, blank=True)
    begindatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))


    def get_absolut_url(self):
        return reverse('project1:detail', kwargs={
            'pk': self.pk})  # dit is voor de details dat elke medewerker zijn eigen detail pagina krijgt met pk



    def __str__(self):
        try:
            return self.voornaam + " " + self.tussenvoegsel + " " + self.achternaam  # de Self voegt deze 3 variabele bij elkaar die je samen kan ophalen.
        except:
            pizza = ''

    def get_status_count(self):
        return Medewerkers.objects.all().filter(status='1').count()


class Medewerkers_History(models.Model):
    medewerker = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING, blank=True, null=True)
    update_id = models.IntegerField(blank=True, null=True)
    voornaam = models.CharField(max_length=100,
                                blank=True)  # max_length=... is bedoeld voor hoeveel tekens het maximaal mag bevatten.
    werkmail = models.EmailField(max_length=150, blank=True)
    roepnaam = models.CharField(max_length=100, blank=True)
    functie = models.CharField(max_length=50, blank=True)
    tussenvoegsel = models.CharField(max_length=6,
                                     blank=True)  # blank=True betekend dat het veld leeg mag zijn ( bij Charfield )
    opleidingsniveau = models.CharField(choices=OPLEIDINGNIVEAU_CHOICES, max_length=50, blank=True)
    achternaam = models.CharField(max_length=100, blank=True)
    datum_in_dienst = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))
    geboortedatum = models.DateField(null=True, blank=True)
    burgerlijkse_staat = models.CharField(choices=BURGERLIJKE_STAAT_CHOICES, max_length=100, blank=True)
    geboorteplaats = models.CharField(max_length=100, blank=True)
    bsnnummer = models.IntegerField(null=True,
                                    blank=True)  # null=True betekend dat het veld leeg mag zijn ( bij IntegerField )
    nationaliteit = models.CharField(max_length=100, blank=True)
    lease_auto = models.CharField(max_length=15, choices=LEASE_AUTO_CHOICES, null=True, blank=True)
    straat = models.CharField(max_length=150, blank=True)
    bv = models.CharField(choices=BV_CHOICES, blank=True, max_length=50)
    huisnummer = models.CharField(max_length=20, blank=True)
    ice_persoon_naam = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    ice_telefoonnummer = models.IntegerField(null=True, blank=True)
    woonplaats = models.CharField(max_length=150, blank=True)
    aantal_uur = models.IntegerField(null=True, blank=True)
    banknummer = models.CharField(max_length=100, blank=True)
    # privémail = models.EmailField(max_length=150, blank=True)
    tariefindicatie = models.FloatField(max_length=20, blank=True, null=True, default=0)
    telefoonnummer = models.CharField(null=True, max_length=20, blank=True)
    status = models.CharField(choices=STATUS_MEDEWERKER_CHOICES, max_length=50, blank=True)
    updatedatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))

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


# VOOR  NIEUWE KLANTEN TABEL ( EINDKLANTEN EN BROKER SAMENGEVOEGD)
class Klanten(models.Model):
    accountmanager = models.CharField(max_length=15, choices=ACCOUNTMANAGER_CHOICES, null=True, blank=True)
    naam = models.CharField(max_length=50, null=True, blank=True)
    telefoonnummer = models.CharField(max_length=17, null=True, blank=True)
    portaal = models.URLField(max_length=300, null=True, blank=True)
    soort = models.CharField(max_length=15, null=True, blank=True)
    begindatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))
    factuuremail = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        try:
            return self.naam
        except:
            pizza = ''

class Klanten_History(models.Model):
    klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING, blank=True, null=True)
    update_id = models.IntegerField(blank=True)
    accountmanager = models.CharField(max_length=15, choices=ACCOUNTMANAGER_CHOICES, null=True, blank=True)
    naam = models.CharField(max_length=50, null=True, blank=True)
    telefoonnummer = models.CharField(max_length=17, null=True, blank=True)
    portaal = models.URLField(max_length=300, null=True, blank=True)
    soort = models.CharField(max_length=15, null=True, blank=True)
    updatedatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))
    factuuremail = models.EmailField(max_length=100, blank=True, null=True)



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
    vestiging = models.CharField(choices=KANTOOR_CHOICES, max_length=20, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    straatnaam = models.CharField(max_length=30, blank=True)
    huisnummer = models.IntegerField(blank=True)
    plaats = models.CharField(max_length=20, blank=True)
    klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING, blank=True)
    opmerkingen = models.CharField(max_length=300, blank=True)
    begindatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))

    def __str__(self):
        return self.straatnaam + ' ' + str(self.huisnummer) + ', ' + self.postcode + ' ' + self.plaats


class Vestigingplaats_History(models.Model):
    vestig = models.ForeignKey(Vestigingplaats, on_delete=models.DO_NOTHING, blank=True, null=True)
    update_id = models.IntegerField(blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True)
    straatnaam = models.CharField(max_length=30, blank=True)
    huisnummer = models.IntegerField(blank=True)
    plaats = models.CharField(max_length=20, blank=True)
    vestiging = models.CharField(max_length=20, blank=True)
    klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING, blank=True)
    opmerkingen = models.CharField(max_length=300, blank=True)
    updatedatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))


class Contactpersonen(models.Model):
    naam = models.CharField(max_length=50, blank=True)
    mail_adres = models.CharField(max_length=50, blank=True)
    telefoonnummer = models.CharField(max_length=30, blank=True)
    functie = models.CharField(max_length=50, blank=True)
    klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING, blank=True)
    vestiging = models.ForeignKey(Vestigingplaats, on_delete=models.DO_NOTHING, blank=True)
    opmerkingen = models.CharField(max_length=300, blank=True)
    begindatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))


class Contactpersonen_History(models.Model):
    contactpersoon = models.ForeignKey(Contactpersonen, on_delete=models.DO_NOTHING, blank=True)
    update_id = models.IntegerField(blank=True)
    naam = models.CharField(max_length=50, blank=True)
    mail_adres = models.CharField(max_length=50, blank=True)
    telefoonnummer = models.CharField(max_length=30, blank=True)
    functie = models.CharField(max_length=50, blank=True)
    klant = models.ForeignKey(Klanten, on_delete=models.DO_NOTHING, blank=True, null=True)
    vestiging = models.ForeignKey(Vestigingplaats, on_delete=models.DO_NOTHING, blank=True, null=True)
    opmerkingen = models.CharField(max_length=300, blank=True)
    updatedatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))


class Aanbiedingen(models.Model):
    medewerker = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING, blank=False, null=True)
    tarief = models.FloatField(max_length=14, default=True, null=True, blank=True)
    betaalkorting = models.FloatField(max_length=14, default=True, null=True, blank=True)
    aangemaakt_door = models.CharField(max_length=50, choices=ACCOUNTMANAGER_CHOICES, blank=True)
    functie = models.CharField(max_length=50, blank=True)
    functie_aanbieding = models.CharField(max_length=50, blank=True)
    klant = models.ForeignKey(Klanten, related_name='klant', on_delete=models.DO_NOTHING, blank=True,
                              limit_choices_to={'soort': '1'})
    broker = models.ForeignKey(Klanten, related_name='broker', on_delete=models.DO_NOTHING, blank=True,
                               limit_choices_to={'soort': '2'})
    accountmanager = models.CharField(max_length=4, choices=ACCOUNTMANAGER_CHOICES, blank=True)

    registratie = models.DateField(null=True, blank=True)
    laatste_update = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_AANBIEDING_CHOICES, blank=True)
    begindatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))


    def get_status_count(self):
        return Aanbiedingen.objects.all().filter(status='1').count()


class Aanbiedingen_History(models.Model):
    aanbieding = models.ForeignKey(Aanbiedingen, on_delete=models.DO_NOTHING, blank=True)
    update_id = models.IntegerField(null=True, blank=True)
    aangemaakt_door = models.CharField(max_length=50, choices=ACCOUNTMANAGER_CHOICES, blank=True)
    registratie = models.DateField(null=True, blank=True)
    laatste_update = models.DateField(null=True, blank=True)
    functie = models.CharField(max_length=50)
    functie_aanbieding = models.CharField(max_length=50)
    klant = models.ForeignKey(Klanten, related_name='klant_history', on_delete=models.DO_NOTHING, blank=True)
    broker = models.ForeignKey(Klanten, related_name='broker_history', on_delete=models.DO_NOTHING, blank=True)
    accountmanager = models.CharField(max_length=4, choices=ACCOUNTMANAGER_CHOICES, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_AANBIEDING_CHOICES)
    tarief = models.FloatField(max_length=14, default=True, null=True)
    betaalkorting = models.FloatField(max_length=14, default=True, null=True)
    medewerker = models.ForeignKey(Medewerkers, on_delete=models.DO_NOTHING, blank=False)
    updatedatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))



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
    begindatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))


    def get_status_count(self):
        return Opdrachten.objects.all().filter(status='1').count()



class Opdrachten_History(models.Model):
    opdracht = models.ForeignKey(Opdrachten, on_delete=models.DO_NOTHING, blank=True, null=True)
    update_id = models.IntegerField(blank=True)
    aanbieding = models.ForeignKey(Aanbiedingen, on_delete=models.DO_NOTHING, blank=True)
    status_opdracht = models.CharField(max_length=50, choices=STATUS_OPDRACHT_CHOICES)
    startdatum = models.DateField(null=True, blank=True)
    einddatum = models.DateField(null=True, blank=True)
    tarief_opdracht = models.FloatField(default=True, blank=True)
    opdracht_betaalkorting = models.FloatField(default=True, null=True, blank=True)
    aantal_uren = models.IntegerField(blank=True)
    opdracht_aangemaakt_door = models.CharField(max_length=4, choices=ACCOUNTMANAGER_CHOICES, blank=True)
    date_created = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))
    updatedatum = models.DateField(null=True, blank=True, default=dateformat.format(timezone.now(), 'o-m-d'))
