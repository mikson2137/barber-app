from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()
DB_NAME = "database.db"




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kvU6yeUkQUzEl5ofCwjq'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Note

    with app.app_context():
        db.create_all()

    from .views import page_not_found
    app.register_error_handler(404, page_not_found)

    return app