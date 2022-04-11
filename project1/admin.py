from django.contrib import admin
from admin_adv_search_builder.filters import AdvancedSearchBuilder
from .models import Medewerkers, Contracten, Leaseautos, Certificaten, Opmerking, Eindklanten, Brokers

admin.site.register(Medewerkers)
admin.site.register(Contracten)
admin.site.register(Leaseautos)
admin.site.register(Certificaten)
admin.site.register(Opmerking)
admin.site.register(Eindklanten)
admin.site.register(Brokers)

class Admin(admin.ModelAdmin):
    list_filter = (AdvancedSearchBuilder,)



