"""
URL configuration for Hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HotelApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('Registro', views.Registro, name="Registro"),
    path('VerUsuarios', views.VerUsuarios, name="VerUsuarios"),
    path('Reservas', views.registrar_reserva, name="Reservas"),
    path('Habitacion', views.registrar_habitacion, name="Habitacion"),
    path('login/', views.login, name='login'),
    path('VerHabitaciones/', views.VerHabitaciones, name='VerHabitaciones'),
    path('VerReservas/', views.VerReservas, name='VerReservas'),
    
    
]
