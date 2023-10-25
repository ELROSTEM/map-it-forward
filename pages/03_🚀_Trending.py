import streamlit as st

st.set_page_config(
     page_title="Map It Forward",
     page_icon="📍",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "Show where you want community improvements!"
     }
)

st.title("Trending Projects 🚀")

with st.expander("Project 1", expanded=True):
    st.image("https://static.streamlit.io/examples/dice.jpg")

    st.write("Description of the project goes here.")

with st.expander("Project 2", expanded=True):
    st.image("https://static.streamlit.io/examples/dice.jpg")

    st.write("Description of the project goes here.")

with st.expander("Project 3", expanded=True):
    st.image("https://static.streamlit.io/examples/dice.jpg")

    st.write("Description of the project goes here.")