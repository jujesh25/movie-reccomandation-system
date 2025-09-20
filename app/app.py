import streamlit as st
from recommender import Recommender

st.title("🎬 Netflix Recommendation Clone")

try:
    rec = Recommender("data/movies.csv")
except Exception as e:
    st.error(f"Error loading dataset: {e}")

movie_name = st.text_input("Enter a movie title:")

if movie_name:
    try:
        recommendations = rec.recommend(movie_name)
        if "Movie not found in database!" in recommendations:
            st.error("❌ Movie not found in database. Try another title.")
        else:
            st.success("✅ Here are some recommendations:")
            for r in recommendations:
                st.write(f"- {r}")
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
