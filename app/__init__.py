from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app ():
    app = Flask(__name__)
    app.config.from_object(Config)

    migrate.init_app(app, db)
    db.init_app(app)

    from .controllers.category import category_bp
    app.register_blueprint(category_bp)
    
    with app.app_context():
        db.create_all()
    
    return app