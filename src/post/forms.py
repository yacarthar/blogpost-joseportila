from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	title = TextField('title', validators=[DataRequired()])
	content = TextField('content', validators=[DataRequired()])
	path = TextField('path', validators=[DataRequired()])
	url = TextField('url', validators=[DataRequired()])
	time = TextField('time', validators=[DataRequired()])
	submit = SubmitField('submit')
