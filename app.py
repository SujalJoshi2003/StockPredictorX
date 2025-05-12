import streamlit as st 
from data import renderTabGlimpse
from graphs import renderTabGraphs
from prediction import renderTabPredictor
from suggestions import renderTabSuggestions

st.title("ReliancePredX")
st.text("")
st.subheader("ReliancePredX is a predictive model that estimates Reliance stock prices based on user inputs and historical data.")
st.text("")
st.text("")
st.text("Here are the main features you can explore!")

tab1 , tab2 , tab3 , tab4= st.tabs(['Prediction','Insights','Glimpse','Suggestions'])

with tab1:
    renderTabPredictor()
with tab2:
    renderTabGraphs()
with tab3:
    renderTabGlimpse()
with tab4:
    renderTabSuggestions()

st.text("")
st.text("This is an experimental project; please invest carefully according to your own strategy.")
st.text("Made by SujalJoshi2003 on github")