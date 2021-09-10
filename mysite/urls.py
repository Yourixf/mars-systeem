"""mysite URL Configuration

"""
from django.contrib import admin
from django.urls import path

from project1 import views

urlpatterns = [
    path(r'home/', views.index, name='index'),
    path(r'admin/', admin.site.urls),
    path(r'medewerkers/', views.a, name='a'),
]

