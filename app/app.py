# python -m streamlit run app.py

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    if not movie_id:
        return "https://via.placeholder.com/500x750?text=No+Image"  # Placeholder for missing ID

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    try:
        response = requests.get(url, timeout=10)  # Set timeout to 10s
        response.raise_for_status()  # Raises HTTP error if response is not 200

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except requests.exceptions.Timeout:
        print("API request timed out. Retrying...")
        return "https://via.placeholder.com/500x750?text=API+Timeout"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].get("movie_id")
        recommended_movies.append(movies.loc[i[0]].title)

        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('D:/Python/ML/MovieRecomSystem/model/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('D:/Python/ML/MovieRecomSystem/model/similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('How would you like to be contacted?', movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])