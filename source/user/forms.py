from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms.file import FileField, FileAllowed

from source.models import User
from flask_login import current_user


class LoginForm(FlaskForm):
	name = StringField('name', validators = [DataRequired()])
	email = StringField('email', validators = [DataRequired(), Email()])
	password = PasswordField('password',
			validators = [DataRequired()]
	)
	submit = SubmitField('login!!!')


class RegisterForm(FlaskForm):
	name = StringField('name', validators = [DataRequired()])
	email = StringField('email', validators = [DataRequired(), Email()])
	password = PasswordField('password', validators = [DataRequired(),
			EqualTo('password_confirm', message='password must match')]
	)
	password_confirm = PasswordField('password', validators = [DataRequired()])
	submit = SubmitField('Register!!!')
	def validate_email(self):
		if User.query.filter_by(email=self.email).first():
			raise ValidationError('your email has been taken')
	def validate_username(self):
		if User.query.filter_by(username=self.username).first():
			raise ValidationError('your username has been taken')
		

class UpdateForm(FlaskForm):
	name = StringField('name', validators = [DataRequired()])
	email = StringField('email', validators = [DataRequired(), Email()])
	avatar = FileField('avatar', validators = [DataRequired(), FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update!!!')
	def validate_email(self):
		if User.query.filter_by(email=self.email).first():
			raise ValidationError('your email has been taken')
	def validate_username(self):
		if User.query.filter_by(username=self.username).first():
			raise ValidationError('your username has been taken')


