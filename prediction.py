import joblib 
import streamlit as st
import pandas as pd 


model = joblib.load("/workspaces/codespaces-blank/xgboost_reliance_pred_model.pkl")

def renderTabPredictor():
    open= st.number_input("Enter Open value")
    high= st.number_input("Enter High value")
    low= st.number_input("Enter Low value")
    prevClose= st.number_input("Enter Previous Close value")
    vwap= st.number_input("Enter VWAP value")
    volume= st.number_input("Enter Volume value")

    data = {
    'OPEN': [open],
    'HIGH': [high],
    'LOW': [low],
    'PREV. CLOSE': [prevClose],
    'vwap': [vwap],
    'VOLUME': [volume]
    }

    calculationDf = pd.DataFrame(data)
    isClick = st.button("Predict Next Day Value")
    if(isClick):
        reliancePrediction = model.predict(calculationDf)
        st.write(f"Predicted value is : {reliancePrediction}")

