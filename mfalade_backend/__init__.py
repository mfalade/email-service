"""."""
from flask import Flask

from extensions import mail
from mfalade_backend.api import api as api_blueprint
from mfalade_backend.config import app_config


def create_app(app_env):
    """Create app instance."""
    app = Flask(__name__)
    app.config.from_object(app_config[app_env])
    
    register_blueprints(app)
    register_extensions(app)

    return app


def register_extensions(app):
    mail.init_app(app)


def register_blueprints(app):
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')