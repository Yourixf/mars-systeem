from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Medewerkers(models.Model):
    voornaam = models.CharField(max_length=100)
    tussenvoegsel = models.CharField(max_length=6, blank=True)
    achternaam = models.CharField(max_length=100)
    bnsnummer = models.IntegerField(null=True)
    huisnummer = models.CharField(max_length=20)
    straat = models.CharField(max_length=150)
    woonplaats = models.CharField(max_length=150)
    postcode = models.CharField(max_length=10)
    mobielnummer = models.IntegerField(null=True)
    icenummer = models.IntegerField(null=True)
    email = models.EmailField(max_length=150)
    teriefindicatie = models.FloatField(max_length=20)
    zzper_eigenwerknemer = models.CharField(max_length=50)
    opleidings_niveau = models.CharField(max_length=50)
    godsdienst = models.CharField(max_length=50)
    burgerlijkse_staat = models.CharField(max_length=100)
    geboorte_datum = models.DateField(null=True)
    foto_medewerker = models.ImageField(upload_to='',
                                        default='userimg.png')

    def get_absolut_url(self):
        return reverse('project1:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.voornaam + " " + self.tussenvoegsel + " " + self.achternaam


class Leaseautos(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE)
    kenteken = models.CharField(max_length=10)
    start_datum_lease_auto = models.DateField(null=True)
    eind_datum_lease_auto = models.DateField(null=True)
    merk_auto = models.CharField(max_length=50)
    type_auto = models.CharField(max_length=100)
    leasemaatschappij = models.CharField(max_length=100)
    kilometer_per_jaar = models.IntegerField(null=True)
    lease_bedrag = models.FloatField(max_length=20)

    def __str__(self):
        return self.merk_auto + " " + self.kenteken


class Opmerkingen(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE)
    datum_opmerkingen = models.DateField(null=True)
    opmerkingveld = models.CharField(max_length=1000)
    naam_user = models.CharField(max_length=30, null=True)


class Contracten(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE)
    contract_uren = models.IntegerField(null=True)
    Startdatum = models.DateField(null=True)
    Einddatum = models.DateField(null=True)
    functie_contract = models.CharField(max_length=100)
    salaris = models.FloatField(max_length=20)
    vakantie_dagen = models.IntegerField(null=True)
    Onkostenvergoeding = models.FloatField(max_length=20)


class Certificaten(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE)
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
    telefoonnummer_klant = models.CharField(max_length=17)
    portaal_klant = models.URLField(max_length=300)


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
    portaal_broker = models.URLField(max_length=300)
