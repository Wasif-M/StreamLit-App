import streamlit as st
from st_functions import st_button, load_css
st.title("Wasif :red[Mehmood]:sunglasses:")
st.header("Data Science Intern At :red[Innomatics] Research Labs")
st.subheader(" Feb 2023")

onClick=st.button("Click Me")

if onClick==True:
    st.header("WOw :sunglasses: :red[You] :red[Clicked] :red[Me] :red[!]")
    st.balloons()
