import streamlit as st
import pandas as pd

# Load dataset (replace with actual dataset)
df1 = pd.read_csv('input2.csv')
# Streamlit UI
st.title("Movie/TV Show Recommendation System")

# User Inputs
country_input = st.selectbox("Select Country:", df1['ori_country'].unique())
genre_input = st.selectbox("Select Genre:", df1['genre'].unique())
show_type_input = st.selectbox("Select Show Type:", df1['show_type'].unique())
release_month = st.slider("Select Release Month:", 1, 12, (1, 12))
imdb_rating = st.number_input("Enter Minimum IMDB Rating:", min_value=0.0, max_value=10.0, value=7.0, step=0.1)

# Filter Data
filtered_df = df1[(df1['ori_country'] == country_input) &
                   (df1['genre'] == genre_input) &
                   (df1['show_type'] == show_type_input) &
                   (df1['Month'].between(release_month[0], release_month[1])) &
                   (df1['imdb_rating'] >= imdb_rating)]

# Display Recommendation
if not filtered_df.empty:
    suggestion = filtered_df.sort_values(by='imdb_rating', ascending=False).iloc[0]
    st.success(f"Recommended {suggestion['show_type']}: {suggestion['title']} (IMDB: {suggestion['imdb_rating']})")
else:
    st.warning("No matching recommendations found!")
