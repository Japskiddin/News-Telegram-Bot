import os

from dotenv import load_dotenv

load_dotenv()


def get_telegram_token():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise ValueError(
            "Токен бота не найден. Убедитесь, что TELEGRAM_TOKEN указан в .env файле."
        )
    return token


def get_news_api_key():
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError(
            "Ключ API не найден. Убедитесь, что NEWS_API_KEY указан в .env файле."
        )
    return api_key
