import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    # def recommend(movies):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]

    recommend_movies = []
    for i in movies_list:
        movie_id = i[0]
        # fetch poster from API
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


# movies_dict = pickle.load(open('/home/aayu/Documents/PROJECTS/Movie-Reccomandation-System/movies_dict.pkl','rb'))
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('/home/aayu/Documents/PROJECTS/Movie-Reccomandation-System/similarity.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Choose the type of movie you want to get recommended for: ',
    movies['title'].values)

st.write('You selected:', selected_movie_name)


st.button("Reset", type="primary")
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
else:
    st.write('Goodbye')