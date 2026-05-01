# HabitTracker API

Учебный проект на Django + DRF + Celery + Telegram для трекинга привычек и отправки напоминаний в Telegram с полной контейнеризацией и автоматическим деплоем.

## 🛠 Стек технологий

- **Backend**: Python 3.12, Django 4.2.30, Django REST Framework 3.15.2
- **База данных**: PostgreSQL 15
- **Кэш и брокер**: Redis 7
- **Асинхронные задачи**: Celery 5.5.3, Celery Beat
- **Web-сервер**: Nginx (reverse proxy)
- **Контейнеризация**: Docker, Docker Compose
- **CI/CD**: GitHub Actions
- **Тестирование**: pytest, pytest-django, pytest-cov
- **Линтинг**: flake8

## 🎯 Основной функционал

- ✅ Регистрация и аутентификация пользователей
- ✅ CRUD операции с привычками
- ✅ Разделение привычек на полезные и приятные
- ✅ Публичные привычки, доступные другим пользователям
- ✅ Пагинация списка привычек
- ✅ Интеграция с Telegram-ботом для напоминаний
- ✅ Периодическая отправка уведомлений через Celery Beat

## 🚀 Запуск проекта локально

### Требования

- Docker 20.10+
- Docker Compose 2.0+

### Инструкция по запуску

**1. Клонируйте репозиторий:**
```bash
git clone https://github.com/VeNDeTeT/Habittracker.git
cd Habittracker
```

**2. Создайте файл `.env`:**
```bash
cp .env.example .env
```

**3. Отредактируйте `.env` (укажите свои значения):**
```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
POSTGRES_DB=habittracker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-strong-password
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

**4. Запустите проект одной командой:**
```bash
docker compose up -d --build
```

**5. Примените миграции и создайте суперпользователя:**
```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py collectstatic --noinput
```

**6. Проект доступен:**
- 🌐 **Admin-панель**: http://localhost/admin/
- 🌐 **API**: http://localhost/api/
- 📖 **Swagger**: http://localhost/swagger/
- 📖 **ReDoc**: http://localhost/redoc/

## 📦 Архитектура контейнеров

Проект состоит из **6 Docker-контейнеров**:

| Контейнер | Описание | Внутренний порт |
|-----------|----------|-----------------|
| **nginx** | Reverse proxy, отдача статики и медиа | 80 → 80 |
| **backend** | Django приложение (Gunicorn WSGI) | 8000 |
| **db** | PostgreSQL база данных | 5432 |
| **redis** | Redis (кэш и брокер для Celery) | 6379 |
| **celery** | Worker для обработки асинхронных задач | - |
| **celery-beat** | Планировщик периодических задач | - |

### Схема взаимодействия:


<!-- Домашнее задание: Контейнеризация и CI/CD выполнено 01.05.2026 -->
