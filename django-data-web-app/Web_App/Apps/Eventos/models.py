from django.db import models
from django.utils.text import slugify

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=200, default='Lugar pendiente') 
    slug = models.SlugField(unique=True, blank=True)
    imagen = models.ImageField(upload_to='eventos_imagenes/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


