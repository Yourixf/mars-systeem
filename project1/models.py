from django.db import models
import uuid

class Medewerkers(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voornaam = models.CharField(max_length=100)
    tussenvoegsel = models.CharField(max_length=6)
    bnsnummer = models.IntegerField(null=True)
    huisnummer = models.CharField(max_length=20)
    straat = models.CharField(max_length=150)
    woonplaats = models.CharField(max_length=150)
    postcode = models.CharField(max_length=10)
    mobielnummer = models.CharField(max_length=20)
    icenummer = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    teriefindicatie = models.FloatField(max_length=20)
    zzper_eigenwerknemer = models.CharField(max_length=50)
    opleidings_niveau = models.CharField(max_length=50)
    godsdienst = models.CharField(max_length=50)
    burgerlijkse_staat = models.CharField(max_length=100)
    geboorte_datum = models.DateField(null=True)

class Leaseautos(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE, default="")
    kenteken = models.CharField(max_length=10)
    start_datum_lease_auto = models.DateField(null=True)
    eind_datum_lease_auto = models.DateField(null=True)
    merk_auto = models.CharField(max_length=50)
    type_auto = models.CharField(max_length=100)
    leasemaatschappij = models.CharField(max_length=100)
    kilometer_per_jaar = models.IntegerField(null=True)
    lease_bedrag = models.FloatField(max_length=20)

class Opmerkingen(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE, default="")
    datum_opmerkingen = models.DateField(null=True)
    opmerkingveld = models.CharField(max_length=1000)

class Contracten(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE, default="")
    contract_uren = models.IntegerField(null=True)
    Startdatum = models.DateField(null=True)
    Einddatum = models.DateField(null=True)
    functie_contract = models.CharField(max_length=100)
    salaris = models.FloatField(max_length=20)
    vakantie_dagen = models.IntegerField(null=True)
    Onkostenvergoeding = models.FloatField(max_length=20)

class Certificaten(models.Model):
    medewerkers = models.ForeignKey(Medewerkers, on_delete=models.CASCADE, default="")
    naam_certificaat = models.CharField(max_length=100)
    datum_afronding =  models.DateField(null=True)
    accreditatie_nummer = models.CharField(max_length=100)
    naam_instituut = models.CharField(max_length=100)

