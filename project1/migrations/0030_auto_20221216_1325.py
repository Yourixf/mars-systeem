# Generated by Django 3.2.15 on 2022-12-16 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0029_auto_20221128_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klanten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountmanager', models.CharField(blank=True, choices=[('1', 'Yoeri Tromp'), ('2', 'Nicky Slothouwer'), ('3', 'Coen Berkhout jr'), ('4', 'Jessica Berkhout')], max_length=15, null=True)),
                ('naam', models.CharField(blank=True, max_length=50, null=True)),
                ('telefoonnummer', models.CharField(blank=True, max_length=17, null=True)),
                ('portaal', models.URLField(blank=True, max_length=300, null=True)),
                ('soort', models.CharField(blank=True, max_length=15, null=True)),
                ('begindatum', models.DateField(blank=True, default='2022-12-16', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='contactpersonen',
            name='broker',
        ),
        migrations.RemoveField(
            model_name='medewerkers',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='vestigingplaats',
            name='broker',
        ),
        migrations.RemoveField(
            model_name='vestigingplaats',
            name='contactpersoon',
        ),
        migrations.AddField(
            model_name='aanbiedingen',
            name='begindatum',
            field=models.DateField(blank=True, default='2022-12-16', null=True),
        ),
        migrations.AddField(
            model_name='contactpersonen',
            name='begindatum',
            field=models.DateField(blank=True, default='2022-12-16', null=True),
        ),
        migrations.AddField(
            model_name='documenten',
            name='begindatum',
            field=models.DateField(blank=True, default='2022-12-16', null=True),
        ),
        migrations.AddField(
            model_name='medewerkers',
            name='begindatum',
            field=models.DateField(blank=True, default='2022-12-16', null=True),
        ),
        migrations.AddField(
            model_name='opdrachten',
            name='begindatum',
            field=models.DateField(blank=True, default='2022-12-16', null=True),
        ),
        migrations.AddField(
            model_name='vestigingplaats',
            name='begindatum',
            field=models.DateField(blank=True, default='2022-12-16', null=True),
        ),
        migrations.AlterField(
            model_name='aanbiedingen',
            name='functie',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medewerkers',
            name='burgerlijkse_staat',
            field=models.CharField(blank=True, choices=[('1', 'Ongehuwd'), ('2', 'Gehuwd'), ('3', 'Samenwonend')], max_length=100),
        ),
        migrations.AlterField(
            model_name='opdrachten',
            name='date_created',
            field=models.DateField(blank=True, default='2022-12-16', null=True),
        ),
        migrations.CreateModel(
            name='Documenten_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField(blank=True, null=True)),
                ('naam_document', models.CharField(blank=True, max_length=20)),
                ('soort_document', models.CharField(blank=True, max_length=50)),
                ('beschrijving', models.CharField(blank=True, max_length=600)),
                ('document', models.FileField(blank=True, null=True, upload_to='static/')),
                ('updatedatum', models.DateField(blank=True, default='2022-12-16', null=True)),
                ('document_fk', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.documenten')),
                ('medewerker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.medewerkers')),
            ],
        ),
        migrations.AlterField(
            model_name='contactpersonen',
            name='klant',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.klanten'),
        ),
        migrations.AlterField(
            model_name='vestigingplaats',
            name='klant',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project1.klanten'),
        ),
    ]