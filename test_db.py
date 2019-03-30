from source.models import User, Post
from source import db

# sample_post = Post.query.all()
# for item in sample_post:
# 	db.session.delete(item)

# sample_post = User.query.all()
# for item in sample_post:
# 	db.session.delete(item)

# for instance in db.session.query(User).order_by(User.id):
# 	print(instance.username, instance.email)

# for item in User.query.all():
# 	print(item.username)

a = User.query.one()
print(a)
b = Post.query.all()
print(b)
c = Post.query.first()
print(c)