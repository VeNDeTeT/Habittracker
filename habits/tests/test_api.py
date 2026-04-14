import pytest
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_habit_via_api(mocker):
    User = get_user_model()
    user = User.objects.create_user(username="api_user", password="testpass")
    client = APIClient()
    client.force_authenticate(user=user)

    now = timezone.localtime().replace(second=0, microsecond=0)

    data = {
        "place": "Дом",
        "time": now.time().strftime("%H:%M:%S"),
        "action": "Тест через API",
        "is_pleasant": False,
        "periodicity": 1,
        "reward": "",
        "execution_time": 60,
        "is_public": False,
    }

    response = client.post("/api/habits/", data, format="json")
    assert response.status_code == 201
    body = response.json()
    assert body["action"] == "Тест через API"
    assert body["user"] == user.id
