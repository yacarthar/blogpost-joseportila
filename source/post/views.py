from flask import (Blueprint, render_template, url_for,
                   redirect, flash, current_app, request, send_from_directory
                   )
# from werkzeug.exceptions import abort
# from flask_login import login_required, current_user
from source import db
from source.post.forms import PostForm
from source.models import User, Post
import os
from flask_ckeditor import upload_success, upload_fail
import pymongo
post = Blueprint('post', __name__)


# CREATE
# @login_required
# @post.route('/post/new', methods=['GET', 'POST'])
# def create():
#     form = PostForm()
#     if form.validate_on_submit():
#         new_post = Post(title=form.title.data,
#                         content=form.content.data,
#                         user_id=current_user.id,
#                         thumb='',
#                         desc=form.desc.data
#                         )
#         print('=======form valid=======')
#         db.session.add(new_post)
#         db.session.commit()
#         flash('Your post has been created !!!')
#         return redirect(url_for('user.posts', username=current_user.username))
#     else:
#         print('=======form not valid=======')
#     post_list = Post.query.filter_by(author=current_user).all()
#     return render_template('modify.html', form=form, post_list=post_list)


# SHOW
# @login_required
@post.route('/post/<pid>/detail')
def show(pid):
    post = Post.find_one({'pid': pid})
    # print(post)
    return render_template('post_detail.html', post=post)


# UPDATE
# @login_required
# @post.route('/post/<post_id>/update', methods=['GET', 'POST'])
# def update(post_id):
#     post_sample = Post.find_one({'post_id': post_id})
#     # if post_sample.author != current_user:
#     #     abort(403)
#     form = PostForm()
#     form.title.data = post_sample['post_title']
#     form.content.data = post_sample['content']
#     form.url.data = post_sample['post_url']
#     form.path.data = post_sample['path']
#     form.time.data = post_sample['time']
#     if form.is_submitted():
#         title = form.title.data
#         content = form.content.data
#         url = form.url.data
#         path = form.path.data
#         time = form.time.data

#         myquery = { 'post_id': post_id }
#         newvalues = { "$set": {
#             'post_title': title,
#             'content': content,
#             'post_url': url,
#             'path': path,
#             'time': time
#         }}
#         Post.update_one(myquery, newvalues)
#         flash('Your post has been updated !!!')
#         return redirect(url_for('post.show', post_id=post_id))
#     return render_template('modify.html', form=form)


# DELETE
# @post.route('/post/<int:post_id>/delete')
# @login_required
# def delete(post_id):
#     post_sample = Post.query.get_or_404(post_id)
#     if post_sample.author != current_user:
#         abort(403)
#     db.session.delete(post_sample)
#     db.session.commit()
#     flash('Your post has been deleted !!!')
#     return redirect(url_for('user.posts', username=current_user.username))


# @post.route('/upload', methods=['POST'])
# def upload():
#     f = request.files.get('upload')
#     # Add more validations here
#     extension = f.filename.rsplit('.')[1].lower()
#     if extension not in ['jpg', 'gif', 'png', 'jpeg']:
#         return upload_fail(message='Image only!')
#     f.save(os.path.join(current_app.root_path, 'static/post_image', f.filename))
#     url = url_for('post.uploaded_files', filename=f.filename)
#     return upload_success(url=url)  # return upload_success call


# @post.route('/files/<path:filename>')
# def uploaded_files(filename):
#     path = os.path.join(current_app.root_path, 'static/post_image')
#     return send_from_directory(path, filename)


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
    number_pages = number_result // page_size + 1
    page_num = min(page_num, number_pages)

    
    skips = page_size * (page_num - 1)
    posts = posts_sorted.skip(skips).limit(page_size)
    # page index
    maxp = min(page_num+5, number_pages)
    minp = max(page_num-5, 1)
    index = [i for i in range(minp, maxp+1)]
    return render_template('search.html', posts=posts, index=index, current_page=page_num,
                            keyword=keyword,
                            sort=sort,
                            search_by=search_by,
                            number_result=number_result
                            )
