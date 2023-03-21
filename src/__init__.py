import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs(app.instance_path, exist_ok=True)

    from . import main

    app.register_blueprint(main.bp)

    return app
