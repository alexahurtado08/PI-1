from django.db import models

class Fotografia(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/')
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Fotografía {self.id}"


class Computer(models.Model):
    model = models.CharField(max_length=100)
    purchase_date = models.DateField()  # 👈 Este debe ser un DateField
    previous_repairs = models.TextField(blank=True, null=True)