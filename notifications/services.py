import requests
from django.conf import settings


def send_telegram_message(chat_id: str, text: str) -> None:
    token = settings.TELEGRAM_BOT_TOKEN
    if not token:
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML",
            },
            timeout=10,
        )
    except requests.RequestException:
        pass
