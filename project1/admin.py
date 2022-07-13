from django.contrib import admin
from admin_adv_search_builder.filters import AdvancedSearchBuilder
from .models import Medewerkers, Contracten, Leaseautos, Certificaten, Eindklanten, Brokers, Postbrokers, Opmerkingenmedewerker


admin.site.register(Medewerkers)
admin.site.register(Contracten)
admin.site.register(Leaseautos)
admin.site.register(Certificaten)
admin.site.register(Eindklanten)
admin.site.register(Brokers)
admin.site.register(Postbrokers)
admin.site.register(Opmerkingenmedewerker)


class Admin(admin.ModelAdmin):
    list_filter = (AdvancedSearchBuilder,)



