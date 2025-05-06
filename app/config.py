import os

from dotenv import load_dotenv


def get_telegram_token():
    load_dotenv()

    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise ValueError(
            "Токен бота не найден. Убедитесь, что TELEGRAM_TOKEN указан в .env файле."
        )
    return token
