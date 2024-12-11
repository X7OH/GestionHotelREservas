import pytest
from django.urls import reverse
from HotelApp.models import Habitacion

@pytest.mark.django_db
def test_registrar_habitacion_exitoso(client):
    url = reverse('Habitacion') 
    data = {
        'piso': 2,
        'nhabitacion': 202,
        'Estado': False
    }
    response = client.post(url, data, content_type="application/json")
    
    assert response.status_code == 201
    assert response.json() == {'message': 'Habitación registrada correctamente'}
    habitacion = Habitacion.objects.get(nhabitacion=202)
    assert habitacion.piso == 2
    assert habitacion.Estado is False

@pytest.mark.django_db
def test_registrar_habitacion_faltan_campos(client):
    url = reverse('Habitacion')
    data = {
        'nhabitacion': 203  # Falta 'piso'
    }
    response = client.post(url, data, content_type="application/json")
    
    assert response.status_code == 400
    assert response.json() == {'message': 'Los campos piso y nhabitacion son obligatorios'}
