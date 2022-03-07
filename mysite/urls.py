from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from project1 import views

app_name = 'project1'

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
    # zoekt naar de view Detail
    path(r'medewerkers/<str:pk>/', views.Detail, name='details'),
    # zoekt naar de view Leaseautosdetail
    path('lease.autos.detail/<str:pk>/', views.Leaseautosdetail, name='lease.autos.detail'),
    # zoekt naar de view Contractendetail
    path('contracten.detail/<str:pk>/', views.Contractendetail, name='contracten.detail'),
    # zoekt naar de admin page
    path(r'admin/', admin.site.urls),

    path(r'foto_toevoegen/<str:pk>/', views.Foto_Toevoegen, name='foto_toevoegen'),

    path(r'medewerker.toevoegen/', views.MedewerkersToevoegen, name='medewerker_toevoegen'),

    path(r'medewerker/delete/<str:pk>/', views.MedewerkerDelete, name='medewerker_delete'),

    path(r'medewerker/update/<str:pk>/', views.MedewerkerUpdate.as_view(), name='medewerker_update'),

    path(r'contracten.toevoegen/<str:pk>/', views.ContractenToevoegen, name='contracten_toevoegen'),

    path(r'eindklanten_page/', views.EindklantenPage, name='eindklanten'),

    path(r'eindklanten.toevoegen', views.EindklantToevoegen, name='eindklanten_toevoegen'),

    path(r'eindklant/delete/<str:id>/', views.EindklantDelete, name='eindklant_delete'),

    path(r'eindklant/update/<str:pk>/', views.EindklantUpdate.as_view(), name='eindklant_update'),

    path(r'brokers_page/', views.BrokersPage, name='brokers'),

    path(r'brokers.toevoegen', views.BrokersToevoegen, name='brokers_toevoegen'),

    path(r'broker/delete/<str:id>/', views.BrokerDelete, name='broker_delete'),

    path(r'broker/update/<str:pk>/', views.BrokerUpdate.as_view(), name='broker_update'),

    path(r'contract/update/<str:pk>/', views.ContractenUpdate.as_view(), name='contract_update'),

    path(r'certificaten.toevoegen/<str:pk>/', views.CertificatenToevoegen, name='certificaten_toevoegen'),

    path(r'lease-auto.toevoegen/<str:pk>/', views.LeaseautosToevoegen, name='lease-auto_toevoegen'),

    path(r'lease-auto/delete/<str:id>/', views.LeaseautoDelete, name='lease-auto_delete'),

    path(r'contract/delete/<str:id>/', views.ContractenDelete, name='contract_delete'),

    path(r'aanbiedingen_page/', views.AanbiedingenPage, name='aanbiedingen'),

    path(r'aanbiedingen.toevoegen/', views.AanbiedingToevoegen, name='aanbieding_toevoegen'),

    path(r'aanbieding/update/<str:pk>/', views.AanbiedingUpdate.as_view(), name='aanbieding_update'),

    path(r'aanbieding/delete/<str:id>/', views.ContractenDelete, name='aanbieding_delete'),

    path(r'archief/aanbiedingen_page/', views.ArchiefAanbiedingenPage, name='archief_aanbiedingen'),

    path(r'broker/<str:pk>/', views.BrokerDetail, name='broker_detail'),

    path(r'eindklant/<str:pk>/', views.EindklantDetail, name='eindklant_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
