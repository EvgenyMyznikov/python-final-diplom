import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_unauthorized_request(api_client):
    url = reverse('shops-list')
    response = api_client.get(url)
    assert response.status_code == 403
