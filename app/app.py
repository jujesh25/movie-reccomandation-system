import streamlit as st
from recommender import Recommender

# Title of the app
st.title("🎬 Netflix Recommendation Clone")
st.write("Type a movie name and get similar recommendations!")

# Load the recommender system
rec = Recommender("data/movies.csv")

# Input from user
movie_name = st.text_input("Enter a movie title:")

if movie_name:
    recommendations = rec.recommend(movie_name)
    if "Movie not found in database!" in recommendations:
        st.error("❌ Movie not found in database. Try another title.")
    else:
        st.success("✅ Here are some recommendations:")
        for r in recommendations:
            st.write(f"- {r}")
