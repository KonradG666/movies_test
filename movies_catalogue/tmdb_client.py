import requests
import os

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZGVhMmY5YzRmZWI4NjE1Mzg1ZTc0MmNlNGM2NTczNCIsInN1YiI6IjVmZWVmNmNlMmRkYTg5MDA0MGYxZWZjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jDODTh6PlIeTYrDKXypWn4BOSW4Mj2khyuqrQzu-lgE"

def call_tmdb(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {"Authorization": f"Bearer {API_TOKEN}"}
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_popular_movies():
    return call_tmdb(f"movie/popular")

def get_movies_list(list_type):
    return call_tmdb(f"movie/{list_type}")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    return call_tmdb(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    return call_tmdb(f"movie/{movie_id}/credits")

def get_movie_images(movie_id):
    return call_tmdb(f"movie/{movie_id}/images")

def get_lists():
    return call_tmdb(f"list/{list_id}")
