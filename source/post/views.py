from flask import (Blueprint, render_template, url_for,
    redirect, session, flash, current_app, request, send_from_directory
)


from flask_login import login_required, current_user
from source.main import db, lm
from source.post.forms import PostForm
from source.models import User, Post
from datetime import datetime
import os
post = Blueprint('post', __name__)

#CREATE
@post.route('/post/new', methods = ['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title = form.title.data,
                        content = form.content.data,
                        user_id = current_user.id
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


#SHOW
@post.route('/post/<post_id>/detail')
@login_required
def show(post_id):
    post_sample = Post.query.get(post_id)
    return render_template('post_content.html', post_sample=post_sample)


#UPDATE
@post.route('/post/<post_id>/update', methods = ['GET', 'POST'])
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


#DELETE
@post.route('/post/<post_id>/delete')
@login_required
def delete(post_id):
    post_sample = Post.query.get_or_404(post_id)
    if post_sample.author != current_user:
        abort(403)
    db.session.delete(post_sample)
    db.session.commit()
    flash('Your post has been deleted !!!')
    return redirect(url_for('user.posts', username=current_user.username))
    

from flask_ckeditor import upload_success, upload_fail

@post.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    # Add more validations here
    extension = f.filename.rsplit('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(current_app.root_path, 'static/post_image', f.filename))
    url = url_for('post.uploaded_files', filename=f.filename)
    return upload_success(url=url) # return upload_success call


@post.route('/files/<path:filename>')
def uploaded_files(filename):
    path = os.path.join(current_app.root_path, 'static/post_image')
    return send_from_directory(path, filename)