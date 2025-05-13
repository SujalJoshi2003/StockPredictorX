from GoogleNews import GoogleNews
import pytz
import datetime as dt 
import time
import streamlit as st

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

tokenizer = AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")



def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True,max_length=512)
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=1)
    sentiment = torch.argmax(probs).item()

    labels = ["negative", "neutral", "positive"]
    return {
        "label": labels[sentiment],
        "confidence": probs[0][sentiment].item()
    }

def renderTabSuggestions():
    avgScore = 0
    scoreSentiments = 0
    india_timezone = pytz.timezone('Asia/Kolkata')
    startDate = dt.datetime.now(india_timezone)
    googlenews = GoogleNews(
              start=startDate.strftime('%m/%d/%Y'),
              end=startDate.strftime('%m/%d/%Y'),
              lang='en',
              region='IN'
              )
    googlenews.search("Reliance Industries Limited ")
    results = googlenews.results()
    googlenews.clear()
    resultsText = [result['title'] for result in results]
    for result in resultsText:
        result = analyze_sentiment(result)
        if result['label'] == 'positive':
            scoreSentiments +=1
        elif result['label'] == 'negative':
            scoreSentiments -=1
        else :
            scoreSentiments +=0
    if(len(resultsText) > 0):
        avgScore = scoreSentiments/len(resultsText)
    if(len(resultsText)==0):
        st.write("Sorry,we couldn't fetch any news for sentiment evaluation ")
    if ( avgScore > 0.5 ):
        st.write("Great news! The overall sentiment is positive according to the recent news. Based on this, we recommend proceeding with your investment or decision")
    elif ( avgScore< -0.5):
        st.write("It seems the sentiment is negative accoring to the recent news. Based on this, we suggest you reconsider your decision or look for other options to meet your needs")
    elif (-0.5< avgScore < 0.5):
        st.write("The sentiment is neutral according to the recent news, meaning the feedback is mixed. It might be a good idea to gather more insights before making a final decision.")
