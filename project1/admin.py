from django.contrib import admin
from admin_adv_search_builder.filters import AdvancedSearchBuilder
from .models import Medewerkers, Contracten, Leaseautos, Certificaten, Opmerkingen, Eindklanten, Brokers

admin.site.register(Medewerkers)
admin.site.register(Contracten)
admin.site.register(Leaseautos)
admin.site.register(Certificaten)
admin.site.register(Opmerkingen)
admin.site.register(Eindklanten)
admin.site.register(Brokers)


class Admin(admin.ModelAdmin):
    list_filter = (AdvancedSearchBuilder,)



