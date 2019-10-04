import logging

import pymongo
import requests
from bs4 import BeautifulSoup, element
from celery import Celery

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    filemode='w',
                    filename='crawl.log'
                    )
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["blog"]
Post = my_db["post"]

app = Celery('post', broker='redis://localhost:6379/0')


@app.task
def get_topic():
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


@app.task
def handle_topic(topic):
    domain = 'https://quantrimang.com'
    while True:
        r = requests.get(domain + topic)
        soup = BeautifulSoup(r.text, 'lxml')
        list_views = soup.find_all('div', {'class': 'listview clearfix'})
        for list_view in list_views:
            post = {}
            for item in list_view.ul.find_all('li'):
                post['url'] = item.a.get('href')
                post['desc'] = repr(item.div.get_text())
                # send task
                handle_post.delay(post)
                pid = post['url'].partition('-')[-1]
                logger.info(f'push: {pid}')

        # next page
        try:
            view_more = soup.find('a', {'class': 'viewmore'})
            topic = view_more.get('href')
        except AttributeError:
            break


@app.task
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
    Post.insert_one(post)
    logger.info(f'write success: {pid}')
