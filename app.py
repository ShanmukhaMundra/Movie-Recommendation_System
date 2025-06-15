import pickle as pkl
import streamlit as st
import requests

def poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=cc8a568348d9a63eeb7b6645d60373b0&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters

st.header('🎬🍿 Movie Recommender System')

with open('binary/movie_list.pkl', 'rb') as f:
    movies = pkl.load(f)

with open('binary/similarity1.pkl', 'rb') as f:
    similarity = pkl.load(f)

movie_list = movies['title'].values

selected_movie = st.selectbox(
    'Pick a movie title from below or enter a movie title to get recommendations:',
    movie_list
)

if st.button('Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    col4, col5, col6 = st.columns([1, 1, 1])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

