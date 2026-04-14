# HabitTracker API

Учебный проект на Django + DRF + Celery + Telegram для трекинга привычек и отправки напоминаний в Telegram.

## Стек

- Python 3.13
- Django 6
- Django REST Framework
- Celery 5 + Redis
- SQLite (для разработки)
- pytest, pytest-django, pytest-cov
- flake8

## Основной функционал

- Регистрация и аутентификация пользователей.
- Создание, просмотр, обновление и удаление привычек.
- Разделение привычек на полезные и приятные.
- Публичные привычки, доступные другим пользователям.
- Пагинация списка привычек.
- Интеграция с Telegram-ботом:
  - привязка Telegram-профиля (chat_id) к пользователю;
  - отправка напоминаний в личный чат с ботом.
- Отложенные задачи через Celery:
  - периодическая задача `send_habit_reminders` раз в минуту проверяет привычки
    и отправляет напоминания в Telegram.

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/USERNAME/Habittracker.git
cd Habittracker
```

(подставьте свой URL репозитория GitHub).

### 2. Виртуальное окружение и зависимости

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Переменные окружения

Создайте файл `.env` в корне проекта:

```env
SECRET_KEY=django-insecure-test-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

TELEGRAM_BOT_TOKEN=ВАШ_ТОКЕН_ОТ_BOTFATHER

CELERY_BROKER_URL=redis://localhost:6379/0
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 4. Миграции и суперпользователь

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Запуск Redis

Redis должен быть запущен локально:

```bash
redis-server
```

(для Windows можно использовать отдельный установщик или Docker).

### 6. Запуск сервисов

В разных терминалах:

```bash
python manage.py runserver
```

```bash
celery -A config worker -l info -P solo
```

```bash
celery -A config beat -l info
```

После этого API будет доступен по адресу:

- `http://127.0.0.1:8000/`
- админка: `http://127.0.0.1:8000/admin/`

## Telegram-интеграция

1. Создайте бота через `@BotFather` и получите токен.
2. Укажите токен в `.env` (`TELEGRAM_BOT_TOKEN`).
3. Откройте чат с ботом в Telegram и отправьте `/start`.
4. Узнайте свой `chat_id`:
   - запросом `https://api.telegram.org/bot<ТОКЕН>/getUpdates`;
   - из поля `"message": {"chat": {"id": ...}}`.
5. Создайте `TelegramProfile` для пользователя (через Django shell или админку),
   указав найденный `chat_id`.
6. Создайте привычку с полями:
   - `user` — ваш пользователь;
   - `is_pleasant = False`;
   - `periodicity = 1`;
   - `time` — ближайшая минута вперёд.
7. В указанную минуту Celery отправит напоминание в чат с ботом.

## Тесты

Проект покрыт тестами более чем на 80%.

Запуск тестов с покрытием:

```bash
pytest --cov=. --cov-report=term-missing
```

### Особенность для Celery в тестах

Для синхронного выполнения задач в тестах используется переменная окружения:

```bash
set PYTEST_RUNNING=1  # Windows
# export PYTEST_RUNNING=1  # Linux/macOS
pytest
```

## Стиль кода

Для проверки стиля используется `flake8`.

Конфигурация (`.flake8`):

```ini
[flake8]
exclude = .venv,venv,migrations,env,__pycache__,.git
max-line-length = 88
```

Запуск проверки:

```bash
flake8 .
```

## Пример основных эндпоинтов

Точные URL зависят от `habits/urls.py` и `users/urls.py`, но типично:

- `POST /api/users/` – регистрация пользователя.
- `POST /api/token/` – получение токена аутентификации.
- `GET /api/habits/` – список привычек (с пагинацией).
- `POST /api/habits/` – создание привычки.
- `GET /api/habits/{id}/` – детальный просмотр привычки.
- `PUT/PATCH /api/habits/{id}/` – обновление привычки.
- `DELETE /api/habits/{id}/` – удаление привычки.

(При необходимости подкорректируйте пути под ваш `urls.py`.)

## Автор

- ФИО студента  
- Группа / курс  
- Контакты (по желанию)