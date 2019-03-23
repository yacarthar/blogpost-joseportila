from source.models import User, Post
from source.main import db

sample_post = Post.query.all()
for item in sample_post:
	db.session.delete(item)

sample_post = User.query.all()
for item in sample_post:
	db.session.delete(item)