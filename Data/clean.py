import pandas as pd

df = pd.read_csv("tmdb_movies_5000.csv")

df.dropna(subset=["overview"], inplace=True)
df = df[df["overview"].str.strip() != ""]
df.drop_duplicates(subset=["title"], inplace=True)
df["genres"] = df["genres"].str.lower()
df["genres"] = df["genres"].str.replace(", ", ",", regex=False)
df["vote_average"] = df["vote_average"].fillna(0)
df.reset_index(drop=True, inplace=True)
df.to_csv("tmdb_movies_cleaned.csv", index=False)

