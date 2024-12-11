import pytest
from HotelApp.models import Habitacion

@pytest.mark.django_db
def test_crear_habitacion():
    # Crear una habitación
    habitacion = Habitacion.objects.create(
        piso=2,
        nhabitacion=201,
        Estado=False  # Estado inicial de la habitación
    )

    # Verificar que la habitación fue creada correctamente
    assert habitacion.id is not None
    assert habitacion.piso == 2
    assert habitacion.nhabitacion == 201
    assert habitacion.Estado is False

    # Verificar que está almacenada en la base de datos
    habitacion_en_db = Habitacion.objects.get(nhabitacion=201, piso=2)
    assert habitacion_en_db == habitacion
