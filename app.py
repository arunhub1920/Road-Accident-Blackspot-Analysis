import streamlit as st
import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\blackspots.csv")

df = df.rename(columns={
    "Latitude": "latitude",
    "Longitude": "longitude"
})

st.map(df[['latitude', 'longitude']])   

