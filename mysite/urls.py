from django.contrib import admin
from django.urls import path, include
from project1 import views



app_name = 'project1'

urlpatterns = [
    path(r'register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path(r'', views.Index, name='index'),
    # dit is het pad voor de medewerkers pagina

    path(r'medewerkers/', views.MedewerkersPage, name='medewerkers'),
    #path(r'medewerkers/', views.MedewerkersView.as_view(), name='medewerkers'),
    # Dit is de URL naar medewerker details
    path(r'medewerkers/<str:pk>/', views.Detail, name='details'),

 #path(r'medewerkers/add/', views.MedewerkersCreate.as_view(), name='medewerker/add'),
    path('lease.autos.detail/<str:pk>/', views.Leaseautosdetail, name='lease.autos.detail'),
    path('contracten.detail/<str:pk>/', views.Contractendetail, name='contracten.detail'),
    path('certificaten.detail/<str:pk>/', views.Certificatendetail, name='certificaten.detail'),

    path(r'admin/', admin.site.urls),
]
