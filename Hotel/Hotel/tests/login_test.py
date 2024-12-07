import pytest
from django.urls import reverse
from HotelApp.models import Usuario
from django.contrib.auth.hashers import make_password
import os
import django

# Asegúrate de que el entorno de Django apunte al archivo settings.py correcto
os.environ['DJANGO_SETTINGS_MODULE'] = 'Hotel.settings'  # 'Hotel' es el nombre de tu proyecto y 'settings' es el archivo de configuración
django.setup()


@pytest.fixture
def usuario_creado(db):
    """Crear un usuario en la base de datos para las pruebas."""
    return Usuario.objects.create(
        nombre="Juan Perez",
        correo="juan.perez@example.com",
        contraseña=make_password("12345678"),  # Encriptar contraseña
        Ciudad="Quito",
        rol="Cliente"
    )

@pytest.mark.django_db
def test_login_exitoso(client, usuario_creado):
    """Probar un inicio de sesión exitoso."""
    url = reverse('login')  # Reemplaza 'login' con el nombre de tu vista si usas `path()` o `name`.
    data = {
        "correo": "juan.perez@example.com",
        "contraseña": "12345678"
    }

    response = client.post(url, data, content_type="application/json")

    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido juan.perez@example.com"}


@pytest.mark.django_db
def test_login_usuario_no_encontrado(client):
    """Probar intento de inicio de sesión con usuario inexistente."""
    url = reverse('login')
    data = {
        "correo": "no.existe@example.com",
        "contraseña": "12345678"
    }

    response = client.post(url, data, content_type="application/json")

    assert response.status_code == 404
    assert response.json() == {"error": "Usuario no encontrado"}


@pytest.mark.django_db
def test_login_contraseña_incorrecta(client, usuario_creado):
    """Probar inicio de sesión con contraseña incorrecta."""
    url = reverse('login')
    data = {
        "correo": "juan.perez@example.com",
        "contraseña": "contraseña_incorrecta"
    }

    response = client.post(url, data, content_type="application/json")

    assert response.status_code == 401
    assert response.json() == {"error": "Contraseña incorrecta"}
