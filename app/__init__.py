from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    # Load environment variables
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'instance', '.env'))

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = "auth.login"

    # Register blueprints here
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    from .routes.projects import projects_bp
    app.register_blueprint(projects_bp)
    from .routes.applications import applications_bp
    app.register_blueprint(applications_bp)
    from .routes.reviews import reviews_bp
    app.register_blueprint(reviews_bp)
    from .routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)
    # Landing page
    @app.route("/")
    def index():
        return render_template("index.html")
    # Create tables
    with app.app_context():
        from . import models
        db.create_all()

    return app