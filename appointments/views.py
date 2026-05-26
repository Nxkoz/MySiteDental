from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Appointment
from .forms import AppointmentForm


def book(request):
    services = Service.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша запис прийнята! Ми зв\'яжемося з вами для підтвердження.')
            return redirect('appointments:success')
    else:
        service_id = request.GET.get('service')
        form = AppointmentForm(initial={'service': service_id} if service_id else {})
    return render(request, 'appointments/book.html', {'form': form, 'services': services})


def success(request):
    return render(request, 'appointments/success.html')
