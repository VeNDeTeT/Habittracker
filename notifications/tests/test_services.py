import pytest
from django.conf import settings


@pytest.mark.django_db
def test_send_telegram_message_calls_requests_post(mocker):
    from notifications.services import send_telegram_message

    mock_post = mocker.patch("notifications.services.requests.post")

    chat_id = "580684609"
    text = "Привет из теста"

    send_telegram_message(chat_id, text)

    if settings.TELEGRAM_BOT_TOKEN:
        mock_post.assert_called_once()
        url = mock_post.call_args[0][0]
        assert "sendMessage" in url
    else:
        mock_post.assert_not_called()
