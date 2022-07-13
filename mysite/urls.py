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
    # zoekt naar de view registerPage
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
    path(r'medewerkers/<str:pk>/', views.Detail, name='details'),
    # zoekt naar de view Leaseautosdetail
    path('lease.autos.detail/<str:pk>/', views.Leaseautosdetail, name='lease.autos.detail'),
    # zoekt naar de view Contractendetail
    path('contracten.detail/<str:pk>/', views.Contractendetail, name='contracten.detail'),
    # zoekt naar de admin page
    path(r'admin/', admin.site.urls),
    # zoekt naar view Foto toevoegen
    path(r'foto_toevoegen/<str:pk>/', views.Foto_Toevoegen, name='foto_toevoegen'),
    # zoekt naar view Medewerker toevoegen
    path(r'medewerker.toevoegen/', views.MedewerkersToevoegen, name='medewerker_toevoegen'),
    # zoekt naar view Medewerkers delete
    path(r'medewerker/delete/<str:pk>/', views.MedewerkerDelete, name='medewerker_delete'),
    # zoekt naar de view Medewerker update
    path(r'medewerker/update/<str:pk>/', views.MedewerkerUpdate.as_view(), name='medewerker_update'),
    # zoekt naar de view Contracten toevoegen
    path(r'contracten.toevoegen/<str:pk>/', views.ContractenToevoegen, name='contracten_toevoegen'),
    # zoekt naar de view Eindklanten Page
    path(r'eindklanten_page/', views.EindklantenPage, name='eindklanten'),
    # zoekt naar de view Eindklanten toevoegen
    path(r'eindklanten.toevoegen', views.EindklantToevoegen, name='eindklanten_toevoegen'),
    # zoekt naar de view Eindklanten delete
    path(r'eindklant/delete/<str:id>/', views.EindklantDelete, name='eindklant_delete'),
    # zoekt naar de view Eindklanten Update
    path(r'eindklant/update/<str:pk>/', views.EindklantUpdate.as_view(), name='eindklant_update'),
    # zoekt naar de view Broker Page
    path(r'brokers_page/', views.BrokersPage, name='brokers'),
    # zoekt naar de view Brokers toevoegen
    path(r'brokers.toevoegen', views.BrokersToevoegen, name='brokers_toevoegen'),
    # zoekt naar de view admin page
    path(r'broker/delete/<str:id>/', views.BrokerDelete, name='broker_delete'),
    # zoekt naar de view Broker update
    path(r'broker/update/<str:pk>/', views.BrokerUpdate.as_view(), name='broker_update'),
    # zoekt naar de view contract update
    path(r'contract/update/<str:pk>/', views.ContractenUpdate.as_view, name='contract_update'),
    # zoekt naar de view certificaten
    path(r'certificaten.toevoegen/<str:pk>/', views.CertificatenToevoegen, name='certificaten_toevoegen'),
    # zoekt naar de view lease auto toevoegen
    path(r'lease-auto.toevoegen/<str:pk>/', views.LeaseautosToevoegen, name='lease-auto_toevoegen'),
    # zoekt naar de view lease auto delete
    path(r'lease-auto/delete/<str:id>/', views.LeaseautoDelete, name='lease-auto_delete'),
    # zoekt naar de view contact delete
    path(r'contract/delete/<str:id>/', views.ContractenDelete, name='contract_delete'),
    # zoekt naar de view aanbieding page
    path(r'aanbiedingen_page/', views.AanbiedingenPage, name='aanbiedingen'),
    # zoekt naar de view aanbieding toevoegen
    path(r'aanbiedingen.toevoegen/', views.AanbiedingToevoegen, name='aanbieding_toevoegen'),
    # zoekt naar de view aanbieding update
    path(r'aanbieding/update/<str:pk>/', views.AanbiedingUpdate.as_view(), name='aanbieding_update'),
    # zoekt naar de view aanbieding delete
    path(r'aanbieding/delete/<str:id>/', views.ContractenDelete, name='aanbieding_delete'),
    # zoekt naar de view aan archief aanbiedingen page
    path(r'archief/aanbiedingen_page/', views.ArchiefAanbiedingenPage, name='archief_aanbiedingen'),
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

    path(r'opmerking/broker/<str:pk>/', views.Post_broker, name='opmerking_broker'),

    path(r'todo/create', views.TodoItemCreateView.as_view(), name='create_list'),

    path('opmerkingen/', views.TodoItemListView.as_view(), name='todo_list'),

    path('opmerkingen/update/<str:pk>/', views.TodoItemUpdateView.as_view(), name='update_list'),

    path('opmerkingen/delete/<str:pk>/', views.TodoItemDeleteView.as_view(), name='delete_list'),

    # path(r'opmerking/eindklant/<str:pk>/', views.Post_eindklant, name='opmerking_eindklant'),

    # path('delete_opmerking/<str:pk>/<int:docid>/', views.delete_opmerking, name='delete_opmerking'),

    # path(r'opmerking/medewerker/<str:pk>/', views.OpmerkingMedewerker, name='editor'),


    # dit is de download path die hij zodat je de download van de betreffende persoon alleen kan downloaden op wie je klinkt en waar django het weg schrijft.
    url(r'^download/<str:pk>/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),



]
# Deze "routes" van de static en de media url voor als er iets geupload wordt.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
