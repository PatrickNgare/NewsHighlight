from app import app
import urllib.request,json
from .models import articles
from .models import source
Articles=articles.Articles
Source=source.Source

base_url = app.config['BASE_NEWS_API_URL']
source_url = app.config['SOURCE_NEWS_URL']
api_key=app.config['NEWS_API_KEY']



def get_sources(coutry, category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(coutry, category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        source_results = None

        if get_news_response['sources']:
            source_results_list = get_news_response['sources']
            source_results = process_sources(source_results_list)

    return source_results


def process_sources(source_list):

    news_results = []
    for source in source_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')
        if url:
            source_object = Source(id, name,description,url,category,country)
            news_results.append(source_object)

    return news_results


def get_articles(id):
    """
    Function that gets the json response to our url request
    """
    get_source_news_url = source_url.format( id, api_key)
    with urllib.request.urlopen(get_source_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_articles(news_results_list)

    return news_results


def process_articles(articles_list):
    news_results = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            
            source_object = Articles(id,name,author,title,description,url,urlToImage, publishedAt)
            news_results.append(source_object)

    return news_results