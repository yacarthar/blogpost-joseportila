from flask import (Blueprint, jsonify, url_for,
                   request, redirect
                   )
from webargs import fields
from walrus import Database

from webargs.flaskparser import parser
import pymongo

from models import Post

post = Blueprint('post', __name__)
db_cache = Database(host='localhost', port=6379, db=0)
cache = db_cache.cache()


@post.route('/post', methods=['GET'])
@cache.cached(timeout=10)
def show_all_post():
    # params
    page_args = {
        "page": fields.Int(missing=1, validate=lambda p: p > 0),
        "size": fields.Int(missing=5, validate=lambda p: p > 0)
    }
    args = parser.parse(page_args, request)
    page = args['page']
    size = args['size']

    # query
    query = {}
    result_total = Post.count_documents(query)

    # get result to display
    page_total = result_total // size + 1
    page = min(page_total, page)
    skips = size * (page - 1)
    result_one_page = Post.find(query).skip(skips).limit(size)
    result_one_page_list = []
    for item in result_one_page:
        result_one_page_list.append({
            'pid': item['pid'],
            'url': item['url'],
            'title': item['title'],
            # 'desc': item['desc'],
            'path': item['path'],
            'content': item['content'],
            'time': item['time']
        })

    # pagination
    pagination = {}
    url = (url_for('post.show_all_post')
           + '?page={0}'
           + f'&size={size}'
           )
    pagination['first_page'] = url.format(1)
    pagination['last_page'] = url.format(page_total)
    if page < page_total:
        pagination['next_page'] = url.format(page + 1)
    if 1 < page:
        pagination['previous_page'] = url.format(page - 1)

    return jsonify({
        'result_total': result_total,
        'current_page': page,
        'result': result_one_page_list,
        'pagination': pagination
    })


@post.route('/post/<pid>', methods=['GET'])
def show_one_post(pid):
    # validate
    if not Post.find_one({'pid': pid}):
        return jsonify({'message': 'wrong pid'})
    query = Post.find_one({'pid': pid})
    post_data = {k: v for (k, v) in query.items() if k != '_id'}
    return jsonify(post_data)


@post.route('/post/search', methods=['GET'])
def search_post():
    # params
    search_args = {
        "page": fields.Int(missing=1, validate=lambda p: p > 0),
        "size": fields.Int(missing=5, validate=lambda p: p > 0),
        'keyword': fields.Str(),
        'search_by': fields.Str(missing='title'),
        'sort': fields.Str(missing='time'),
    }
    args = parser.parse(search_args, request)
    page = args['page']
    keyword = args['keyword']
    search_by = args['search_by']
    sort = args['sort']

    #query
    query = {}
    if search_by == 'title':
        query['title'] = {'$regex': keyword, '$options': "$i"}
    elif search_by == 'topic':
        query['path'] = {'$regex': keyword, '$options': "$i"}
    else:
        query['content'] = {'$regex': keyword}
    result_total = Post.count_documents(query)

    # get result to display
    page_total = result_total // size + 1
    page = min(page_total, page)
    skips = size * (page - 1)
    result_one_page = Post.find(query).skip(skips).limit(size).sort(sort, pymongo.DESCENDING)
    result_one_page_list = []
    for item in result_one_page:
        result_one_page_list.append({
            'pid': item['pid'],
            'url': item['url'],
            'title': item['title'],
            # 'desc': item['desc'],
            'path': item['path'],
            'content': item['content'],
            'time': item['time']
        })

    # pagination
    pagination = {}
    url = (url_for('post.search_post')
           + '?page={0}'
           + f'&size={size}&keyword={keyword}&search_by={search_by}&sort={sort}'
           )
    pagination['first_page'] = url.format(1)
    pagination['last_page'] = url.format(page_total)
    if page < page_total:
        pagination['next_page'] = url.format(page + 1)
    if 1 < page:
        pagination['previous_page'] = url.format(page - 1)

    return jsonify({
        'result_total': result_total,
        'current_page': page,
        'result': result_one_page_list,
        'pagination': pagination
    })


@post.route('/post', methods=['POST'])
def create_post():
    # get data body
    data = request.json
    if not data:
        return jsonify({'message': 'json data missing'})
    pid = data.get('pid', None)
    # validate
    if pid is None:
        return jsonify({'message': 'pid (post id) missing'})
    if Post.find_one({'pid': pid}):
        return jsonify({'message': 'post exist'})
    # insert
    Post.insert_one(data)
    return jsonify({
        'message': 'create success',
        'pid': pid
    })


@post.route('/post/<pid>', methods=['PUT'])
def update_post(pid):
    # validate
    if not Post.find_one({'pid': pid}):
        return jsonify({'message': 'wrong pid'})
    # get data body
    data = request.json
    if not data:
        return jsonify({'message': 'json data missing'})
    # update
    Post.find_one_and_update(
        {'pid': pid},
        {'$set': data},
    )
    return redirect(url_for('post.show_one_post', pid=pid))


@post.route('/post/<pid>', methods=['DELETE'])
def delete_post(pid):
    # validate
    if not Post.find_one({'pid': pid}):
        return jsonify({'message': 'wrong pid'})
    # delete
    Post.delete_one({'pid': pid})
    return jsonify({
        'message': 'delete success',
        'pid': pid
    })
