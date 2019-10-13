import os

from flask import Flask, jsonify

from src.post.views import post

app = Flask(__name__)

config_dict = {
    "development": "src.config.DevelopmentConfig",
    "production": "src.config.ProductionConfig",
    "default": "src.config.DefaultConfig"
}

config_name = os.getenv('FLASK_ENV', 'default')
app.config.from_object(config_dict.get(config_name, 'default'))


app.register_blueprint(post)


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'message': 'page not found'}), 404
