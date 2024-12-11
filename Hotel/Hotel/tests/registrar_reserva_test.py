import pytest
from django.urls import reverse
from HotelApp.models import Reservas, Habitacion

@pytest.mark.django_db
def test_registrar_reserva_exitoso(client):

    Habitacion.objects.create(piso=3, nhabitacion=301, Estado=False)
    
    url = reverse('Reservas') 
    data = {
        'nombre': 'Alice Doe',
        'correo': 'alice.doe@example.com',
        'contraseña': 'securepassword123',
        'piso': 3,
        'nhabitacion': 301
    }
    response = client.post(url, data, content_type="application/json")
    
    assert response.status_code == 201
    assert response.json() == {'message': 'Reserva realizada correctamente'}
    reserva = Reservas.objects.get(correo='alice.doe@example.com')
    assert reserva.nombre == 'Alice Doe'
    assert reserva.piso == 3
    assert reserva.nhabitacion == 301

@pytest.mark.django_db
def test_registrar_reserva_habitacion_no_existe(client):
    url = reverse('Reservas')
    data = {
        'nombre': 'Bob Smith',
        'correo': 'bob.smith@example.com',
        'contraseña': 'password123',
        'piso': 4,
        'nhabitacion': 401
    }
    response = client.post(url, data, content_type="application/json")
    
    assert response.status_code == 404
    assert response.json() == {'message': 'La habitación no existe'}

@pytest.mark.django_db
def test_registrar_reserva_habitacion_ocupada(client):

    Habitacion.objects.create(piso=5, nhabitacion=501, Estado=True)
    
    url = reverse('Reservas')
    data = {
        'nombre': 'Charlie Brown',
        'correo': 'charlie.brown@example.com',
        'contraseña': 'password123',
        'piso': 5,
        'nhabitacion': 501
    }
    response = client.post(url, data, content_type="application/json")
    
    assert response.status_code == 400
    assert response.json() == {'message': 'La habitación está ocupada'}
