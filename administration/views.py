from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Alert

from .google_sheets import GoogleSheet
from datetime import date
import json
import uuid

file_name_gs = "credenciales.json"
google_sheet = "Pruebas"
sheet_name = "Hoja 1"

def alerts(request):
    return render(request, 'alerts.html')

def alertas_json(request):
    google = GoogleSheet(file_name_gs, google_sheet, sheet_name)
    alertas = google.get_all_values()

    return JsonResponse(alertas, safe=False)


def alert_notification(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Aquí puedes hacer lo que quieras con los datos: guardarlos, imprimirlos, etc.
            print("Datos recibidos:", data)

            # Ejemplo: guardar como Alerta si tienes un modelo
            # Alerta.objects.create(**data)

            return JsonResponse({'status': 'success', 'message': 'Dato recibido correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Solo se permite POST'}, status=405)



