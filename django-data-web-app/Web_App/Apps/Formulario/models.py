from Apps.Eventos.models import Evento  # Importa Evento para la relación
from django.db import models

class RegistroEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='registros')  # ← Esta línea es clave
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    identificacion = models.FileField(upload_to='identificaciones/', null=True, blank=True)
    logo = models.FileField(upload_to='logos/', null=True, blank=True)
    comentario = models.TextField(blank=True)

    acepta_politicas = models.BooleanField(default=False)
    desea_recibir_noticias = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({self.correo})"