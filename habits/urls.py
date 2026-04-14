from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, PublicHabitListAPIView

router = DefaultRouter()
router.register(r"habits", HabitViewSet, basename="habits")

urlpatterns = [
    path("", include(router.urls)),
    path("public-habits/", PublicHabitListAPIView.as_view(), name="public-habits"),
]
