# Bij alle tamplates die waar functies staan worden kan je dingen importen die je vervolgens kan gebruiken in je code die staan hier onder.
# "from djano.db import blablabla" (voorbeeld van hieronder). Ook importen vanuit andere templates zoals de views.py template.
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from project1 import views

app_name = 'project1'
#Dit zijn de "Paths" die URLS moeten voorstellen van de webapplicatie. Begint met PATH(r'dit is dan de url waar de persoon op zoekt.', dan laat je hem zoeken naar view functie in de views template.
# )


urlpatterns = [
    # zoekt naar de view registerPage ( alles in de views.py)
    path(r'register/', views.registerPage, name='register'),
    # zoekt naar de view loginPage
    path('login/', views.loginPage, name="login"),
    # zoekt naar de view logoutUser
    path('logout/', views.logoutUser, name="logout"),
    # zoekt naar de view Index
    path(r'', views.Index, name='index'),
    # zoekt naar de view MedewerkersPage
    path(r'medewerkers/', views.MedewerkersPage, name='medewerkers'),
    # zoekt naar de view Detail(medewerkers)
    path(r'medewerkers/<str:pk>/', views.MedewerkerDetail, name='details'),
    # zoekt naar de view Leaseautosdetail
    # zoekt naar de view Contractendetail
    path('contracten.detail/<str:pk>/', views.Contractendetail, name='contracten.detail'),
    # zoekt naar de admin page
    path(r'admin/', admin.site.urls),
    # zoekt naar view Foto toevoegen
    path(r'foto_toevoegen/<str:pk>/', views.Foto_Toevoegen, name='foto_toevoegen'),
    # zoekt naar view Medewerker toevoegen
    path(r'medewerker/toevoegen/', views.MedewerkersToevoegen, name='medewerker_toevoegen'),
    # zoekt naar view Medewerkers delete
    path(r'medewerker/delete/<str:pk>/', views.MedewerkerDelete, name='medewerker_delete'),
    # zoekt naar de view Medewerker update

    path(r'medewerker/update/<str:pk>/', views.MedewerkersUpdaten, name='medewerker_update'),
    # zoekt naar de view Contracten toevoegen
    path(r'contracten/toevoegen/<str:pk>/', views.ContractenToevoegen, name='contracten_toevoegen'),
    # zoekt naar de view Eindklanten Page
    path(r'eindklanten_page/', views.EindklantenPage, name='eindklanten'),
    # zoekt naar de view Eindklanten toevoegen
    path(r'eindklanten/toevoegen', views.EindklantToevoegen, name='eindklanten_toevoegen'),
    # zoekt naar de view Eindklanten delete
    path(r'eindklant/delete/<str:id>/', views.EindklantDelete, name='eindklant_delete'),
    # zoekt naar de view Eindklanten Update
    path(r'eindklant/update/<str:pk>/', views.EindklantenUpdaten, name='eindklant_update'),
    # zoekt naar de view Broker Page
    path(r'brokers_page/', views.BrokersPage, name='brokers'),
    # zoekt naar de view Brokers toevoegen
    path(r'brokers/toevoegen', views.BrokersToevoegen, name='brokers_toevoegen'),
    # zoekt naar de view admin page
    path(r'broker/delete/<str:id>/', views.BrokerDelete, name='broker_delete'),
    # zoekt naar de view Broker update
    path(r'broker/update/<str:pk>/', views.BrokerUpdaten, name='broker_update'),
    # zoekt naar de view contract update
    path(r'contract/update/<str:pk>/', views.ContractenUpdate.as_view(), name='contract_update'),
    # zoekt naar de view certificaten
    path(r'certificaten/toevoegen/<str:pk>/', views.CertificatenToevoegen, name='certificaten_toevoegen'),
    # zoekt naar de view contact delete
    path(r'contract/delete/<str:id>/', views.ContractenDelete, name='contract_delete'),
    # zoekt naar de view aanbieding page
    path(r'aanbiedingen_page/', views.AanbiedingenPage, name='aanbiedingen'),
    # zoekt naar de view aanbieding toevoegen
    path(r'aanbiedingen/toevoegen/', views.AanbiedingToevoegen, name='aanbieding_toevoegen'),
    # zoekt naar de view aanbieding update
    path(r'aanbieding/update/<str:pk>/', views.AanbiedingUpdaten, name='aanbieding_update'),
    # zoekt naar de view aanbieding delete
    path(r'aanbieding/delete/<str:pk>/', views.AanbiedingDelete, name='aanbieding_delete'),
    # zoekt naar de view aan archief aanbiedingen page
    path(r'archief/aanbiedingen_page/', views.ArchiefAanbiedingenPage, name='archief_aanbiedingen'),
    # zoekt naar de view aanbieding met opdracht
    path(r'opdracht/aanbieding/', views.AanbiedingMetOpdracht, name='opdracht_aanbieding'),
    # zoekt naar de view Broker detail
    path(r'broker/<str:pk>/', views.BrokerDetail, name='broker_detail'),
    # zoekt naar de view eindklant detail
    path(r'eindklant/<str:pk>/', views.EindklantDetail, name='eindklant_detail'),
    # zoekt naar de view upload cv
    path(r'upload/cv/<str:pk>/', views.Cv_Upload, name='cv_upload'),
    # zoekt naar de view feedback upload
    path(r'upload/feedback/<str:pk>/', views.Feedback_Upload, name='feedback_upload'),
    # zoekt naar de view documenten upload
    path(r'upload/documenten/<str:pk>/', views.Documenten_Upload, name='documenten_upload'),
    # zoekt naar de view aanbiedingen detail
    path(r'aanbiedingen/<str:pk>/', views.AanbiedingenDetail, name='aanbieding_detail'),
    # zoekt naar de view TodoItemCreateView
    path(r'todo/create', views.OpmerkingSchrijvenView.as_view(), name='create_list'),
    # zoekt naar de view TodoItemlistView
    path('opmerkingen/', views.OpmerkingenPageView.as_view(), name='todo_list'),
    # zoekt naar de view TodoItemUpdateView
    path('opmerkingen/update/<str:pk>/', views.OpmerkingenUpdateView.as_view(), name='update_list'),
    # zoekt naar de view TodoItemDelete
    path('opmerkingen/delete/<str:pk>/', views.OpmerkingenDeleteView.as_view(), name='delete_list'),
    # voor vestigingsadres
    path(r'vestiging/toevoegen/<str:pk>/', views.VestigingToevoegen, name='vestiging_toevoegen'),
    #voor vestiging updaten
    path(r'vestiging/updaten/<str:pk>/', views.VestigingUpdaten, name='vestiging_updaten'),
    #voor vestiging deleten
    path(r'vestiging/delete/<str:pk>/', views.VestigingDeleten, name='vestiging_delete'),
    #voor lopende opdrachten
    path(r'opdrachten/lopende', views.lopendeOpdrachtenPage, name='lopende_opdrachten'),
    #voor opdrachten die aflopen
    path(r'opdrachten/aflopende', views.aflopendeOpdrachtenPage, name='aflopende_opdrachten'),
    #voor archief opdrachten
    path(r'opdrachten/archief', views.archiefOpdrachtenPage, name='archief_opdrachten'),
    #voor opdrachten updaten
    path(r'opdrachten/updaten/<str:pk>/', views.OpdrachtenUpdaten, name='update_opdracht'),
    #voor opdrachten detail
    path(r'opdrachten/detail/<str:pk>/', views.OpdrachtenDetail, name='detail_opdracht'),
    #voor opdrachten maken
    path(r'opdracht/toevoegen/<str:pk>/', views.OpdrachtToevoegen, name='toevoegen_opdracht'),
    #voor opdrachten te deleten
    path(r'opdracht/delete/<str:pk>', views.OpdrachtDelete, name='delete_opdracht'),
    #voor medewerkers die in de leegloop zijn
    path(r'leegloop/medewerkers', views.MedewerkersLeegloop, name='leegloop_medewerkers'),
    #voor oud medewerkers
    path(r'archief/medewerkers', views.ArchiefMedewerkers, name='archief_medewerkers'),
    #voor medewerkers met aanbiedingen / opdrachten
    path(r'medewerker/aanbiedingen/opdrachten/<str:pk>', views.MedewerkerAanbiedingOpdrachten, name='opdracht_aanbieding_medewerkers'),
    #voor contactpersonen
    path(r'contactpersonen/toevoegen/<str:pk>/', views.ContactPersonenToevoegen, name='toevoegen.contactpersoon'),
    #voor contactpesonen updaten
    path(r'contactpersoon/updaten/<str:pk>/', views.ContactPersoonUpdaten, name='update_contactpersoon'),
    #voor contactpersoon delete
    path(r'contactpersoon/delete/<str:pk>/', views.ContactPersonenDelete, name='delete_contactpersoon'),

    # dit is de download path die hij zodat je de download van de betreffende persoon alleen kan downloaden op wie je klinkt en waar django het weg schrijft.
    url(r'^download/<str:pk>/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),



]
# Deze "routes" van de static en de media url voor als er iets geupload wordt.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
