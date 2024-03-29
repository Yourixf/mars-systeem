# Generated by Django 3.2.15 on 2023-02-23 13:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aanbiedingen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarief', models.FloatField(blank=True, default=True, max_length=14, null=True)),
                ('betaalkorting', models.FloatField(blank=True, default=True, max_length=14, null=True)),
                ('aangemaakt_door', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=50)),
                ('functie', models.CharField(blank=True, max_length=50)),
                ('functie_aanbieding', models.CharField(blank=True, max_length=50)),
                ('accountmanager', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=4)),
                ('registratie', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Open'), ('2', 'Intake'), ('3', 'Geplaatst'), ('4', 'Afgewezen'), ('5', 'Opdracht'), ('6', 'Verlopen')], max_length=50)),
                ('laatste_update', models.DateField(blank=True, null=True)),
                ('opmerking', models.CharField(blank=True, max_length=600)),
                ('begindatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('aantal_intakes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactpersonen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(blank=True, max_length=50)),
                ('mail_adres', models.CharField(blank=True, max_length=50)),
                ('telefoonnummer', models.CharField(blank=True, max_length=30)),
                ('functie', models.CharField(blank=True, max_length=50)),
                ('opmerkingen', models.CharField(blank=True, max_length=300)),
                ('begindatum', models.DateField(blank=True, default='2023-02-23', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documenten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam_document', models.CharField(blank=True, max_length=20)),
                ('soort_document', models.CharField(blank=True, max_length=50)),
                ('beschrijving', models.CharField(blank=True, max_length=600)),
                ('document', models.FileField(blank=True, null=True, upload_to='static/')),
                ('begindatum', models.DateField(blank=True, default='2023-02-23', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Klanten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountmanager', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=15, null=True)),
                ('naam', models.CharField(blank=True, max_length=50, null=True)),
                ('telefoonnummer', models.CharField(blank=True, max_length=17, null=True)),
                ('portaal', models.URLField(blank=True, max_length=300, null=True)),
                ('soort', models.CharField(blank=True, max_length=15, null=True)),
                ('begindatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('factuuremail', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medewerkers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voornaam', models.CharField(blank=True, max_length=100)),
                ('werkmail', models.EmailField(blank=True, max_length=150)),
                ('roepnaam', models.CharField(blank=True, max_length=100)),
                ('functie', models.CharField(blank=True, max_length=50)),
                ('tussenvoegsel', models.CharField(blank=True, max_length=6)),
                ('opleidingsniveau', models.CharField(blank=True, choices=[('1', 'Middelbaar beroepsonderwijs (MBO)'), ('2', 'Hoger beroepsonderwijs (HBO)'), ('3', 'Wetenschappelijk onderwijs (WO)')], max_length=50)),
                ('achternaam', models.CharField(blank=True, max_length=100)),
                ('datum_in_dienst', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('geboortedatum', models.DateField(blank=True, null=True)),
                ('burgerlijkse_staat', models.CharField(blank=True, choices=[('1', 'Gehuwd'), ('2', 'Ongehuwd'), ('3', 'Gescheiden/beëindigd samenleving'), ('4', 'Weduwe/weduwnaar'), ('5', 'Samenwonend zonder samenlevingscontract'), ('6', 'Geregistreerd Partnerschap')], max_length=100)),
                ('geboorteplaats', models.CharField(blank=True, max_length=100)),
                ('bsnnummer', models.IntegerField(blank=True, null=True)),
                ('nationaliteit', models.CharField(blank=True, max_length=100)),
                ('lease_auto', models.CharField(blank=True, choices=[('1', 'Ja'), ('2', 'All in'), ('3', 'Lease vergoeding'), ('4', 'Geen')], max_length=15, null=True)),
                ('straat', models.CharField(blank=True, max_length=150)),
                ('bv', models.CharField(blank=True, choices=[('1', 'Ict'), ('2', 'Infra'), ('3', 'III'), ('4', 'Extern')], max_length=50)),
                ('huisnummer', models.CharField(blank=True, max_length=20)),
                ('ice_persoon_naam', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('ice_telefoonnummer', models.IntegerField(blank=True, null=True)),
                ('woonplaats', models.CharField(blank=True, max_length=150)),
                ('aantal_uur', models.IntegerField(blank=True, null=True)),
                ('banknummer', models.CharField(blank=True, max_length=100)),
                ('tariefindicatie', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('telefoonnummer', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Intake'), ('2', 'Opdracht'), ('3', 'Leegloop'), ('4', 'Uit dienst')], max_length=50)),
                ('begindatum', models.DateField(blank=True, default='2023-02-23', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opdrachten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdatum', models.DateField(blank=True, null=True)),
                ('status_opdracht', models.CharField(choices=[('1', 'Lopend'), ('2', 'Afgelopen')], max_length=50)),
                ('einddatum', models.DateField(blank=True, null=True)),
                ('aantal_uren', models.IntegerField(blank=True)),
                ('tarief_opdracht', models.FloatField(blank=True, default=True)),
                ('opdracht_aangemaakt_door', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=4)),
                ('opdracht_betaalkorting', models.FloatField(blank=True, default=True, null=True)),
                ('date_created', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('opdracht_nummer', models.CharField(blank=True, max_length=50)),
                ('opmerking', models.CharField(blank=True, max_length=600)),
                ('begindatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('aanbieding', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.aanbiedingen')),
            ],
        ),
        migrations.CreateModel(
            name='Opmerkingen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_finished', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('MEDEWERKERS', 'MEDEWERKERS'), ('EINDKLANTEN', 'EINDKLANTEN'), ('BROKERS', 'BROKERS')], default='DEFAULT', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vestigingplaats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vestiging', models.CharField(blank=True, choices=[('1', 'Hoofdkantoor'), ('2', 'Bijkantoor')], max_length=20)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('straatnaam', models.CharField(blank=True, max_length=30)),
                ('huisnummer', models.IntegerField(blank=True)),
                ('plaats', models.CharField(blank=True, max_length=20)),
                ('opmerkingen', models.CharField(blank=True, max_length=300)),
                ('begindatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('klant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.klanten')),
            ],
        ),
        migrations.CreateModel(
            name='Vestigingplaats_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField(blank=True, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('straatnaam', models.CharField(blank=True, max_length=30)),
                ('huisnummer', models.IntegerField(blank=True)),
                ('plaats', models.CharField(blank=True, max_length=20)),
                ('vestiging', models.CharField(blank=True, max_length=20)),
                ('opmerkingen', models.CharField(blank=True, max_length=300)),
                ('updatedatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('klant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.klanten')),
                ('vestig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.vestigingplaats')),
            ],
        ),
        migrations.CreateModel(
            name='Opdrachten_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField(blank=True)),
                ('status_opdracht', models.CharField(choices=[('1', 'Lopend'), ('2', 'Afgelopen')], max_length=50)),
                ('startdatum', models.DateField(blank=True, null=True)),
                ('einddatum', models.DateField(blank=True, null=True)),
                ('tarief_opdracht', models.FloatField(blank=True, default=True)),
                ('opdracht_betaalkorting', models.FloatField(blank=True, default=True, null=True)),
                ('aantal_uren', models.IntegerField(blank=True)),
                ('opdracht_aangemaakt_door', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=4)),
                ('date_created', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('opdracht_nummer', models.CharField(blank=True, max_length=50)),
                ('opmerking', models.CharField(blank=True, max_length=600)),
                ('updatedatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('aanbieding', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.aanbiedingen')),
                ('opdracht', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.opdrachten')),
            ],
        ),
        migrations.CreateModel(
            name='Medewerkers_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField(blank=True, null=True)),
                ('voornaam', models.CharField(blank=True, max_length=100)),
                ('werkmail', models.EmailField(blank=True, max_length=150)),
                ('roepnaam', models.CharField(blank=True, max_length=100)),
                ('functie', models.CharField(blank=True, max_length=50)),
                ('tussenvoegsel', models.CharField(blank=True, max_length=6)),
                ('opleidingsniveau', models.CharField(blank=True, choices=[('1', 'Middelbaar beroepsonderwijs (MBO)'), ('2', 'Hoger beroepsonderwijs (HBO)'), ('3', 'Wetenschappelijk onderwijs (WO)')], max_length=50)),
                ('achternaam', models.CharField(blank=True, max_length=100)),
                ('datum_in_dienst', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('geboortedatum', models.DateField(blank=True, null=True)),
                ('burgerlijkse_staat', models.CharField(blank=True, choices=[('1', 'Gehuwd'), ('2', 'Ongehuwd'), ('3', 'Gescheiden/beëindigd samenleving'), ('4', 'Weduwe/weduwnaar'), ('5', 'Samenwonend zonder samenlevingscontract'), ('6', 'Geregistreerd Partnerschap')], max_length=100)),
                ('geboorteplaats', models.CharField(blank=True, max_length=100)),
                ('bsnnummer', models.IntegerField(blank=True, null=True)),
                ('nationaliteit', models.CharField(blank=True, max_length=100)),
                ('lease_auto', models.CharField(blank=True, choices=[('1', 'Ja'), ('2', 'All in'), ('3', 'Lease vergoeding'), ('4', 'Geen')], max_length=15, null=True)),
                ('straat', models.CharField(blank=True, max_length=150)),
                ('bv', models.CharField(blank=True, choices=[('1', 'Ict'), ('2', 'Infra'), ('3', 'III'), ('4', 'Extern')], max_length=50)),
                ('huisnummer', models.CharField(blank=True, max_length=20)),
                ('ice_persoon_naam', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('ice_telefoonnummer', models.IntegerField(blank=True, null=True)),
                ('woonplaats', models.CharField(blank=True, max_length=150)),
                ('aantal_uur', models.IntegerField(blank=True, null=True)),
                ('banknummer', models.CharField(blank=True, max_length=100)),
                ('tariefindicatie', models.FloatField(blank=True, default=0, max_length=20, null=True)),
                ('telefoonnummer', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Intake'), ('2', 'Opdracht'), ('3', 'Leegloop'), ('4', 'Uit dienst')], max_length=50)),
                ('updatedatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('medewerker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.medewerkers')),
            ],
        ),
        migrations.CreateModel(
            name='Klanten_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField(blank=True)),
                ('accountmanager', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=15, null=True)),
                ('naam', models.CharField(blank=True, max_length=50, null=True)),
                ('telefoonnummer', models.CharField(blank=True, max_length=17, null=True)),
                ('portaal', models.URLField(blank=True, max_length=300, null=True)),
                ('soort', models.CharField(blank=True, max_length=15, null=True)),
                ('updatedatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('factuuremail', models.EmailField(blank=True, max_length=100, null=True)),
                ('klant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.klanten')),
            ],
        ),
        migrations.CreateModel(
            name='Eindklanten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountmanager', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=5, null=True)),
                ('klantnaam', models.CharField(blank=True, max_length=50, null=True)),
                ('telefoonnummer_klant', models.CharField(blank=True, max_length=17, null=True)),
                ('portaal_klant', models.URLField(blank=True, max_length=300, null=True)),
                ('contactpersoon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.contactpersonen')),
                ('vestiging', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.vestigingplaats')),
            ],
        ),
        migrations.CreateModel(
            name='Documenten_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField(blank=True, null=True)),
                ('naam_document', models.CharField(blank=True, max_length=20)),
                ('soort_document', models.CharField(blank=True, max_length=50)),
                ('beschrijving', models.CharField(blank=True, max_length=600)),
                ('document_path', models.FileField(blank=True, null=True, upload_to='static/')),
                ('updatedatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('document', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.documenten')),
                ('medewerker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.medewerkers')),
            ],
        ),
        migrations.AddField(
            model_name='documenten',
            name='medewerker',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.medewerkers'),
        ),
        migrations.CreateModel(
            name='Contracten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_uren', models.IntegerField(null=True)),
                ('Startdatum', models.DateField(null=True)),
                ('Einddatum', models.DateField(null=True)),
                ('functie_contract', models.CharField(max_length=100)),
                ('salaris', models.FloatField(max_length=20)),
                ('vakantie_dagen', models.IntegerField(null=True)),
                ('Onkostenvergoeding', models.FloatField(max_length=20)),
                ('medewerkers', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project1.medewerkers')),
            ],
        ),
        migrations.CreateModel(
            name='Contactpersonen_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField(blank=True)),
                ('naam', models.CharField(blank=True, max_length=50)),
                ('mail_adres', models.CharField(blank=True, max_length=50)),
                ('telefoonnummer', models.CharField(blank=True, max_length=30)),
                ('functie', models.CharField(blank=True, max_length=50)),
                ('opmerkingen', models.CharField(blank=True, max_length=300)),
                ('updatedatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('contactpersoon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.contactpersonen')),
                ('klant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.klanten')),
                ('vestiging', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.vestigingplaats')),
            ],
        ),
        migrations.AddField(
            model_name='contactpersonen',
            name='klant',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.klanten'),
        ),
        migrations.AddField(
            model_name='contactpersonen',
            name='vestiging',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.vestigingplaats'),
        ),
        migrations.CreateModel(
            name='Certificaten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam_certificaat', models.CharField(max_length=100)),
                ('datum_afronding', models.DateField(null=True)),
                ('accreditatie_nummer', models.CharField(max_length=100)),
                ('naam_instituut', models.CharField(max_length=100)),
                ('medewerkers', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project1.medewerkers')),
            ],
        ),
        migrations.CreateModel(
            name='Brokers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountmanager', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=4)),
                ('broker_naam', models.CharField(blank=True, max_length=50)),
                ('telefoonnummer_broker', models.CharField(blank=True, max_length=20, null=True)),
                ('portaal_broker', models.URLField(blank=True, max_length=300, null=True)),
                ('contactpersoon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.contactpersonen')),
                ('vestiging', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.vestigingplaats')),
            ],
        ),
        migrations.CreateModel(
            name='Aanbiedingen_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField(blank=True, null=True)),
                ('aangemaakt_door', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=50)),
                ('registratie', models.DateField(blank=True, null=True)),
                ('laatste_update', models.DateField(blank=True, null=True)),
                ('functie', models.CharField(max_length=50)),
                ('functie_aanbieding', models.CharField(max_length=50)),
                ('accountmanager', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=4)),
                ('status', models.CharField(choices=[('1', 'Open'), ('2', 'Intake'), ('3', 'Geplaatst'), ('4', 'Afgewezen'), ('5', 'Opdracht'), ('6', 'Verlopen')], max_length=50)),
                ('tarief', models.FloatField(default=True, max_length=14, null=True)),
                ('betaalkorting', models.FloatField(default=True, max_length=14, null=True)),
                ('opmerking', models.CharField(blank=True, max_length=600)),
                ('updatedatum', models.DateField(blank=True, default='2023-02-23', null=True)),
                ('aantal_intakes', models.IntegerField(blank=True, null=True)),
                ('aanbieding', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.aanbiedingen')),
                ('broker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='broker_history', to='project1.klanten')),
                ('klant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='klant_history', to='project1.klanten')),
                ('medewerker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project1.medewerkers')),
            ],
        ),
        migrations.AddField(
            model_name='aanbiedingen',
            name='broker',
            field=models.ForeignKey(blank=True, limit_choices_to={'soort': '2'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='broker', to='project1.klanten'),
        ),
        migrations.AddField(
            model_name='aanbiedingen',
            name='klant',
            field=models.ForeignKey(blank=True, limit_choices_to={'soort': '1'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='klant', to='project1.klanten'),
        ),
        migrations.AddField(
            model_name='aanbiedingen',
            name='medewerker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.medewerkers'),
        ),
    ]
