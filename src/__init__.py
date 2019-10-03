from flask import Flask

from src.post.views import post
# from src.user.views import user

app = Flask(__name__)

app.register_blueprint(post)
# app.register_blueprint(user)
