from source.models import Post
from source import db

from bs4 import BeautifulSoup
import requests

def update_post(url, post_quota=10000):
    payload = 1
    while True:
        source_code = requests.get(url, params=str(payload))
        soup = BeautifulSoup(source_code.text, 'html.parser')
        posts = soup.find_all("li", {"class":"listitem clearfix"})
        i = 0
        for post in posts:
            title = post.find('a', {'class': 'title'})
            # print(title.text[1:-1])
            link = 'https://quantrimang.com'+title.get('href')
            thumb = post.find('a', {'class': 'thumb'}).img.get('src')
            # print(thumb)
            desc = post.find('div', {'class': 'desc'}).get_text()
            # print(desc)
            single_post = requests.get(link)
            soup_single_post = BeautifulSoup(single_post.text, 'html.parser')
            content_raw = soup_single_post.find("div", {"class":"content-detail textview"})
            content = str(content_raw)
            # print('----------------------------------------------------')
            if Post.query.filter_by(title=title.text[1:-1]).first() == None:
                new_post = Post(
                    title=title.text[1:-1],
                    content=content,
                    user_id=1,
                    thumb=thumb,
                    desc=desc
                )
                db.session.add(new_post)
                db.session.commit()    
            

        # check next_page
        button_next_page = soup.find("div", {"class":"pagination-container"})
        p_href = button_next_page.ul.li.a.get('href')[-1]
        if int(p_href) > int(payload):
            payload = p_href
        else:
            break


if __name__ == '__main__':
    url = 'https://quantrimang.com/unix-va-linux'
    update_post(url)
