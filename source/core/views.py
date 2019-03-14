from flask import Blueprint, render_template, url_for
# from .. import *
from source.models import User
core = Blueprint('core', __name__)


@core.route('/')
def index():
	user_list = User.query.all()
	print(user_list)
	return render_template('index.html', user_list=user_list)


@core.route('/about')
def about():
	return render_template('about.html')