from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


from source.main import db, lm
from flask_login import UserMixin

@lm.user_loader
def load_user(user_id):
	return User.query.get(user_id)



class User(db.Model, UserMixin):
	__tablename__ = 'user_table'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True, index =True, nullable=False)
	email = db.Column(db.String(40), unique=True, index =True, nullable=False)
	avatar = db.Column(db.String(30), nullable=False, default='default.png')
	password_hash = db.Column(db.String(128), nullable=False)
	post = db.relationship('Post', backref='author', lazy=True)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password_hash = generate_password_hash(password)

		
	def check_password(self, passtest):
		return check_password_hash(self.password_hash, passtest)


class Post(db.Model):
	__tablename__ = 'post_table'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(30), nullable=False)
	date = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
	content = db.Column(db.Text(), nullable=False)
	# author = db.relationship('user_table')
	user_id = db.Column(db.String(30), db.ForeignKey('user_table.id'), nullable=False)
	# author_name = db.Column(db.String(30), db.ForeignKey('user_table.username'), nullable=False)

	def __init__(self, title, content, user_id):
		self.title = title
		self.content = content
		self.user_id = user_id