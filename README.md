# HabitTracker API

Учебный проект на Django + DRF + Celery + Telegram для трекинга привычек и отправки напоминаний в Telegram.

## Стек

- Python 3.12
- Django 6
- Django REST Framework
- PostgreSQL
- Redis
- Celery 5
- Docker Compose
- pytest, pytest-django, pytest-cov
- flake8

## Основной функционал

- Регистрация и аутентификация пользователей.
- Создание, просмотр, обновление и удаление привычек.
- Разделение привычек на полезные и приятные.
- Публичные привычки, доступные другим пользователям.
- Пагинация списка привычек.
- Интеграция с Telegram-ботом:
  - привязка Telegram-профиля (`chat_id`) к пользователю;
  - отправка напоминаний в личный чат с ботом.
- Отложенные задачи через Celery:
  - периодическая задача `send_habit_reminders` раз в минуту проверяет привычки
    и отправляет напоминания в Telegram.

## Запуск проекта через Docker Compose

### 1. Клонирование репозитория

```bash
git clone https://github.com/VeNDeTeT/Habittracker.git
cd Habittracker
```

### 2. Переменные окружения

Создайте файл `.env` в корне проекта на основе `.env.example` и заполните нужные переменные (секретный ключ Django, параметры PostgreSQL, токен Telegram-бота и т. д.).

### 3. Сборка и запуск контейнеров

```bash
docker compose up --build
```

### 4. Миграции

```bash
docker compose exec backend python manage.py migrate
```

### 5. Создание суперпользователя

```bash
docker compose exec backend python manage.py createsuperuser
```

## Проверка сервисов

Проверить статус контейнеров:

```bash
docker compose ps
```

Посмотреть логи отдельных сервисов:

```bash
docker compose logs backend
docker compose logs db
docker compose logs redis
docker compose logs celery
docker compose logs celery-beat
```

После запуска:

- Backend: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Telegram-интеграция

1. Создайте бота через `@BotFather` и получите токен.
2. Укажите токен в `.env` в переменной `TELEGRAM_BOT_TOKEN`.
3. Откройте чат с ботом в Telegram и отправьте `/start`.
4. Получите `chat_id` через `https://api.telegram.org/bot<ТОКЕН>/getUpdates`.
5. Создайте `TelegramProfile` для пользователя (через админку или Django shell), указав `chat_id`.
6. Создайте привычку с подходящими параметрами (`periodicity`, `time` и т. д.).
7. Периодическая задача Celery будет отправлять напоминания в указанный чат.

## Тесты

Запуск тестов с покрытием:

```bash
pytest --cov=. --cov-report=term-missing
```

## Стиль кода

Проверка стиля:

```bash
flake8 .
```

## Автор

VeNDeTeT