from rest_framework import viewsets, generics, permissions
from .models import Habit
from .serializers import HabitSerializer
from .pagination import HabitPagination
from .permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = HabitPagination
    queryset = Habit.objects.filter(is_public=True)
