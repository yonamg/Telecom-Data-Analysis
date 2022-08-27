import streamlit as st
import streamlit.components.v1 as comp
from PIL import Image
@st.cache
def homepage_app():
    st.title("Home Page")
    image = Image.open('../images/telecom.jpg')
    st.image(image, caption="Telecom Data Analysis", use_column_width=True)
    app_link = st.sidebar.selectbox('Select Page', ['User Overview Analysis', 'Model Prediction'])

homepage_app()