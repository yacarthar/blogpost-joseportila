from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import DataRequired, EqualTo, Email

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
	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('your email has been taken')
	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('your username has been taken')
		

class UpdateForm(FlaskForm):
	name = StringField('name')
	# email = StringField('email', validators = [Email()])
	email = StringField('email')
	# avatar = FileField('avatar', validators = [FileAllowed(['jpg', 'png'])])
	avatar = FileField('avatar')
	submit = SubmitField('Update!!!')
	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('your email has been taken')
	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('your username has been taken')


class UpdateFormSimple(FlaskForm):
	number = IntegerField('id', validators = [DataRequired()])
	submit = SubmitField('Update!!!')
	