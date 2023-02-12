from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from .models import db

from .models import Service

# db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kvU6yeUkQUzEl5ofCwjqDupaFIUT'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

        # new_service = Service(service_name='Broda + strzyżenie',
        #                       duration='110',
        #                       price='100.00')
        #
        # db.session.add(new_service)
        # db.session.commit()

    return app
