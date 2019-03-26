from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
app = Flask(__name__)
app.jinja_env.keep_trailing_newline = True
app.config['SECRET_KEY'] = 'mysecret'

##### 1 DB #####
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///' 
	+ os.path.join(basedir + 'data.sqlite')
)
app.config['TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
Migrate(app, db)

##### 2 LoginManager #####
lm = LoginManager(app)
lm.init_app(app)
lm.login_view = 'user.login'


##### 3 blueprint #####
from source.core.views import core
from source.user.views import user
from source.post.views import post
from source.error_handler.error_handler import error_handler
app.register_blueprint(core)
app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(error_handler)
