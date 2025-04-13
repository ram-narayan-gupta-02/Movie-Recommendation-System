# 🎥 Movie Recommendation System (Content-Based)

## 📌 Project Overview
**Movie Recommendation System** This project is a **content-based movie recommendation system** that suggests movies similar to a given movie. It leverages movie metadata (such as genres, keywords, cast, crew, and overview) to make accurate recommendations. The system is built using Python, Pandas, Scikit-learn, and Streamlit for deployment, providing an interactive web interface for easy usage.

---

## 📌 Features

- ✅ **Data Preprocessing**: Handles missing values and extracts relevant features like genres, keywords, and cast.
- ✅ **Exploratory Data Analysis (EDA)**: Visualizes key patterns and insights in the movie dataset.
- ✅ **Feature Engineering**: Transforms data into suitable formats for machine learning.
- ✅ **Machine Learning Model**: Implements cosine similarity between TF-IDF vectors for movie recommendations.
- ✅ **Web App with Streamlit**: Allows users to input a movie title and get recommendations based on similarity.

---

## 📂 Project Structure
```
MovieRecommendationSystem/
│── dataset/
│   ├── tmdb_5000_movies.csv          # Movie metadata
│   ├── tmdb_5000_credits.csv         # Cast and crew data
│── app.py                            # Streamlit app for prediction
│── movie_recommendation.py           # Logic for movie recommendation
│── movies.pkl                        # Serialized movie data (used for prediction)
│── movies_dict.pkl                   # Serialized movie metadata dictionary
│── requirements.txt                  # Required Python libraries
│── README.md                         # Project documentation

```
- ✅ **dataset/**: Contains movie metadata and cast information.
- ✅ **app.py**: Streamlit app for generating movie recommendations.
- ✅ **movie_recommendation.py**: Core recommendation logic.
- ✅ **movies.pkl**: Serialized movie data for quick access.
- ✅ **movies_dict.pkl**: Serialized movie metadata.
- ✅ **requirements.txt**: List of dependencies for the project.
- ✅ **README.md**: Project documentation.

---

## 📁 Dataset

The dataset used includes two CSV files from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata):

- `movies.csv` – Basic movie info
- `credits.csv` – Cast and crew details

---

## 📊 Data Preprocessing & EDA

The dataset contains:

- **movieId** (Unique ID)
- **title** (Movie title)
- **genres** (Movie genres)
- **keywords** (Related keywords)
- **cast** (Movie cast)
- **crew** (Director, producers, etc.)
- **overview** (Movie description)

###🔹 Handling Missing Data

**Keywords**: Filled with empty strings where missing.
**Overview**: Left untouched, as missing values indicate that no description is available.

###🔹 Encoding Categorical Variables

**Genres**: One-hot encoding for different genres.
**Keywords**: Vectorized using TF-IDF for textual information.
**Cast and Crew**: Extracted and cleaned for use in the recommendation model.

---

## 🔍 Model Training

**Algorithm Used**: Cosine Similarity with TF-IDF Vectorization
```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
```
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

## Model Performance

- The model provides accurate movie recommendations based on content similarity.
- Cosine similarity calculates similarity between movies, considering their metadata (genres, keywords, etc.).

---

## 🖥️ Running the Web App

**Run Streamlit App**
```
streamlit run app.py
```
**Alternative**: Run via Python Script
```
python -m streamlit run app.py
```
**Access in Browser**
Once running, open in your browser.

---

## 🛠️ Future Improvements

- ✅ Implement collaborative filtering to enhance recommendations with user ratings.
- ✅ Add more machine learning models like Random Forest or SVM for better predictions.
- ✅ Deploy the app using Heroku or AWS for public access.

---

## 🤝 Contributing

Feel free to contribute by submitting a pull request or reporting issues!

---
## 📩 Contact

📧 **Email**: ramnrngupta@gmail.com
📌 **GitHub**: ram-narayan-gupta-02
