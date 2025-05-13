import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st
import plotly.graph_objects as go

df = pd.read_csv("reliance_data_2018_2023.csv")

def renderTabGraphs():
    st.text("Close vs Time ")
    st.line_chart(df["close"])
    st.text("If an investment had been made in 2018, it would have yielded a 140% return by 2023, as illustrated in the plot.")
    st.text("")
    st.text("CandleStick")
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['OPEN'], high=df['HIGH'], low=df['LOW'], close=df['close'])])
    st.plotly_chart(fig)
    st.text("Trading Volume")
    st.line_chart(df["VOLUME"])
    
