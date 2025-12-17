import streamlit as st
import pandas as pd

# Load dataset (replace with actual dataset)
df1 = pd.read_csv('input.csv')


# Streamlit UI
st.title("Movie/TV Show Recommendation System")

# User Inputs
type_input = st.selectbox("Select Type:", df1['Type'].unique())
genre_input = st.selectbox("Select Genre:", df1['Genre'].unique())
year_range = st.slider("Select Premiere Year Range:", int(df1['Premiere'].min()), int(df1['Premiere'].max()), (2010, 2020))
min_views = st.number_input("Enter Minimum Watchtime in :", min_value=0, value=50)

# Filter Data
filtered_df = df1[(df1['Type'] == type_input) &
                   (df1['Genre'] == genre_input) &
                   (df1['Premiere'].between(year_range[0], year_range[1])) &
                   (df1['WM']>= min_views)]

# Display Recommendation
if not filtered_df.empty:
    suggestion = filtered_df.sort_values(by='WM', ascending=False).iloc[0]
    st.success(f"Recommended {suggestion['Type']}: {suggestion['Title']} ({suggestion['Premiere']})")
else:
    st.warning("No matching recommendations found!")