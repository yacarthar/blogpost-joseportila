from flask import Flask

from src.post.views import post
# from src.user.views import user

app = Flask(__name__)
app.config.from_object('config.default')
app.register_blueprint(post)

