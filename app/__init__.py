from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__, template_folder='templates')

    app.secret_key = 's3cr3t'
    JWTManager(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
