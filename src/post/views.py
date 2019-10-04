from flask import (Blueprint, jsonify, url_for,
                   request, redirect
                   )
import pymongo

from src.models import Post

post = Blueprint('post', __name__)


@post.route('/post', methods=['GET'])
def show_all_post():
    # params
    page_param = request.args.get('page', 1, type=int)
    size_param = request.args.get('size', 5, type=int)
    page = max(page_param, 1)
    size = max(size_param, 5)
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
            'desc': item['desc'],
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
        'page_total': page_total,
        'result': result_one_page_list,
        'pagination[': pagination
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
    page_param = request.args.get('page', 1, type=int)
    size_param = request.args.get('size', 5, type=int)
    page = max(page_param, 1)
    size = max(size_param, 5)
    keyword = request.args.get('keyword')
    search_by = request.args.get('search_by', 'title')  # title, topic, content
    sort = request.args.get('sort', 'time')  # time, title

    # query
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
            'desc': item['desc'],
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
        'page_total': page_total,
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
