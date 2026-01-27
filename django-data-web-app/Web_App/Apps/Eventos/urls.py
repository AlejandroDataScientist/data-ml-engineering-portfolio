# eventos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventos_home, name='eventos_home'),
    path('<slug:evento_slug>/registro/', views.registro_evento, name='registro_evento'),  # <- Esta línea es clave
]
