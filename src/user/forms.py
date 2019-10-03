from flask_wtf import FlaskForm
from flask_wtf.file import FileField

from wtforms import StringField, PasswordField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, EqualTo, Email

from source.models import User


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password',
                             validators=[DataRequired()]
                             )
    submit = SubmitField('login!!!')


class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    # email = StringField('email', validators=[DataRequired(), Email()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),
                             EqualTo('password_confirm', message='password must match')]
                             )
    password_confirm = PasswordField('password confirm', validators=[DataRequired()])
    submit = SubmitField('Register!!!')

    # @staticmethod
    # def validate_email(field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('your email has been taken')

    # @staticmethod
    # def validate_username(field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('your username has been taken')


class UpdateForm(FlaskForm):
    name = StringField('name')
    # email = StringField('email', validators = [Email()])
    email = StringField('email')
    # avatar = FileField('avatar', validators = [FileAllowed(['jpg', 'png'])])
    avatar = FileField('avatar')
    submit = SubmitField('Update!!!')

    @staticmethod
    def validate_email(field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('your email has been taken')

    @staticmethod
    def validate_username(field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('your username has been taken')


