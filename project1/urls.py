from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('views', views.index, name='index'),

    # /admin/project1/medewerkers/
    path('view', views.a, name='a'),

]
