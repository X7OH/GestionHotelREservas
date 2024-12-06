# conftest.py
import pytest
from HotelApp import Usuario

@pytest.fixture
def user():
    return Usuario.objects.create_user(username='testuser', password='testpass')

# test_views.py
def test_login(user, client):
    url = reverse('login')
    response = client.post(url, {'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert b'Bienvenido, testuser' in response.content
