from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config=Config):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config)

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    from app.main import main
    app.register_blueprint(main)

    return app