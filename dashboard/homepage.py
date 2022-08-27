import streamlit as st
import streamlit.components.v1 as comp
from PIL import Image
import user_overview_page
import modelpredict

st.title("Telecommunication Data Analysis")
pages = {
    "User Overview Analysis": user_overview_page.overview_app,
    "Model Prediction" : modelpredict.prdict_app
}

image = Image.open('../images/telecom.jpg')
st.image(image, caption="Telecom Data Analysis", use_column_width=True)
selection = st.sidebar.selectbox("Go to page ", list(pages.keys()))
if selection=="User Overview Analysis":
    user_overview_page.overview_app()
else:
    modelpredict.prdict_app()