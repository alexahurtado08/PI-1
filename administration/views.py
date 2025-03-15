from django.shortcuts import render
from django.http import HttpResponse
from .models import Alert

def alerts(request):
    alertass=Alert.objects.all()
    return render(request, 'alerts.html', {'alertass':alertass})
