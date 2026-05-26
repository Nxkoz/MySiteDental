from django.contrib import admin
from .models import Service, Appointment


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_from', 'order')
    ordering = ('order',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'service', 'date')
    search_fields = ('name', 'phone', 'email')
    list_editable = ('status',)
