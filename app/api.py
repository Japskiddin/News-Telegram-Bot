from http import HTTPStatus

import requests

API_KEY = "f6f95dbec53646ea91b0fb672f7336df"

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
