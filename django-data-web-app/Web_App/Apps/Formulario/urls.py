# Formulario/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('<slug:evento_slug>/registro/', views.registrar_evento, name='registro_evento'),
]