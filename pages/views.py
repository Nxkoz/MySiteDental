from django.shortcuts import render
from appointments.models import Service


def home(request):
    services = Service.objects.all()[:6]
    return render(request, 'pages/home.html', {'services': services})


def services(request):
    all_services = Service.objects.all()
    return render(request, 'pages/services.html', {'services': all_services})


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')
