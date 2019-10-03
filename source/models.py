# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime


# from flask_login import UserMixin
from source import db

Post = db["post"]
User = db["user"]

# @lm.user_loader
# def load_user(user_id):
	# return User.query.get(user_id)

