from main import app
from unittest.mock import Mock
import pytest

TEST_POPULAR_MOVIES = {'page': 1, 'results': [
    {'adult': False, 'backdrop_path': '/srYya1ZlI97Au4jUYAktDe3avyA.jpg', 'genre_ids': [14, 28, 12], 'id': 464052,
     'original_language': 'en', 'original_title': 'Wonder Woman 1984',
     'overview': 'Wonder Woman comes into conflict with the Soviet Union during the Cold War in the 1980s and finds a formidable foe by the name of the Cheetah.',
     'popularity': 2510.585, 'poster_path': '/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg', 'release_date': '2020-12-16',
     'title': 'Wonder Woman 1984', 'video': False, 'vote_average': 7, 'vote_count': 3303}], 'total_pages': 1,
                       'total_results': 1}

@pytest.mark.parametrize("list_type, result", [ ("/?list_type=popular", "movie/popular"),
                                                ("/?list_type=upcoming", "movie/upcoming"),
                                                ("/?list_type=top_rated", "movie/top_rated"),
                                                ("/?list_type=now_playing", "movie/now_playing")])

def test_hompepage(monkeypatch, list_type, result):
    api_mock = Mock(return_value=TEST_POPULAR_MOVIES)
    monkeypatch.setattr("tmdb_client.call_tmdb", api_mock)

    with app.test_client() as client:
        response = client.get(list_type)
        assert response.status_code == 200
        api_mock.assert_called_once_with(result)


