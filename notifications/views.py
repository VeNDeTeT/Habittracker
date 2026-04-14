from rest_framework import permissions, status, views
from rest_framework.response import Response
from .models import TelegramProfile


class LinkTelegramAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        chat_id = request.data.get("chat_id")
        if not chat_id:
            return Response(
                {"chat_id": "Обязательное поле."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        profile, _ = TelegramProfile.objects.update_or_create(
            user=request.user,
            defaults={"chat_id": chat_id},
        )
        return Response({"detail": "Telegram успешно привязан."})
