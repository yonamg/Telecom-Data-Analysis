import streamlit as st
import streamlit.components.v1 as comp
from PIL import Image

def homepage_app():
    st.title("Home Page")
    image = Image.open('./images/telecom.jpg')
    st.image(image, caption="Telecom Data Analysis", use_column_width=True)
    st.write("A brief analysis of Telecom data")