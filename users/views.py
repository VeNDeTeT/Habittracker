from rest_framework import generics, permissions
from .models import User
from .serializers import UserRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]
