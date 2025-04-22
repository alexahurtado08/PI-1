from django.db import models

class AuthorizedPersonnel(models.Model):
    mensaje = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='authorized_personnel/')

    def __str__(self):
        return self.nombre
    