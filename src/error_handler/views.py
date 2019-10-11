from flask import Blueprint, jsonify

error_handler = Blueprint('error_handler', __name__)


@error_handler.errorhandler(404)
def not_found_error(error):
    return jsonify({'message': 'page not found'}), 404
