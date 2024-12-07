import pytest
from HotelApp.models import Usuario  

@pytest.mark.django_db 
def test_usuario_registrado():
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


    try:
        usuario_en_db = Usuario.objects.get(correo="juan@example.com")
        assert usuario_en_db is not None  
        assert usuario_en_db == usuario  
    except Usuario.DoesNotExist:
        pytest.fail("El usuario no fue encontrado en la base de datos")

@pytest.mark.django_db
def test_no_existe_usuario():
    try:
        Usuario.objects.get(correo="noexiste@example.com")
        pytest.fail("El usuario no debería existir en la base de datos")
    except Usuario.DoesNotExist:
        pass  
