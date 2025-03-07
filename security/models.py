from django.db import models

# Create your models here.

class Alert(models.Model):
   
    triggered_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se activó la alarma")
    