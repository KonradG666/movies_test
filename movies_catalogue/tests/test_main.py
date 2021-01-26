from unittest.mock import Mock
import pytest
from main import app

@pytest.mark.parametrize("list_type, movie",
                       [ ("/" ,"movie/popular"),
                        ("/?list_type=popular", "movie/popular"),
                        ("/?list_type=top_rated","movie/top_rated"),
                        ("/?list_type=upcoming","movie/upcoming"),
                        ("/?list_type=now_playing","movie/now_playing"),
                        ("/?list_type=nowa", "movie/popular")])

def test_movie_list(monkeypatch, list_type, movie):
    print(list_type)
    print(movie)
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb", api_mock)

    with app.test_client() as client:
       response = client.get(list_type)
       assert response.status_code == 200
       api_mock.assert_called_once_with(movie)



