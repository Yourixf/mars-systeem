from django.contrib import admin
from django.urls import path, include
from project1 import views


app_name = 'project1'

urlpatterns = [

    path(r'', views.IndexView.as_view(), name='index'),

    path(r'admin/', admin.site.urls),

    # dit is het pad voor de medewerkers pagina
    path(r'medewerkers/', views.MedewerkersView.as_view(), name='medewerkers'),

    # Dit is de URL naar medewerker details
    path(r'medewerkers/<pk>/', views.DetailView.as_view(), name='details'),

    path(r'register/', views.UserFormView.as_view(), name='register'),

    path(r'medewerkers/add/', views.MedewerkersCreate.as_view(), name='medewerker/add'),

    path('login/', views.login, name="login"),

    path('logout/', views.logout, name="logout"),

    path('home/', views.home, name="home"),

    path('lease.autos.detail/<pk>/', views.LeaseautosdetailView.as_view(), name='lease.autos.detail'),

    path('contracten.detail/<pk>/', views.ContractenCertificatendetailView.as_view(), name='contracten.detail'),

    path('certificaten.detail/<pk>/', views.CertificatendetailView.as_view(), name='certificaten.detail'),
]
