from django.urls import path
from .views import LinkTelegramAPIView

urlpatterns = [
    path("link-telegram/", LinkTelegramAPIView.as_view(), name="link-telegram"),
]
