# Dit zijn de import voor de Admin pagina van Django, als je een nieuwe model hebt aangemaakt kan je deze ook zichtbaar maken in de Django admin pagina.
from django.contrib import admin
from admin_adv_search_builder.filters import AdvancedSearchBuilder
from .models import Medewerkers, Contracten, Certificaten, Eindklanten, Brokers, Opmerkingen

#admin.site.register() hier zet je in welke models je in je admin pagina wilt laten verschijnen. Wanneer je een model verwijderd moet je dit ook hierin aanpassen.
admin.site.register(Medewerkers)
admin.site.register(Contracten)
admin.site.register(Certificaten)
admin.site.register(Eindklanten)
admin.site.register(Brokers)
admin.site.register(Opmerkingen)

# dit is een functie om te kunnen zoeken in de admin.
class Admin(admin.ModelAdmin):
    list_filter = (AdvancedSearchBuilder,)



