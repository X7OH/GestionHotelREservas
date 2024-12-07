import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_usuario_login_exitoso(client):
    """
    Verifica que un usuario pueda iniciar sesión correctamente.
    """
    # Crear un usuario en la base de datos
    usuario = User.objects.create_user(
        username="testuser",
        password="securepassword123",
        email="testuser@example.com"
    )

    # Enviar una solicitud de inicio de sesión
    url_login = reverse("login")  # Ajusta al nombre de tu vista de login
    response = client.post(url_login, {"username": "testuser", "password": "securepassword123"})

    # Verificar el estado HTTP de la respuesta
    assert response.status_code == 200

    # Verificar que el mensaje de éxito aparece en la respuesta
    assert "Inicio de sesión exitoso" in response.content.decode()


@pytest.mark.django_db
def test_usuario_login_fallido(client):
    """
    Verifica que un usuario no pueda iniciar sesión con credenciales incorrectas.
    """
    # Crear un usuario en la base de datos
    User.objects.create_user(
        username="testuser",
        password="securepassword123",
        email="testuser@example.com"
    )

    # Enviar una solicitud de inicio de sesión con credenciales incorrectas
    url_login = reverse("login")  # Ajusta al nombre de tu vista de login
    response = client.post(url_login, {"username": "testuser", "password": "wrongpassword"})

    # Verificar el estado HTTP de la respuesta
    assert response.status_code == 200

    # Verificar que el mensaje de error aparece en la respuesta
    assert "Credenciales inválidas" in response.content.decode()
