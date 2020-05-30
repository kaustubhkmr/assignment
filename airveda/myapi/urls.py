from django.urls import path
from .views import device_list, device_detail, get_readings
from django.shortcuts import redirect

urlpatterns = [
    path('',lambda request: redirect('devices/', permanent=False)),
    path('devices/', device_list),
    path('devices/<int:pk>/', device_detail),
    path('devices/<str:device>/readings/<str:parameter>/',get_readings)
]