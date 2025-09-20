import streamlit as st
import random
from recommender import Recommender

# Set page configuration
st.set_page_config(page_title="Netflix Recommender", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #F63366;'>🎬 Netflix Recommendation Clone</h1>", unsafe_allow_html=True)
st.write("Find movies with plots similar to your favorite movie!")

# Sidebar
st.sidebar.header("Options")
top_n = st.sidebar.slider("Number of Recommendations", 1, 10, 5)
show_overview = st.sidebar.checkbox("Show movie overview", True)

st.sidebar.markdown("""
---
#### About
This app recommends movies based on plot similarity using a content-based approach.
""")

# Load recommender
try:
    rec = Recommender("data/movies.csv")
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# Movie input
movie_name = st.text_input("Enter a movie title:")

# Random movie button
if st.button("🎲 Recommend from Random Movie"):
    movie_name = random.choice(rec.df['title'].tolist())
    st.info(f"Random Movie Selected: **{movie_name}**")

# Generate recommendations
if movie_name:
    try:
        recommendations = rec.recommend(movie_name, top_n=top_n)
        if "Movie not found in database!" in recommendations:
            st.error("❌ Aukaat ke bahar. Doosri dekh.")
        else:
            st.markdown(f"<h3 style='color: #0e76a8;'>✅ Top {top_n} Dekh Le:</h3>", unsafe_allow_html=True)
            for movie in recommendations:
                cols = st.columns([1, 3])
                with cols[0]:
                    # Placeholder poster image (can be replaced with real posters later)
                    st.image("https://via.placeholder.com/80x120.png?text=Poster", width=80)
                with cols[1]:
                    st.write(f"**{movie}**")
                    if show_overview:
                        overview = rec.df[rec.df['title']==movie]['overview'].values[0]
                        with st.expander("Show Overview"):
                            st.write(overview)
                st.markdown("---")
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
