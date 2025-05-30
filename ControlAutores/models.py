from django.db import models
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name_plural = "Autores"

# Create your models here.
