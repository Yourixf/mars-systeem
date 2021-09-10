from django.contrib import admin
from .models import Medewerkers, Contracten, Opmerkingen, Leaseautos, Certificaten

admin.site.register(Medewerkers)
admin.site.register(Contracten)
admin.site.register(Opmerkingen)
admin.site.register(Leaseautos)
admin.site.register(Certificaten)
