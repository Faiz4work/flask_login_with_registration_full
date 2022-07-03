from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from myapp.config import Config

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message = "Please login to access Dashboard"
login_manager.login_message_category = "warning"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)

    from myapp.user.routes import user
    app.register_blueprint(user)

    return app