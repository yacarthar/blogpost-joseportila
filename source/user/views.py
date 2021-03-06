import re

from flask import Blueprint, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
# from werkzeug.exceptions import abort

# from source import db
from source.models import User, Post
from source.user.forms import LoginForm, RegisterForm, UpdateForm
# from source.user.picture_handler import picture_handler

user = Blueprint('user', __name__)


def check_valid_email(email):
    regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z]+$')
    return regex.match(email)


@user.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        if not check_valid_email(email):
            return "Not valid email"
        if User.count_documents({'email': email}):
            return "Email exist!"

        name = form.name.data
        password = form.password.data
        User.insert_one({
           'name': name,
           'email': email,
           'password': generate_password_hash(password),
           'role_admin': False
        })
        return redirect(url_for('user.login'))
    return render_template('register.html', form=form)


@user.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if not User.count_documents({'email': form.email.data}):
            return "email not registered"
        user = User.find_one({'email': form.email.data})
        if not check_password_hash(user['password'], form.password.data):
            return "wrong password"
        login_user(user)
        next_page = request.args.get('next')
        if next_page is None or next_page[0] != '/':
            next_page = url_for('core.index')
        return redirect(next_page)
    return render_template('login.html', form=form)


# @user.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('core.index'))


# @user.route('/account/<int:user_id>', methods=['GET', 'POST'])
# @login_required
# def account(user_id):
#     sample_user = User.query.get_or_404(user_id)
#     if sample_user != current_user:
#         # Forbidden, No Access
#         abort(403)
#     form = UpdateForm()
#     # if form.validate_on_submit():
#     if form.is_submitted():
#         if form.avatar.data:
#             image_link = picture_handler(form.avatar.data, current_user.username)
#             sample_user.avatar = image_link
#         sample_user.username = form.name.data
#         sample_user.email = form.email.data
#         db.session.commit()
#         flash('update success!!!')
#         return redirect(url_for('user.account', user_id=sample_user.id))
#     elif request.method == 'GET':
#         form.name.data = sample_user.username
#         form.email.data = sample_user.email
#     return render_template('account1.html', form=form)


# @user.route("/user/<username>")
# @login_required
# def posts(username):
#     page = request.args.get('page', 1, type=int)
#     user_query = User.query.filter_by(username=username).first()
#     posts_query = Post.query.filter_by(author=user_query).order_by(Post.date.desc()).paginate(page=page, per_page=5)
#     return render_template('posts.html', user=user_query, posts=posts_query)

