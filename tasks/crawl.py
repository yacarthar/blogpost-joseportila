import os
import logging
import logging.config

import pymongo
from pymongo import InsertOne
import requests
from bs4 import BeautifulSoup, element
from celery import Celery
from celery.signals import worker_ready

from celery_config import LOGGING_CONFIG

# db
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["blog"]
Post = my_db["post"]

# app celery
app = Celery(__name__)

config_dict = {
    "development": "celery_config.DevelopmentConfig",
    "production": "celery_config.ProductionConfig",
    "default": "celery_config.DefaultConfig"
}
config_name = os.getenv('CELERY_CONFIGURATION', 'default')
app.config_from_object(config_dict.get(config_name, 'default'))

# logging
logging.config.dictConfig(app.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


@worker_ready.connect
def get_topic(sender=None, headers=None, body=None, **kwargs):
    url = 'https://quantrimang.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    left_bar = soup.find('div', {'class': 'leftbar'})
    for sub_topic in [tree for tree in left_bar.div.div.ul.contents
                      if isinstance(tree, element.Tag)
                      ]:
        try:
            for item in sub_topic.ul.find_all('li'):
                topic = item.a.get('href')

                # send task
                handle_topic.delay(topic)
                logger.info(f'push: {topic}')
        except AttributeError:
            topic = sub_topic.a.get('href')
            
            # send task
            handle_topic.delay(topic)
            logger.info(f'push: {topic}')


def handle_post(post):
    url = post['url']
    pid = url[url.rfind('-') + 1:]
    # pid, title, url, path, desc, content, time
    domain = 'https://quantrimang.com'
    r = requests.get(domain + url)
    soup = BeautifulSoup(r.text, 'lxml')
    title = soup.find('div', {'id': 'contentMain'}).div.h1.get_text().strip()
    path = soup.find('div', {'class': 'breadcrumbs info-detail'}).text.strip().replace('   ', '/')
    content = '\n'.join(
        [item.get_text() for item in soup.find('div', {'class': 'content-detail textview'}).find_all('p')])
    time_publish = soup.find('div', {'class': 'author-info clearfix'}).get_text().strip().partition(', ')[2]

    post['pid'] = pid
    post['title'] = title
    post['path'] = path
    post['content'] = content
    post['time'] = time_publish
    return post


@app.task
def handle_topic(topic):
    domain = 'https://quantrimang.com'
    request_array = []
    while True:
        r = requests.get(domain + topic)
        soup = BeautifulSoup(r.text, 'lxml')
        list_views = soup.find_all('div', {'class': 'listview clearfix'})
        for list_view in list_views:
            post = {}
            for item in list_view.ul.find_all('li'):
                post['url'] = item.a.get('href')
                post['desc'] = repr(item.div.get_text())
                detail_post = handle_post(post)
                logger.info("handle: {}".format(detail_post['pid']))
                request_array.append(InsertOne(detail_post))
                

        # next page
        view_more = soup.find('a', {'class': 'viewmore'})
        if view_more is not None:
            topic = view_more.get('href')
            # check to write db every page
            if len(request_array) >= 1000:
                # Post.bulk_write(request_array)
                request_array = []
                logger.info("write success")
        else :
            break

    # Post.bulk_write(request_array)
