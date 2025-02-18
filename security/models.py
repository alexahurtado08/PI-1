from django.db import models

# Create your models here.

class Alert(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Activa'),
        ('RESOLVED', 'Resuelta'),
    ]
    sensor_id = models.CharField(max_length=100, help_text="ID del sensor que activó la alarma")
    triggered_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se activó la alarma")
    location = models.CharField(max_length=255, help_text="Ubicación del sensor")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE', help_text="Estado de la alarma")
    additional_info = models.TextField(blank=True, null=True, help_text="Información adicional del evento")