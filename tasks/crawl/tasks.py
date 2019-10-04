import time

import redis
from celery import Celery
import requests
from bs4 import BeautifulSoup, element
import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["zed"]
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
                print('push: ', topic)
        except AttributeError:
            topic = sub_topic.a.get('href')
            # send task
            handle_topic.delay(topic)
            print('push: ', topic)


@app.task
def handle_topic(topic):
    domain = 'https://quantrimang.com'
    while True:
        r = requests.get(domain + topic)
        soup = BeautifulSoup(r.text, 'lxml')
        list_views = soup.find_all('div', {'class': 'listview clearfix'})
        for list_view in list_views:
            post = {}
            for item in listview.ul.find_all('li'):
                post['url'] = item.a.get('href')
                post['desc'] = repr(item.div.get_text())
                # send task
                handle_post.delay(post)
                print('push: ', post['url'].partition('-')[-1])

        # next page
        try:
            viewmore = soup.find('a', {'class': 'viewmore'})
            topic = viewmore.get('href')
        except:
            break


@app.task
def handle_post(post):
    url = post['url']
    pid = url[url.rfind('-') + 1:]
    # pid, title, url, path, desc, content, time
    domain = 'https://quantrimang.com'
    r = requests.get(domain + url)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup.prettify())
    title = soup.find('div', {'id': 'contentMain'}).div.h1.get_text().strip()
    path = soup.find('div', {'class': 'breadcrumbs info-detail'}).text.strip().replace('   ', '/')
    content = '\n'.join(
        [item.get_text() for item in soup.find('div', {'class': 'content-detail textview'}).find_all('p')])
    time = soup.find('div', {'class': 'author-info clearfix'}).get_text().strip().partition(', ')[2]

    post['pid'] = pid
    post['title'] = title
    post['path'] = path
    post['content'] = content
    post['time'] = time
    Post.insert_one(post)
    print('write success: ', pid)
