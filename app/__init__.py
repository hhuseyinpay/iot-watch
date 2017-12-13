from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from app.db.queries.user import UserQueries
from app.db.queries.admin import AdminQueries

login_manager = LoginManager()


@login_manager.user_loader
def load_user(ssn):
    admin = AdminQueries.get_admin(ssn)
    if admin is not None:
        return admin
    return UserQueries.get_user(ssn)


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['DEBUG'] = True
    app.secret_key = 's3cr3t'
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    Bootstrap(app)
    JWTManager(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
