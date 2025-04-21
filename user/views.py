from django.shortcuts import render
from django.http import HttpResponse
from .models import AuthorizedPersonnel

def home(request):
    return render(request, 'home.html')


def personnel(request):
    personal = AuthorizedPersonnel.objects.all()
    return render(request, 'personnel.html', {'personal': personal})


def about(request):
    return render(request, 'about.html')

def landing_page(request):
    return render(request, 'landing.html')

