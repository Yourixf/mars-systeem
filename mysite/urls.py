from django.contrib import admin
from django.urls import path
from project1 import views

app_name = 'project1'

urlpatterns = [

    path(r'', views.IndexView.as_view(), name='home'),

    path(r'admin/', admin.site.urls),

    # dit is het pad voor de medewerkers pagina
    path(r'medewerkers/', views.MedewerkersView.as_view(), name='medewerkers'),

    # Dit is de URL naar medewerker details
    path(r'medewerkers/<pk>/', views.DetailView.as_view(), name='details'),

    path(r'login/', views.UserFormView.as_view(), name='login'),

    path(r'medewerkers/add/', views.MedewerkersCreate.as_view(), name= 'medewerker/add'),

]
