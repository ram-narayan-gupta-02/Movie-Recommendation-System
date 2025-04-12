# 🎥 Movie Recommendation System (Content-Based)

This is a **Movie Recommendation System** project inspired by [CodeBasics' YouTube tutorial](https://youtu.be/1xtrIEwY_zY?feature=shared). It uses **content-based filtering** to suggest similar movies based on their genres, keywords, cast, crew, and overview using the IMDb movie dataset.

---

## 📌 Features

- ✅ Recommends movies similar to the input movie
- ✅ Uses movie metadata: genres, keywords, cast, crew, overview
- ✅ Applies **TF-IDF** and **cosine similarity** for content similarity
- ✅ Lightweight and beginner-friendly implementation in Python
- ✅ No user-rating data required

---

## 📁 Dataset

The dataset used includes two CSV files from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata):

- `movies.csv` – Basic movie info
- `credits.csv` – Cast and crew details

---

## 🧠 How It Works

1. **Preprocessing**
   - Merge `movies.csv` and `credits.csv`
   - Clean and combine relevant features: title, genres, overview, keywords, cast, crew
   - Convert text data into lowercase and remove spaces/special characters

2. **Feature Engineering**
   - Create a new feature called `tags` which combines:
     - Overview
     - Genres
     - Keywords
     - Cast (top 3)
     - Director (only one)

3. **Vectorization**
   - Use `CountVectorizer` from scikit-learn to convert tags into numeric vectors

4. **Similarity Calculation**
   - Compute similarity using **cosine similarity**
   - Recommend top N movies with the highest similarity score

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-content-based.git
cd movie-recommendation-content-based
