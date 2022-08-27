import streamlit as st
import streamlit.components.v1 as comp
from PIL import Image
import user_overview_page
import modelpredict

st.title("Telecommunication Data Analysis")
pages = {
    "User Overview Analysis": user_overview_page,
    "Model Prediction" : modelpredict
}

image = Image.open('../images/telecom.jpg')
st.image(image, caption="Telecom Data Analysis", use_column_width=True)
selection = st.sidebar.radio("Go to page ", list(pages.keys()))
page = pages[selection]
page.app()