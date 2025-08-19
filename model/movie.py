import pandas as pd
import numpy as np

# Load Data SEts of Movies & credits
movies = pd.read_csv(r'D:\Python\ML\MovieRecomSystem\dataset\tmdb_5000_movies.csv')
credits = pd.read_csv(r'D:\Python\ML\MovieRecomSystem\dataset\tmdb_5000_credits.csv')

# Merging of two diffrent Data Sets
movies = movies.merge(credits, on='title')

# Now fetch useful columns as like Genres, title, Keywords, Cast, Crew, Overview, Id
movies = movies[['id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)


import ast

# print(movies.iloc[0])

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def fetch_cast(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L
movies['cast'] = movies['cast'].apply(fetch_cast)

def fetch_movie_dir(obj):    
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L
movies['crew'] = movies['crew'].apply(fetch_movie_dir)

movies['overview'] = movies['overview'].apply(lambda x: x.split())

movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

movies['tag'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

nw_df = movies[['id', 'title', 'tag']]

nw_df.loc[:, 'tag'] = nw_df['tag'].apply(lambda x: " ".join(x))
nw_df.loc[:, 'tag'] = nw_df['tag'].apply(lambda x: x.lower())


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(nw_df['tag']).toarray()

import nltk 

# This library is used to the remove the Root terms
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

nw_df.loc[:, 'tag'] = nw_df['tag'].apply(stem)


from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

def recommend(movie):
    movie_indx = nw_df[nw_df['title'] == movie].index[0]
    distances = similarity[movie_indx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        print(nw_df.loc[i[0]].title)

recommend('Avatar')

import pickle

pickle.dump(nw_df.to_dict(), open('D:/Python/ML/MovieRecomSystem/movies_dict.pkl', 'wb'))

pickle.dump(similarity, open('D:/Python/ML/MovieRecomSystem/similarity.pkl', 'wb'))