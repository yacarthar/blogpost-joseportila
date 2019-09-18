from flask import Blueprint, render_template, request
# from .. import *
from source.models import User, Post

core = Blueprint('core', __name__)


@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts)


@core.route('/about')
def about():
    user_list = User.query.all()
    return render_template('about.html', user_list=user_list)
