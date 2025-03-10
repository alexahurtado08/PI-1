from django.shortcuts import render
from django.http import HttpResponse
from .models import Alert
from django.shortcuts import render
from .models import PersonalAutorizado


# Create your views here.

def home(request):
    return render(request, 'home.html')

def alerts(request):
    alertass=Alert.objects.all()
    return render(request, 'alerts.html')

def personal_autorizado(request):
    personal = PersonalAutorizado.objects.all()
    return render(request, 'personal_autorizado.html', {'personal': personal})
