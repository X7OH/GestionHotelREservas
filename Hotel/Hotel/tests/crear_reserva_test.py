import pytest
from HotelApp.models import Reservas, Habitacion

@pytest.mark.django_db
def test_crear_reserva():
    # Crear una habitación para asociar a la reserva
    habitacion = Habitacion.objects.create(
        piso=3,
        nhabitacion=301,
        Estado=False
    )

    # Crear una reserva asociada a la habitación
    reserva = Reservas.objects.create(
        nombre="Carlos Pérez",
        correo="carlos.perez@example.com",
        contraseña="password123",
        piso=3,
        nhabitacion=301
    )

    # Verificar que la reserva fue creada correctamente
    assert reserva.id is not None
    assert reserva.nombre == "Carlos Pérez"
    assert reserva.correo == "carlos.perez@example.com"
    assert reserva.contraseña == "password123"
    assert reserva.piso == 3
    assert reserva.nhabitacion == 301

    # Verificar que la habitación quedó ocupada
    habitacion.refresh_from_db()  # Refrescar la instancia de la base de datos
    assert habitacion.Estado is False  # (Cambia si deseas modificar su estado en tu lógica)
