import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
df = pd.read_csv("tmdb_movies_cleaned.csv")
# Shape of the data

# print("Shape of dataset:", df.shape)
# print("\nColumns:")
# print(df.columns)

# print("\nData Types:")
# print(df.dtypes)

# Analysing the most popular genre
# genre_counter = Counter()

# for genre_list in df["genres"]:
#     genres = genre_list.split(",")
#     genre_counter.update(genres)

# genre_df = pd.DataFrame(
#     genre_counter.items(),
#     columns=["Genre", "Count"]
# )

# genre_df = genre_df.sort_values(
#     by="Count",
#     ascending=False
# )
# plt.figure(figsize=(10,6))

# plt.bar(
#     genre_df["Genre"][:10],
#     genre_df["Count"][:10]
# )

# plt.xticks(rotation=45)
# plt.title("Top 10 Genres")
# plt.ylabel("Number of Movies")
# plt.savefig('./results/top_genre.png')
# plt.show()

# Finding the most rated movies
# print(
#     df.sort_values(
#         by="vote_average",
#         ascending=False
#     )[["title","vote_average"]].head(10)
#)

# Finding the number of genres

all_genres = set()

for genres in df["genres"]:
    all_genres.update(genres.split(","))

print("Unique genres:", len(all_genres))
print(sorted(all_genres))