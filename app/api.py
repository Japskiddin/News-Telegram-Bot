from http import HTTPStatus

import requests

from config import get_news_api_key

API_KEY = get_news_api_key()

BASE_URL = "https://newsapi.org/v2"
URL_TOP_HEADLINES = "/top-headlines"


def get_top_headlines():
    url = f"{BASE_URL}{URL_TOP_HEADLINES}?country=us&category=science&apiKey={API_KEY}"

    response = requests.get(url)

    code = response.status_code

    if code == HTTPStatus.OK:
        data = response.json()
        return get_data_from_response(data)
    else:
        return None


def get_data_from_response(data):
    status = data["status"]

    if status == "ok":
        articles = data["articles"][:5]
        result = []
        for article in articles:
            news = {
                "author": article["author"],
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
            }
            result.append(news)
        return result
    else:
        return None
