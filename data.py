import streamlit as st
import pandas as pd
import numpy as np


st.title("Air pollution in Seoul Data")


@st.cache_data
def get_sales():
    data = pd.read_csv("Measurement_summary.csv")
    data[['latitude', 'longitude']] = data[['latitude', 'longitude']].replace("-", np.NaN)
    data[['latitude', 'longitude']] = data[['latitude', 'longitude']].astype('f')
    data.dropna(inplace=True)
    return data

# def page_config():
#     st.set_page_config(
#         page_title="South Korea COVID-19",
#         page_icon="🏥",
#     )

st.dataframe(get_sales())
# st.dataframe(page_config())