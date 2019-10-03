from flask import Flask
import pymongo

app = Flask(__name__)

# 1 DB #####
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["zed"]

# 2 LoginManager #####
# lm = LoginManager(app)
# lm.init_app(app)
# lm.login_view = 'user.login'

# 3 blueprint #####
from source.core.views import core
# from source.user.views import user
from source.post.views import post
# from source.error_handler.error_handler import error_handler
app.register_blueprint(core)
# app.register_blueprint(user)
app.register_blueprint(post)
# app.register_blueprint(error_handler)
