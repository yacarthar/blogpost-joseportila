from source.models import User, Post
from source import db


# p = Post.query.join(User).filter(User.username.like(r'%ad%')).all()
# print(p)

p = Post.query.filter(Post.id > 16)
# i=0
for item in p:
	db.session.delete(item)
	db.session.commit()