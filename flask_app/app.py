import os

from flask import Flask, jsonify
from flask_cors import CORS

from modules.post.views import post

app = Flask(__name__)
CORS(app)

def configure_app(app):
    """
    Config a flask app
    :return: flask app
    """
    # Load proper config for app
    config_dict = {
        "development": "config.DevelopmentConfig",
        "production": "config.ProductionConfig",
        "default": "config.DefaultConfig"
    }
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(config_dict.get(config_name, 'default'))

    # Correct LOG_FOLDER config
    app.config['LOG_FOLDER'] = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'logs')
    if not os.path.isdir(app.config['LOG_FOLDER']):
        os.makedirs(app.config['LOG_FOLDER'])

    # configure_extensions(app)
    configure_blueprints(app)
    # configure_log_handlers(app)
    # configure_hook(app)
    configure_error_handlers(app)
    # configure_main_route(app)

    return app


def configure_blueprints(app):
    """
    Registry flask url
    :param app: flask app
    :return: not return
    """
    app.register_blueprint(post)


def configure_error_handlers(app):
    """
    Handle error process
    :param app: flask app
    :return: not return
    """
    # @app.errorhandler(404)
    # def not_found_error(e):
    #     return jsonify({'message': 'page not found'}), 404
    pass


configured_app = configure_app(app)
if __name__ == '__main__':
    configured_app.run(host='0.0.0.0')
