from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from app.models.book_genre import BookGenre

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

#******************** books ********************#
def create_app(testing=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False

    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.book import Book
    from app.routes import books_bp
    app.register_blueprint(books_bp)

    from app.models.author import Author
    from app.routes import authors_bp
    app.register_blueprint(authors_bp)

    from app.models.genre import Genre
    from app.routes import genres_bp
    app.register_blueprint(genres_bp)

    return app

#******************** hello_world ********************#
# def create_app(test_config=None):
#     app = Flask(__name__)

#     from .routes import hello_world_bp
#     app.register_blueprint(hello_world_bp)
    
#     return app