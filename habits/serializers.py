from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("user", "created_at")

    def validate(self, attrs):
        reward = attrs.get("reward")
        related_habit = attrs.get("related_habit")
        is_pleasant = attrs.get("is_pleasant")
        execution_time = attrs.get("execution_time")
        periodicity = attrs.get("periodicity")

        if reward and related_habit:
            raise serializers.ValidationError(
                "Нельзя одновременно указывать вознаграждение и связанную привычку."
            )

        if execution_time and execution_time > 120:
            raise serializers.ValidationError(
                "Время выполнения должно быть не больше 120 секунд."
            )

        if related_habit and not related_habit.is_pleasant:
            raise serializers.ValidationError(
                "Связанной может быть только приятная привычка."
            )

        if is_pleasant and reward:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения."
            )

        if is_pleasant and related_habit:
            raise serializers.ValidationError(
                "У приятной привычки не может быть связанной привычки."
            )

        if periodicity and periodicity > 7:
            raise serializers.ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            )

        return attrs
