import pytest
from HotelApp.models import Usuario 
@pytest.mark.django_db 
def test_crear_usuario():
    # Crear un usuario
    usuario = Usuario.objects.create(
        nombre="Juan",
        correo="juan@example.com",
        contraseña="securepassword123",
        Ciudad="Quito",
        rol="Admin"
    )

    assert usuario.id is not None  
    assert usuario.nombre == "Juan"
    assert usuario.correo == "juan@example.com"
    assert usuario.contraseña == "securepassword123"
    assert usuario.Ciudad == "Quito"
    assert usuario.rol == "Admin"

    usuario_en_db = Usuario.objects.get(correo="juan@example.com")
    assert usuario_en_db == usuario
