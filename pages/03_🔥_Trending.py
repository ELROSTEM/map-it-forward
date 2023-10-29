import streamlit as st
from PIL import Image
import os
import pandas as pd

st.set_page_config(
     page_title="Map It Forward",
     page_icon="📍",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "Show where you want community improvements!"
     }
)

st.title("🔥 Trending")

# Read submissions
df = pd.read_csv("database/submissions.csv")

# Find images path
path = r"./database/images/"
files = os.listdir(path)

for file in files:
    # make sure file is an image
    if file.endswith(('.jpg', 'jpeg')):
        img_path = path + file
        img = Image.open(img_path)
        
        with st.expander(f"Submission {file[:-4]}", expanded=True):
            st.image(img)
            st.caption(df.iloc[int(file[:-4])]['address'])
            st.subheader("Category")
            st.write(df.iloc[int(file[:-4])]['category'])
            st.subheader("Description")
            st.write(df.iloc[int(file[:-4])]['description'])
            st.subheader("Recommendation")
            st.write(df.iloc[int(file[:-4])]['recommendation'])