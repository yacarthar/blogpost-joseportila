import time
import threading
from queue import Queue

import requests
from bs4 import BeautifulSoup, element

from tasks import handle_topic



def main():
    url = 'https://quantrimang.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    leftbar = soup.find('div', {'class':'leftbar'})
    for sub_topic in [tree for tree in leftbar.div.div.ul.contents
                        if isinstance(tree, element.Tag)
                        ]:
        try:
            for item in sub_topic.ul.find_all('li'):
                topic = item.a.get('href')

        except AttributeError:
            topic = sub_topic.a.get('href')

        # send task
        handle_topic.delay(topic)
        print('push: ', topic)


if __name__ == '__main__':
    main()
    