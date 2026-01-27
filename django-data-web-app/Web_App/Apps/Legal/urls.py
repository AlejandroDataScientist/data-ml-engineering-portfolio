# Legal/urls.py
from django.urls import path
from .views import politicas_privacidad

app_name = 'Legal'  # para uso de namespacing si lo deseas

urlpatterns = [
    path('', politicas_privacidad, name='politicas'),
]
