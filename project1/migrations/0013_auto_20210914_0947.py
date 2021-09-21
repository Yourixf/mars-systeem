# Generated by Django 3.2.7 on 2021-09-14 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0012_medewerkers_achternaam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medewerkers',
            name='uid',
        ),
        migrations.AddField(
            model_name='medewerkers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificaten',
            name='medewerkers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.medewerkers'),
        ),
        migrations.AlterField(
            model_name='contracten',
            name='medewerkers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.medewerkers'),
        ),
        migrations.AlterField(
            model_name='leaseautos',
            name='medewerkers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.medewerkers'),
        ),
        migrations.AlterField(
            model_name='opmerkingen',
            name='medewerkers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.medewerkers'),
        ),
    ]
