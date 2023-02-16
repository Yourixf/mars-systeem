# Generated by Django 3.2.15 on 2023-02-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0031_auto_20230208_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aanbiedingen',
            name='begindatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='aanbiedingen',
            name='registratie',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='aanbiedingen_history',
            name='updatedatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='contactpersonen',
            name='begindatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='contactpersonen_history',
            name='updatedatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='documenten',
            name='begindatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='documenten_history',
            name='updatedatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='klanten',
            name='begindatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='klanten_history',
            name='updatedatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='medewerkers',
            name='begindatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='medewerkers',
            name='datum_in_dienst',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='medewerkers_history',
            name='datum_in_dienst',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='medewerkers_history',
            name='updatedatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='opdrachten',
            name='begindatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='opdrachten',
            name='date_created',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='opdrachten_history',
            name='date_created',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='opdrachten_history',
            name='updatedatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='vestigingplaats',
            name='begindatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
        migrations.AlterField(
            model_name='vestigingplaats_history',
            name='updatedatum',
            field=models.DateField(blank=True, default='2023-02-14', null=True),
        ),
    ]
