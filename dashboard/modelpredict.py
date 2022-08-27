import pickle

import pandas as pd
import streamlit as st
from PIL import Image


def load_model():
    pickle_in = open('../models/satisfaction_model.pkl', 'rb')
    satisfaction_model = pickle.load(pickle_in)
    return satisfaction_model


def prdict_app():
    st.title("Prdict customer satisfaction")

    engage_score = st.slider("Engagement score", min_value=0.0,
                          max_value=2.0, step=0.1)
    exper_score = st.slider("Experience score", min_value=0.0,
                          max_value=2.0, step=0.1)

    if st.button("Predict"):
        model = load_model()
        result = model.predict([[engage_score, exper_score]])

        st.success(f"The customer satisfaction is {result[0][0]}")