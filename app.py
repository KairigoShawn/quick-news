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

    #gets all of the contents of the articles using for loop
    for i in range(len(t_articles)):
      main_article = t_articles[i]

      #append all the contents into the list
      news.append(main_article['title'])
      dets.append(main_article['description'])
      img.append(main_article['urlToImage'])
      p_date.append(main_article['publishedAt'])
      url.append(main_article['url'])

      contents = zip(news,dets,img,p_date,url)


    