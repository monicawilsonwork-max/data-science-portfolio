import streamlit as st
import pandas as pd

st.title('My Data Dashboard')
st.write('Replace with your dataset and KPIs.')
uploaded = st.file_uploader('Upload a CSV', type='csv')
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())
