from django.db import models


# Create your models here.

class Alert(models.Model):
   
    triggered_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se activó la alarma")
    active_boolean = models.BooleanField(default=True, help_text="Indica si la alarma está activa")
    
class Fotografia(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/')
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fotografía {self.id}"


class AuthorizedPersonnel(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='authorized_personnel/')

    def __str__(self):
        return self.nombre