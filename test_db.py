from source.models import User, Post
from source import db


# p = Post.query.join(User).filter(User.username.like(r'%ad%')).all()
# print(p)

p = Post.query.get(14)
cont = p.content
print(dir(cont))
print(cont.title)