from flask import Blueprint, render_template, request
from source.models import User, Post

core = Blueprint('core', __name__)


@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    page_num = max(page, 1)
    size = request.args.get('size', 10, type=int)
    page_size = max(size, 10)
    skips = page_size * (page_num - 1)
    posts = Post.find({}).skip(skips).limit(page_size)
    # page list
    number_pages = posts.count() // page_size + 1
    maxp = min(page_num+5, number_pages)
    minp = max(page_num-5, 1)
    index = list(range(minp, maxp+1))
    return render_template('index.html', posts=posts, index=index, current_page=page_num)


