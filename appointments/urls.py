from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.book, name='book'),
    path('success/', views.success, name='success'),
]
