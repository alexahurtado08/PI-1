from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Alert

from .google_sheets import GoogleSheet
from datetime import date
import json
import uuid

file_name_gs = "credenciales.json"
google_sheet = "Datos SafeDesk"
sheet_name = "Hoja 1"

def alerts(request):
    return render(request, 'alerts.html')

def alertas_json(request):
    google = GoogleSheet(file_name_gs, google_sheet, sheet_name)
    alertas = google.get_all_values()

    return JsonResponse(alertas, safe=False)

def update_alert(request):
    google = GoogleSheet(file_name_gs, google_sheet, sheet_name)
    alerta_data = google.get_last_row()  # Suponiendo que devuelve una lista

    if alerta_data:
        alerta, created = Alert.objects.get_or_create(pk=1)  # Solo una alerta
        alerta.fecha = alerta_data[0]
        alerta.mensaje = alerta_data[2]
        alerta.estado = alerta_data[3]
        alerta.save()

        return JsonResponse(alerta_data, safe=False)
    else:
        return JsonResponse({'error': 'No se encontró alerta'}, status=404)





