from django.conf import settings
from django.db import models


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="Пользователь",
    )
    place = models.CharField("Место", max_length=255)
    time = models.TimeField("Время")
    action = models.CharField("Действие", max_length=255)

    is_pleasant = models.BooleanField(
        "Приятная привычка",
        default=False,
        help_text="Если включено — это приятная, а не полезная привычка",
    )

    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Связанная привычка",
        related_name="related_to",
        help_text="Связать можно только с приятной привычкой",
    )

    periodicity = models.PositiveSmallIntegerField(
        "Периодичность, дней",
        default=1,
        help_text="Нельзя реже, чем раз в 7 дней",
    )

    reward = models.CharField(
        "Вознаграждение",
        max_length=255,
        blank=True,
        null=True,
    )

    execution_time = models.PositiveSmallIntegerField(
        "Время на выполнение, сек",
        help_text="Не больше 120 секунд",
    )

    is_public = models.BooleanField(
        "Публичная",
        default=False,
        help_text="Если включено — видна другим пользователям",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.action} в {self.time}"
