from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    fecha = models.DateField(null=False)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"
    
class Participantes(models.Model):
    evento = models.ForeignKey(Evento, related_name='participantes',  on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=False)
    correo = models.EmailField(unique=True, null=False)
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return {self.nombre}
