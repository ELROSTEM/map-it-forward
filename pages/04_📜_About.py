import streamlit as st

st.set_page_config(
     page_title="Map It Forward",
     page_icon="📍",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "Show where you want community improvements!"
     }
)

with open('./database/about.txt', 'r') as f:
    about = f.read()
    st.markdown(about)