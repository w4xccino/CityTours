from django.db import models
from django.db.models.base import Model

# Create your models here.

class Lugar(models.Model):
  nombre = models.CharField(max_length=60)
  descripcion = models.TextField()
  imagen = models.ImageField(null = True, blank = True, upload_to = "images/")

  def __str__(self):
    return self.nombre