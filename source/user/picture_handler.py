from flask import url_for, current_app
from PIL import Image
import os

def picture_handler(image_load, username):
	old_name = image_load.filename
	ext = old_name.split('.')[-1]
	new_name = str(username) + '.' + ext
	filepath = os.path.join(current_app.root_path, 'static/profile_pics',
		new_name
	)
	output_size = (200, 200)
	pic = Image.open(image_load)
	pic.thumbnail(output_size)
	pic.save(filepath)
	return new_name
