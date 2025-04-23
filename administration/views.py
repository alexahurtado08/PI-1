from django.http import JsonResponse
from .models import Alert, Computer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .import ComputerForm
from .ComputerForm import ComputerForm


from django.shortcuts import get_object_or_404

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
    
# Verifica si pertenece al grupo "admin"
def es_admin(user):
    return user.groups.filter(name='admin').exists()

def computers_view(request):
    computadoras = Computer.objects.all()  # Obtener todas las computadoras
    return render(request, 'computers.html', {'computadoras': computadoras})

@login_required
@user_passes_test(es_admin)
def registrar_computadora(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('computadoras')  
    else:
        form = ComputerForm()
    return render(request, 'registrar_computadora.html', {'form': form})



@login_required
@user_passes_test(es_admin)
def eliminar_computadora(request, computadora_id):
    computadora = get_object_or_404(Computer, id=computadora_id)
    computadora.delete()
    return redirect('computadoras')




