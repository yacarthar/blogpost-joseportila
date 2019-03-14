from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from flask_login import login_required, login_user, logout_user, current_user

from source.main import db
from source.models import User, Post
from source.user.forms import LoginForm, RegisterForm, UpdateForm
from source.user.picture_handler import picture_handler



user = Blueprint('user', __name__)


@user.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('user.login'))
    return render_template('register.html', form=form)


@user.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_check = User.query.filter_by(username=form.name.data).first()
        if user_check.check_password(form.password.data) and user_check is not None:
            login_user(user_check)
            flash('login success')
            next = request.args.get('next')
            if next == None or next[0] != '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))



@user.route('/account', methods = ['POST', 'GET'])
@login_required
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.avatar.data:
            username = current_user.username
            image_link = picture_handler(form.avatar.data, username)
            current_user.avatar = image_link
        current_user.username = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('user.account'))
    elif request.method == 'GET':
        form.name.data = current_user.username
        form.email.data = current_user.email
    avatar = url_for('static', filename='profile_pics/' + current_user.avatar)
    return render_template('account.html', form=form, avatar=avatar)


@user.route("/user/<username>")
@login_required
def posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(author=user).order_by(Post.date.desc()).paginate(page=page, per_page=5)
    return render_template('posts.html', user = user, posts=posts)
