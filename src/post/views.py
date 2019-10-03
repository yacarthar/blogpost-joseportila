from flask import (Blueprint, jsonify, url_for,
                   request
                   )
import pymongo

from src.models import Post
post = Blueprint('post', __name__)



@post.route('/post', methods=['GET'])
def show_all_post():
    #params
    page_param = request.args.get('page', 1, type=int)
    size_param = request.args.get('size', 5, type=int)
    page = max(page_param, 1)
    size = max(size_param, 5)
    # query
    query = Post.find({})
    result_total = Post.count_documents({})
    # get result to display
    page_total = result_total // size + 1
    page = min(page_total, page)
    skips = size * (page - 1)
    query_one_page = query.skip(skips).limit(size)
    # result_one_page = [item for item in query_one_page]
    result_one_page = []
    for item in query_one_page:
        result_one_page.append(item['post_id'])
    # pagination
    next_page = url_for('post.show_all_post') + f'?page={page+1}&size={size}'
    previous_page = url_for('post.show_all_post') + f'?page={page-1}&size={size}'

    return jsonify({
            'result_total': result_total,
            'total pages': page_total,
            'result': result_one_page,
            'next_page': next_page,
            'previous_page': previous_page
    })


# @post.route('/post/<pid>', methods=['GET'])
# def show_one_post(pid):
#     post = Post.find_one({'pid': pid})
#     # print(post)
#     return render_template('post_detail.html', post=post)


# @post.route('/post/search')
# def search_post():
#     keyword = request.args.get('keyword')
#     search_by = request.args.get('search_by') # title, topic, content
#     sort = request.args.get('sort') # date, alphabet
#     # query
#     if search_by == 'title':
#         query = Post.find({'title': {'$regex': keyword, '$options':"$i"} })
#     elif search_by == 'topic':
#         query = Post.find({'path': {'$regex': keyword, '$options':"$i"} })
#     else:
#         query = Post.find({'content': {'$regex': keyword} })

#     # sort
#     if sort == 'date':
#         posts_sorted = query.sort('time', pymongo.DESCENDING)
#     else:
#         posts_sorted = query.sort('title',  pymongo.ASCENDING)

#     # pagination
#     number_result = query.count()
#     size = request.args.get('size', 10, type=int)
#     page_size = max(size, 10)
#     page = request.args.get('page', 1, type=int)
#     page_num = max(page, 1)
#     pages_amount = number_result // page_size + 1
#     page_num = min(page_num, pages_amount)

    
#     skips = page_size * (page_num - 1)
#     posts = posts_sorted.skip(skips).limit(page_size)
#     # page index
#     maxp = min(page_num+5, pages_amount)
#     minp = max(page_num-5, 1)
#     index = [i for i in range(minp, maxp+1)]
#     return render_template('search.html', posts=posts, index=index, current_page=page_num,
#                             keyword=keyword,
#                             sort=sort,
#                             search_by=search_by,
#                             number_result=number_result
#                             )


@post.route('/post', methods=['POST'])
def create_post():
    pass


@post.route('/post', methods=['PUT'])
def update_post():
    pass


@post.route('/post', methods=['DELETE'])
def delete_post():
    pass