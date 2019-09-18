from flask import (Blueprint, render_template, url_for,
                   redirect, flash, current_app, request, send_from_directory
                   )
from werkzeug.exceptions import abort
from flask_login import login_required, current_user
from source import db
from source.post.forms import PostForm
from source.models import User, Post
import os
from flask_ckeditor import upload_success, upload_fail

post = Blueprint('post', __name__)


# CREATE
@post.route('/post/new', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data,
                        content=form.content.data,
                        user_id=current_user.id,
                        thumb='',
                        desc=form.desc.data
                        )
        print('=======form valid=======')
        db.session.add(new_post)
        db.session.commit()
        flash('Your post has been created !!!')
        return redirect(url_for('user.posts', username=current_user.username))
    else:
        print('=======form not valid=======')
    post_list = Post.query.filter_by(author=current_user).all()
    return render_template('modify.html', form=form, post_list=post_list)


# SHOW
@post.route('/post/<int:post_id>/detail')
@login_required
def show(post_id):
    post_sample = Post.query.get(post_id)
    return render_template('post_content.html', post_sample=post_sample)


# UPDATE
@post.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update(post_id):
    post_sample = Post.query.get_or_404(post_id)
    if post_sample.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post_sample.title = form.title.data,
        post_sample.content = form.content.data,
        post_sample.user_id = current_user.id
        db.session.commit()
        flash('Your post has been updated !!!')
        return redirect(url_for('user.posts'))
    return render_template('modify.html', form=form)


# DELETE
@post.route('/post/<int:post_id>/delete')
@login_required
def delete(post_id):
    post_sample = Post.query.get_or_404(post_id)
    if post_sample.author != current_user:
        abort(403)
    db.session.delete(post_sample)
    db.session.commit()
    flash('Your post has been deleted !!!')
    return redirect(url_for('user.posts', username=current_user.username))


@post.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    # Add more validations here
    extension = f.filename.rsplit('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(current_app.root_path, 'static/post_image', f.filename))
    url = url_for('post.uploaded_files', filename=f.filename)
    return upload_success(url=url)  # return upload_success call


@post.route('/files/<path:filename>')
def uploaded_files(filename):
    path = os.path.join(current_app.root_path, 'static/post_image')
    return send_from_directory(path, filename)


@post.route('/search')
def search():
    page = request.args.get('page', 1, type=int)
    keyword = request.args.get('keyword')
    search_by = request.args.get('search_by')
    # title, author, content
    sort = request.args.get('sort')
    # date, alphabet

    # query
    if search_by == 'title':
        sample = Post.query.filter(Post.title.like(f'%{keyword}%'))
    elif search_by == 'author':
        sample = Post.query.join(User).filter(User.username.like(f'%{keyword}%'))
    else:
        sample = Post.query.filter(Post.content.like(f'%{keyword}%'))

    if sort == 'date':
        post_sorted = sample.order_by(Post.date.desc()).paginate(page=page, per_page=5)
    else:
        post_sorted = sample.order_by(Post.author.username).paginate(page=page, per_page=5)

    return render_template('search.html', post_sorted=post_sorted)
