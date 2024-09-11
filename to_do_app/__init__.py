from flask import Flask

from to_do_app.api import api_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object("config.Config")

    app.register_blueprint(api_bp, url_prefix="")

    return app
