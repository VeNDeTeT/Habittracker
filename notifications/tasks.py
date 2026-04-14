from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from notifications.models import TelegramProfile
from notifications.services import send_telegram_message


@shared_task
def send_test_message():
    """
    Разовая проверка, что Celery + Telegram работают.
    Вызывается вручную через .delay().
    """
    now = timezone.localtime().strftime("%Y-%m-%d %H:%M:%S")

    # Шлём всем привязанным профилям
    for profile in TelegramProfile.objects.all():
        text = f"Тест от Celery. Время: {now}"
        send_telegram_message(profile.chat_id, text)


@shared_task
def send_habit_reminders():
    """
    Периодическая задача (каждую минуту).
    Находит привычки, которым сейчас нужно отправить напоминание,
    и шлёт сообщение в Telegram пользователю.
    """
    now = timezone.localtime()
    today = now.date()
    current_hour = now.hour
    current_minute = now.minute

    # Берём только полезные привычки (is_pleasant=False),
    # у которых время совпадает с текущим часом и минутой.
    habits = Habit.objects.filter(
        is_pleasant=False,
        time__hour=current_hour,
        time__minute=current_minute,
    )

    for habit in habits:
        # Проверяем периодичность по дням
        days_passed = (today - habit.created_at.date()).days
        if days_passed < 0:
            continue

        if days_passed % habit.periodicity != 0:
            continue

        # Берём TelegramProfile пользователя
        try:
            telegram_profile = habit.user.telegram_profile
        except TelegramProfile.DoesNotExist:
            # У пользователя нет chat_id — просто пропускаем
            continue

        text = (
            f"Напоминание о привычке\n\n"
            f"Место: {habit.place}\n"
            f"Время: {habit.time.strftime('%H:%M')}\n"
            f"Действие: {habit.action}"
        )

        send_telegram_message(telegram_profile.chat_id, text)
