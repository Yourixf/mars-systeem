from django.contrib import admin
from django.urls import path
from project1 import views

app_name = 'project1'

urlpatterns = [

    path(r'', views.index, name='home'),

    path(r'admin/', admin.site.urls),

    # dit is het pad voor de medewerkers pagina
    path(r'medewerkers/', views.medewerkers, name='medewerkers'),

    # Dit is de URL naar medewerker details
    path(r'medewerkers/<medewerkers_id>/', views.detail_medewerkers, name='details'),

    path(r'login/', views.login, name='login'),

]
