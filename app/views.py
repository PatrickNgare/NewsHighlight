from flask import render_template
from app import app
from .request import get_sources, get_articles



@app.route('/')
def index():
    

    spo = get_sources('us', 'sports')
    biz = get_sources('us', 'business')
    heal = get_sources('us', 'health')
    sci = get_sources('us', 'science')
    ent = get_sources('us', 'entertainment')
    gen = get_sources('us', 'general')
    biz = get_sources('us', 'business')
    tech = get_sources('us', 'technology')
   
  
    return render_template('index.html', general=gen,business=biz,technology=tech,sports=spo,health=heal,science=sci,
            entertainment=ent)


@app.route('/news/<id>')
def news(id):
    
    news_args = get_articles(id)

    return render_template('new.html',news=news_args)