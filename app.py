from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
#creates route function and renders html template here
@app.route('/')
def home():
    #client id and api_key
    newsapi = NewsApiClient(api_key="c912ed1962e542bb8529a76ce984add9")

    