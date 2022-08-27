import os
import sys

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

sys.path.append(os.path.abspath(os.path.join('./scripts')))


def overview_app():
    st.title("Overview")
    st.write(
        "Customer Data's Overview")
    number = st.number_input("Enter the number of rows and press enter: ", min_value=None, max_value=None, value=0,
                             step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

    df = pd.read_csv('./data/cleaned_Telecom_data.csv', nrows=number)
    st.write(df)

    st.header("Top 10 handsets used by customers")
    top_df = pd.read_csv('./data/top10handset.csv')

    fig = px.bar(top_df, x='handset_type', y='count', height=500)
    st.plotly_chart(fig)

    st.header("Top 3 handsets Manufacturers")
    top_3_df = pd.read_csv('./data/top3manufacture.csv')
    fig = px.bar(top_3_df, x='handset_manufacturer', y='count', height=500)
    st.plotly_chart(fig)

    st.header("Top 5 handsets type manufactured by Huawei")
    top_5_app = pd.read_csv('./data/top5huawei.csv')
    fig = px.bar(top_5_app, x='Handset', y='count', height=500)
    st.plotly_chart(fig)

   

    st.header("Top 3 App Used")
    image = Image.open('./images/top3appused.png')
    st.image(image, caption="Duration Distribution", use_column_width=True)

    st.header("Top 10 handset")
    image = Image.open('./images/top10.png')
    st.image(image, caption="Applications Data usage", use_column_width=True)

    st.header("Application Duration distribution using deciles")
    image = Image.open('./images/decile.png')
    st.image(image, caption="Applications Duration Distribution",
             use_column_width=True)

    st.header("Top 10 Satidfied customer")
    image = Image.open('./images/top10satisfied.png')
    st.image(image, caption="top ten satisfied customer based on usage",
             use_column_width=True)

   