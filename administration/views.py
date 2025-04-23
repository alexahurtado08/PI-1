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
    alerta = google.get_last_row()
    return JsonResponse(alerta, safe=False)





