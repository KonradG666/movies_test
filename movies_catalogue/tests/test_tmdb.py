import tmdb_client
from unittest.mock import Mock

def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']
    request_mock = Mock()
    response =  request_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list  == mock_movies_list

def test_get_single_movie(monkeypatch):
    mock_single_movie = "movie1"
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)
    single_movie = tmdb_client.get_single_movie(419704)
    assert single_movie == mock_single_movie

def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = 'actor name'
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_single_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", request_mock)
    single_movie_cast = tmdb_client.get_single_movie_cast(419704)
    assert single_movie_cast == mock_single_movie_cast

def test_get_movie_images(monkeypatch):
    mock_movie_images = 'image'
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie_images
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie_images = tmdb_client.get_movie_images(419704)
    assert movie_images == mock_movie_images

