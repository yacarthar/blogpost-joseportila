from flask import url_for, current_app
from PIL import Image
import os

def picture_handler(image_load, username):
	image_name = image_load.filename
	ext = image_name.split('.')[-1]
	storage_filename = image_name + '_' + str(username) + '.' + ext
	filepath = os.path.join(current_app.root_path, 'static/profile_pics',
		storage_filename
	)
	output_size = (200, 200)
	pic = Image.open(image_load)
	pic.thumbnail(output_size)
	pic.save(filepath)
	return storage_filename


# a = picture_handler('/home/vernja/Pictures/Jinx.jpg', 'lonxon')
# print(a)