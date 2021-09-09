from django.contrib import admin
from . import models

admin.site.register(models.Medewerkers)
admin.site.register(models.Contracten)
admin.site.register(models.Opmerkingen)
admin.site.register(models.Leaseautos)
admin.site.register(models.Certificaten)
