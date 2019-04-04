from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	title = StringField('title', validators = [DataRequired()])
	# content = TextAreaField('content', validators = [DataRequired()])
	desc = TextField('Description', validators = [DataRequired()])
	content = CKEditorField('content', validators = [DataRequired()])
	submit = SubmitField('submit')