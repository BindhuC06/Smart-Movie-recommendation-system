import numpy as np
import pandas as pd
import faiss
import os
from sentence_transformers import SentenceTransformer

df_cleaned=pd.read_csv("../tmdb_movies_cleaned.csv")

def create_soup(row):
    genres = row['genres']
    genres_str = " ".join(genres) if isinstance(genres, list) else str(genres)
    return f"Title: {row['title']}. Genres: {genres_str}. Overview: {row['overview']}"

df_cleaned['content_soup']=df_cleaned.apply(create_soup, axis=1)

model = SentenceTransformer('all-MiniLM-L6-v2')
sentences = df_cleaned['content_soup'].tolist()

print("\nEncoding movie text profiles into dense vector space of 384 dimentions.....")
embeddings = model.encode(sentences, show_progress_bar=True, convert_to_numpy=True)

# Save the raw mathematical matrix to disk
np.save('movie_embeddings.npy', embeddings)
print(f"Embeddings matrix saved successfully. Shape: {embeddings.shape}")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

if not embeddings.dtype == np.float32:
    embeddings = embeddings.astype('float32')

index.add(embeddings)
print(f"Total vectors indexed inside FAISS: {index.ntotal}")

# Serialize and save the index file directly to disk
faiss.write_index(index, 'movies_faiss_flat.index')
print("FAISS index successfully compiled and written to disk.")