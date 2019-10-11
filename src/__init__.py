import os

from flask import Flask

from src.post.views import post
from src.error_handler.views import error_handler

app = Flask(__name__)

config_dict = {
    "development": "src.config.DevelopmentConfig",
    "production": "src.config.ProductionConfig",
    "default": "src.config.DefaultConfig"
}

config_name = os.getenv('FLASK_ENV', 'default')
app.config.from_object(config_dict.get(config_name, 'default'))


app.register_blueprint(post)
app.register_blueprint(error_handler)
