from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
#creates route function and renders html template here
@app.route('/')
def home():
