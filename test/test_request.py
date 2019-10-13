import requests
from bs4 import BeautifulSoup, element


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
            print('send:', topic)
            # handle_topic.delay(topic)
            # logger.info(f'push: {topic}')
    except AttributeError:
        topic = sub_topic.a.get('href')

        # send task
        print('send:', topic)
        # handle_topic.delay(topic)
        # logger.info(f'push: {topic}')