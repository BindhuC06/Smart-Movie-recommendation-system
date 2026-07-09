import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

url = "https://api.themoviedb.org/3/discover/movie"
movies = []

# Genre Mapping
genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}"
genre_data = requests.get(genre_url).json()

genre_map = {}

for g in genre_data["genres"]:
    genre_map[g["id"]] = g["name"]


TOTAL_PAGES = 250      # 250 pages × 20 movies ≈ 5000 movies

for page in range(1, TOTAL_PAGES + 1):

    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "include_adult": False,
        "include_video": False,
        "page": page
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed on page {page}")
        continue

    data = response.json()

    for movie in data["results"]:

        genres = [
            genre_map[g]
            for g in movie.get("genre_ids", [])
            if g in genre_map
        ]

        movies.append({
            "title": movie.get("title"),
            "overview": movie.get("overview"),
            "genres": ", ".join(genres),
            "poster_path": movie.get("poster_path"),
            "vote_average": movie.get("vote_average")
        })

    print(f"Fetched page {page}")

    # avoid rate limiting
    time.sleep(0.2)

df = pd.DataFrame(movies)

df.to_csv("tmdb_movies_5000.csv", index=False)

print(df.head())
print(f"\nTotal movies fetched: {len(df)}")