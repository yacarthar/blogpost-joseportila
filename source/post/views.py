from flask import (Blueprint, render_template, url_for,
                   redirect, flash, current_app, request, send_from_directory
                   )
import pymongo

from source.models import Post
post = Blueprint('post', __name__)



@post.route('/post/<pid>/detail')
def show(pid):
    post = Post.find_one({'pid': pid})
    # print(post)
    return render_template('post_detail.html', post=post)


@post.route('/search')
def search():
    keyword = request.args.get('keyword')
    search_by = request.args.get('search_by') # title, topic, content
    sort = request.args.get('sort') # date, alphabet
    # query
    if search_by == 'title':
        query = Post.find({'title': {'$regex': keyword, '$options':"$i"} })
    elif search_by == 'topic':
        query = Post.find({'path': {'$regex': keyword, '$options':"$i"} })
    else:
        query = Post.find({'content': {'$regex': keyword} })

    # sort
    if sort == 'date':
        posts_sorted = query.sort('time', pymongo.DESCENDING)
    else:
        posts_sorted = query.sort('title',  pymongo.ASCENDING)

    # pagination
    number_result = query.count()
    size = request.args.get('size', 10, type=int)
    page_size = max(size, 10)
    page = request.args.get('page', 1, type=int)
    page_num = max(page, 1)
    pages_amount = number_result // page_size + 1
    page_num = min(page_num, pages_amount)

    
    skips = page_size * (page_num - 1)
    posts = posts_sorted.skip(skips).limit(page_size)
    # page index
    maxp = min(page_num+5, pages_amount)
    minp = max(page_num-5, 1)
    index = [i for i in range(minp, maxp+1)]
    return render_template('search.html', posts=posts, index=index, current_page=page_num,
                            keyword=keyword,
                            sort=sort,
                            search_by=search_by,
                            number_result=number_result
                            )
