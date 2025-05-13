

import requests
from config import settings


# Тест 0 — доступность API
def test_api_status():
    response = requests.get(f"{settings.BASE_URL_API}/movie",
                            headers=settings.HEADERS_API)
    assert response.status_code in [200, 403]


# Тест 1 — получение фильма по ID
def test_get_film_by_id():
    film_id = "301"
    url = f"{settings.BASE_URL_API}/movie/{film_id}"

    response = requests.get(url, headers=settings.HEADERS_API)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == int(film_id)

    assert "name" in data
    assert data["name"] == "Матрица"


# Тест 2 — поиск фильма по названию
def test_search_movie_by_title():
    query = "Побег из Шоушенка"
    url = f"{settings.BASE_URL_API}/movie/search?query={query}"

    response = requests.get(url, headers=settings.HEADERS_API)
    assert response.status_code == 200

    data = response.json()

    assert "docs" in data
    assert len(data["docs"]) > 0

    titles = [film.get("name") for film in data["docs"] if film.get("name")]
    assert any(query.lower() in title.lower() for title in titles)


# Тест 3 — поиск фильмов по жанру
def test_search_movies_by_genre():
    genre = "драма"
    url = f"{settings.BASE_URL_API}/movie?genres.name={genre}&limit=10"

    response = requests.get(url, headers=settings.HEADERS_API)
    assert response.status_code == 200

    data = response.json()

    assert "docs" in data
    assert len(data["docs"]) > 0

    for film in data["docs"]:
        genres = [g["name"] for g in film.get("genres", [])]
        assert genre in genres


# Тест 4 — поиск фильмов с рейтингом от 8.2 до 9.8
def test_search_movies_by_rating():
    url = f"{settings.BASE_URL_API}/movie?rating.kp=8.2-9.8&limit=10"

    response = requests.get(url, headers=settings.HEADERS_API)
    assert response.status_code == 200

    data = response.json()
    assert "docs" in data
    assert len(data["docs"]) > 0

    for film in data["docs"]:
        rating = film.get("rating", {}).get("kp")
        assert rating is not None
        assert 8.2 <= rating <= 9.8


# Тест 5 — негативный: запрос фильма с несуществующим ID
def test_get_film_invalid_id():
    invalid_id = "999999999"
    url = f"{settings.BASE_URL_API}/movie/{invalid_id}"

    response = requests.get(url, headers=settings.HEADERS_API)

    assert response.status_code == 400
