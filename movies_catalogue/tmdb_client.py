import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NzM4OWQwZjdlNmI5NjJkYTgyZWRhM2FkMjcwOTg4MCIsInN1YiI6IjVmZWIwYTNlZDQwZDRjMDAzZTg1MjYwZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0kD6RaCKMHdn9ydafXlSLgypfmCHiVUqKcrV85oLOcU"

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
    return call_tmdb(f"movie/{movie_id}/cast")

def get_movie_images(movie_id):
    return call_tmdb(f"movie/{movie_id}/images")

def get_lists():
    endpoint = "https://api.themoviedb.org/3/list/{list_id}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()
