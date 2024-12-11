import pytest
from django.urls import reverse
from HotelApp.models import Habitacion

@pytest.mark.django_db
def test_ver_habitaciones(client):
    # Crear datos de prueba para habitaciones
    Habitacion.objects.create(piso=1, nhabitacion=101, Estado=False)
    Habitacion.objects.create(piso=2, nhabitacion=202, Estado=True)

    # Realizar una solicitud GET al endpoint de Ver Habitaciones
    url = reverse("VerHabitaciones")  # Asegúrate de que el nombre de la vista coincide con tu configuración
    response = client.get(url)

    # Validar la respuesta
    assert response.status_code == 200
    data = response.json()
    assert "habitaciones" in data
    assert len(data["habitaciones"]) == 2  # Validar que se devuelvan 2 habitaciones
    assert data["habitaciones"][0]["piso"] == 1
    assert data["habitaciones"][1]["Estado"] == True
