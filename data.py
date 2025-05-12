import pandas as pd 
import streamlit as st

df = pd.read_csv("/workspaces/codespaces-blank/reliance_data_2018_2023.csv")

def renderTabGlimpse():
    st.text("")
    st.text("Here is a preview of the data used to train the model.")
    st.write(df.head())
    st.text("")
    st.text("Here are the final data values that were used in the model's training.")
    st.write(df.tail())
    st.text("")
    st.text("The changes in stock features over time are clearly noticeable.")
    st.text("Note: The data covers the period from 2018 to 2023.")