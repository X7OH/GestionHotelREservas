import pytest
from django.urls import reverse
from HotelApp.models import Reservas

@pytest.mark.django_db
def test_ver_reservas(client):
    # Crear datos de prueba para reservas
    Reservas.objects.create(
        nombre="Juan Perez",
        correo="juan.perez@example.com",
        contraseña="securepassword",
        piso=2,
        nhabitacion=101
    )
    Reservas.objects.create(
        nombre="Ana López",
        correo="ana.lopez@example.com",
        contraseña="securepassword",
        piso=3,
        nhabitacion=202
    )

    # Realizar una solicitud GET al endpoint de Ver Reservas
    url = reverse("VerReservas")  # Asegúrate de que el nombre de la vista coincide con tu configuración
    response = client.get(url)

    # Validar la respuesta
    assert response.status_code == 200
    data = response.json()
    assert "reservas" in data
    assert len(data["reservas"]) == 2  # Validar que se devuelvan 2 reservas
    assert data["reservas"][0]["nombre"] == "Juan Perez"
    assert data["reservas"][1]["nombre"] == "Ana López"
