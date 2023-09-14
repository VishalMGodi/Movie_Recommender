import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

new_mov=pd.read_csv(r"cleaned_movies.csv")
x=pd.read_csv(r"dirty_movies.csv")
z=pd.read_csv(r"movies.csv")

temp=TfidfVectorizer(max_features=5000,stop_words="english")
temp=temp.fit_transform(new_mov["tags"]).toarray()
sim=cosine_similarity(temp)

st.set_page_config(layout="wide")
st.title('Movie Recommendation')
with st.container():
    st.write("-"*150)
    left_col,right_col=st.columns((2,1))
    with left_col:
        global selected_movie
        selected_movie = st.selectbox('Select a movie', new_mov['title'].values)

    with right_col:
        global nums
        nums = st.selectbox('How many recommendations?', [x for x in range(1,11)])

if st.button('Get Similar Movie Recommendations'):
    movie_id=new_mov[new_mov["title"]==selected_movie].index[0]
    scores = list(enumerate(sim[movie_id]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:nums+1]
    movies = [new_mov.iloc[score[0]]['title'] for score in scores]
    
    test=st.tabs(movies)
    for i in range(len(test)):
        with test[i]:
            st.subheader("GENRES:")
            genres=x[x['title']==movies[i]]['genres'].values[0][1:-1].split(",")
            for k in range(len(genres)):
                if k==0:
                    genres[0]=genres[0][1:-1]
                else:
                    genres[k]=genres[k][2:-1]
            st.markdown(", ".join(genres[0:len(genres)]))

            st.subheader("PLOT:")
            st.markdown(x[x['title']==movies[i]]['overview'].values[0])

            st.subheader("STAR CAST:")
            cast=x[x['title']==movies[i]]['cast'].values[0][1:-1].split(",")
            for k in range(3):
                if k==0:
                    cast[0]=cast[0][1:-1]
                else:
                    cast[k]=cast[k][2:-1]
            st.markdown(", ".join(cast[0:3]))
            
            st.subheader("CHECK ON WEBSITE:")
            st.markdown(z[z['title']==movies[i]]['homepage'].values[0])