import pytest
from django.utils import timezone

from django.contrib.auth import get_user_model
from habits.models import Habit
from notifications.models import TelegramProfile
from notifications.tasks import send_habit_reminders


@pytest.mark.django_db
def test_send_habit_reminders_sends_message_to_telegram(mocker):
    User = get_user_model()

    # Пользователь + TelegramProfile
    user = User.objects.create_user(username="admin_test", password="testpass")
    TelegramProfile.objects.create(user=user, chat_id="580684609")

    # Время совпадает с текущими часами/минутами
    now = timezone.localtime()
    reminder_time = now.replace(second=0, microsecond=0).time()

    habit = Habit.objects.create(
        user=user,
        place="Дом",
        time=reminder_time,
        action="Тест из задачи",
        is_pleasant=False,
        periodicity=1,
        execution_time=60,
        is_public=False,
    )

    # created_at = сегодня
    habit.created_at = now
    habit.save()

    # Мокаем отправку в Telegram
    mocked_send = mocker.patch("notifications.tasks.send_telegram_message")

    # Запускаем задачу синхронно
    send_habit_reminders()

    mocked_send.assert_called_once()
    args, kwargs = mocked_send.call_args
    assert args[0] == "580684609"
    assert "Тест из задачи" in args[1]
