from flask import Blueprint, render_template
error_handler = Blueprint('error_handler', __name__)

@error_handler.app_errorhandler(404)
def error_404(error):
	return render_template('error_pages/404.html'), 404


@error_handler.app_errorhandler(403)
def error_403(error):
	return render_template('error_pages/403.html'), 403