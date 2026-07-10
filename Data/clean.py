import pandas as pd

df = pd.read_csv("tmdb_movies_5000.csv")
# dropping rows with empty values
df.dropna(subset=["overview"], inplace=True)
# removing extra spaces 
df = df[df["overview"].str.strip() != ""]
#Deduplication
df.drop_duplicates(subset=["title"], inplace=True)
# String fromatting
df["genres"] = df["genres"].str.lower()
df["genres"] = df["genres"].str.replace(", ", ",", regex=False)
# Filling the missing values
df["vote_average"] = df["vote_average"].fillna(0)
# Resetting index to make the data uniform 
df.reset_index(drop=True, inplace=True)
#saving back the refined dataset to a new csv file
df.to_csv("tmdb_movies_cleaned.csv", index=False)