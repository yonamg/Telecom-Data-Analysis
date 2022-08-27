import streamlit as st
import streamlit.components.v1 as comp
from PIL import Image
import user_overview_page
import modelpredict
import imagegrid

st.title("Telecommunication Data Analysis")
image = Image.open('../images/telecom.jpg')
st.image(image, caption="Telecom Data Analysis", use_column_width=True)
pages = {
    "User Overview Analysis": user_overview_page.overview_app,
    "Model Prediction" : modelpredict.prdict_app,
    "Detailed Telecom-Data-Analysis Figure": imagegrid.image_grid()
}


selection = st.sidebar.selectbox("Go to page ", list(pages.keys()))
if selection=="User Overview Analysis":
    user_overview_page.overview_app()

if selection=="Model Predictione":
    modelpredict.prdict_app()
    
if selection=="Detailed Telecom-Data-Analysis Figure":
    imagegrid.image_grid()




   