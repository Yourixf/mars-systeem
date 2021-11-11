from django.contrib import admin
from django.urls import path, include
from project1 import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'project1'

urlpatterns = [
#zoekt naar de view registerPage
    path(r'register/', views.registerPage, name='register'),
#zoekt naar de view loginPage
    path('login/', views.loginPage, name="login"),
#zoekt naar de view logoutUser
    path('logout/', views.logoutUser, name="logout"),
#zoekt naar de view Index
    path(r'', views.Index, name='index'),
#zoekt naar de view MedewerkersPage
    path(r'medewerkers/', views.MedewerkersPage, name='medewerkers'),
#zoekt naar de view Detail
    path(r'medewerkers/<str:pk>/', views.Detail, name='details'),
#zoekt naar de view Leaseautosdetail
    path('lease.autos.detail/<str:pk>/', views.Leaseautosdetail, name='lease.autos.detail'),
#zoekt naar de view Contractendetail
    path('contracten.detail/<str:pk>/', views.Contractendetail, name='contracten.detail'),
#zoekt naar de admin page
    path(r'admin/', admin.site.urls),

    path('foto/toevoegen/<str:pk>', views.Medewerker_foto, name='medewerker-foto'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)