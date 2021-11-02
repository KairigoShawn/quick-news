from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
#creates route function and renders html template here
@app.route('/')
def home():
    #client id and api_key
    newsapi = NewsApiClient(api_key="c912ed1962e542bb8529a76ce984add9")

    #adds top headlines from news api
    top_headlines = newsapi.get_top_headlines(sources = 'cnn')

    #gets all of the main articles
    t_articles = top_headlines['articles']


    #makes a list of contents in which we will store the values
    news = []
    dets = []
    img = []
    p_date = []
    url = []

