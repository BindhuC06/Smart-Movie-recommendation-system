# Smart Movie Recommendation System

## Project Overview

The **Smart Movie Recommendation System** is a content-based movie recommendation project that recommends movies based on their **title, genres, and movie overview** using Natural Language Processing (NLP).

The project collects movie information from **The Movie Database (TMDB)** API, cleans the dataset, performs Exploratory Data Analysis (EDA), generates semantic embeddings using **Sentence Transformers**, indexes the embeddings using **FAISS**, and provides a **Streamlit web interface** for users to search and receive similar movie recommendations.

---

# Objectives

The primary objectives of this project are:

- Collect movie data from TMDB API.
- Clean and preprocess the collected dataset.
- Perform Exploratory Data Analysis (EDA).
- Generate semantic embeddings using Sentence Transformers.
- Build a FAISS similarity search index.
- Recommend similar movies based on user queries.
- Develop an interactive Streamlit web application.

---

# Project Structure

```
Smart Recommendation Movie System
│
├── Data
│   ├── fetch_tmdb.py
│   ├── clean.py
│   └── eda.py
│
├── embedding
│   ├── embed.py
│   ├── search_interface.py
│   ├── movie_embeddings.npy
│   └── movies_faiss_flat.index
│
├── results
│   ├── eda1.png
│   ├── eda2.png
│   └── top_genre.png
│
├── app.py
├── main.py
├── README.md
├── requirements.txt
├── tmdb_movies_5000.csv
└── tmdb_movies_cleaned.csv
```

---

# Data Collection

The dataset was collected from **The Movie Database (TMDB)** using its official API.

The following information was collected for every movie:

- Movie Title
- Movie Overview
- Genres
- Poster Path
- Average Rating
- Release Information

The collected data was stored as:

```
tmdb_movies_5000.csv
```

---

# Data Cleaning

The raw dataset contained missing values, duplicate entries, and inconsistent formatting.

The following preprocessing steps were performed:

1. Removed duplicate movie entries.
2. Removed rows with missing overview values.
3. Filled missing numerical values using column averages.
4. Trimmed unnecessary white spaces.
5. Standardized text formatting.
6. Reset dataframe index.
7. Saved the cleaned dataset.

Output:

```
tmdb_movies_cleaned.csv
```

---

# Exploratory Data Analysis (EDA)

EDA was performed to understand the dataset before building the recommendation engine.

## 1. Dataset Information

The structure, datatype, and missing values of the dataset were analyzed.

![Dataset Information](results/eda1.png)

---

## 2. Most Popular Genres

The frequency of each genre was calculated.

This helped identify which movie genres dominate the dataset.

![Top Genres](results/top_genre.png)

### Observation

- Drama is the most common genre.
- Comedy is the second most frequent genre.
- Action ranks among the top genres.

---

## 3. Highest and Lowest Rated Movies

Movies were analyzed based on their average ratings.

This helped identify the highest-rated and lowest-rated movies in the dataset.

![Ratings Analysis](results/eda2.png)

---

# Sentence Embedding Generation

To understand movie meanings rather than simple keyword matching, semantic embeddings were generated.

### Model Used

```
all-MiniLM-L6-v2
```

using the **Sentence Transformers** library.

Each movie was converted into a 384-dimensional dense vector.

The text embedded for every movie was created by combining:

- Movie Title
- Genres
- Movie Overview

The generated embeddings were stored as:

```
embedding/movie_embeddings.npy
```

---

# FAISS Index Creation

To perform fast similarity search on thousands of movie vectors, a **FAISS Flat Index** was built.

Benefits:

- Fast nearest-neighbor search
- Efficient semantic similarity matching
- Scalable recommendation system

The generated index was stored as:

```
embedding/movies_faiss_flat.index
```

---

# Recommendation Engine

The recommendation engine performs the following steps:

1. Accepts a user query.
2. Converts the query into a sentence embedding.
3. Searches the FAISS index.
4. Retrieves the Top-K most similar movies.
5. Displays movie titles with similarity rankings.

The recommendation logic is implemented in:

```
embedding/search_interface.py
```

---

# Streamlit Web Application

A simple interactive web application has been developed using **Streamlit**.

Features include:

- User-friendly interface
- Movie search box
- Semantic movie recommendations
- Fast response using FAISS

Main application:

```
app.py
```

---

# Installation

Clone this repository

```bash
git clone https://github.com/BindhuC06/Smart-Movie-recommendation-system.git
```

Move into the project folder

```bash
cd Smart-Movie-recommendation-system
```

Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

# Execution

## 1. Fetch Dataset

```bash
python3 Data/fetch_tmdb.py
```

---

## 2. Clean Dataset

```bash
python3 Data/clean.py
```

---

## 3. Perform EDA

```bash
python3 Data/eda.py
```

---

## 4. Generate Sentence Embeddings

```bash
python3 embedding/embed.py
```

---

## 5. Run Recommendation Search

```bash
python3 embedding/search_interface.py
```

---

## 6. Launch Streamlit Application

```bash
python3 -m streamlit run app.py
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Sentence Transformers
- FAISS
- Streamlit
- TMDB API

---

# Future Improvements

The future scope of this project includes:

- Personalized recommendations based on user history.
- Hybrid recommendation system combining content-based and collaborative filtering.
- Genre-based filtering.
- Movie poster display using TMDB images.
- IMDb rating integration.
- User authentication.
- Cloud deployment using Streamlit Community Cloud or Render.
- Recommendation explanation (Why this movie was recommended).

---
